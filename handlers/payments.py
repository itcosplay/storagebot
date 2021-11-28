from aiogram import types
# from aiogram.dispatcher.filters import StateFilter
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.message import ContentType

from states import NaturalPerson
from loader import dp, bot
from data import yookassa_test_token
from utils import get_qr
from utils import delete_user_qr
from utils import get_qr_date
from utils import validate_user_birthday


@dp.message_handler(state=NaturalPerson.birthday)
async def get_pay(message: types.Message, state: FSMContext):
    """send payment invoice"""
    state_data = await state.get_data()
    await bot.delete_message(message.chat.id, state_data['message_to_delete'])
    await message.delete()

    if not validate_user_birthday(message.text):
        message = await message.answer(
            text=('Не получилось обработать данные. \n'
                  'Введите дату рождения в формате дд.мм.гггг.\n'
                  'Например: 01.04.1994')
        )
        await state.update_data(message_to_delete=message.message_id)
        return

    await state.update_data(birthday=message.text)
    # await state.finish()

    message_data = await bot.send_invoice(
        chat_id=message.from_user.id,
        title='Оплатить услугу',
        description='Бронь места на складе',
        payload='storage-invoice',
        provider_token=yookassa_test_token,
        currency="RUB",
        start_parameter='unique-deep-linking-parameter',
        prices=[{
            "label": "руб",
            "amount": 100000
        }]
    )
    await state.update_data(message_to_delete=message_data.message_id)
    await state.set_state('payments')


@dp.pre_checkout_query_handler(state='payments')
async def process_pre_checkout_query(pre_checkput_query: types.PreCheckoutQuery, state: FSMContext):
    """Do final confirmation to complete payment process."""
    state_data = await state.get_data()
    await bot.delete_message(pre_checkput_query.from_user.id, state_data['message_to_delete'])
    await bot.answer_pre_checkout_query(pre_checkput_query.id, ok=True)
    await state.reset_state(with_data=False)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_afterpayment(message: types.Message, state: FSMContext):
    """Process successful payment."""
    if message.successful_payment.invoice_payload == 'storage-invoice':
        await bot.send_message(message.from_user.id, "===========\n===========")
        await bot.send_message(message.from_user.id, "Заказ оплачен! :)")
        state_data = await state.get_data()
        qr_date = get_qr_date(state_data)
        caption = f'Ваш доступ на склад до {qr_date}'
        photo = get_qr(message.from_user.id)
        await bot.send_photo(
            message.from_user.id,
            photo=photo,
            caption=caption
        )
        await bot.send_message(message.from_user.id, "===========\n===========")
        delete_user_qr(message.from_user.id)
