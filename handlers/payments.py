from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.message import ContentType

from states import NaturalPerson
from loader import dp, bot
from data import yookassa_test_token
from data import price
from utils import get_final_sum


# @dp.message_handler(Command(commands='pay'))
@dp.message_handler(state=NaturalPerson.birthday)
async def get_pay(message: types.Message, state=FSMContext):
    """send payment invoice"""
    state_data = await state.get_data()
    final_sum = get_final_sum(state_data, price)
    final_sum = str(final_sum) + '00'
    final_sum = int(final_sum)
    await bot.delete_message(message.from_user.id, message.message_id)
    
    await bot.send_invoice (
        chat_id=message.from_user.id,
        title='Оплатить услугу',
        description='Бронь места на складе',
        payload='storage-invoice',
        provider_token=yookassa_test_token,
        currency="RUB",
        start_parameter='unique-deep-linking-parameter',
        prices=[{
            "label": "руб",
            "amount": final_sum
        }]
    )


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkput_query: types.PreCheckoutQuery):
    """Do final confirmation to complete payment process."""
    await bot.answer_pre_checkout_query(pre_checkput_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_afterpayment(message: types.Message):
    """Process successful payment."""
    if message.successful_payment.invoice_payload == 'storage-invoice':
        state = dp.current_state(user=message.from_user.id)
        await bot.send_message(message.from_user.id, "Заказ оформлен. QR-Code для доступа формируется...")
