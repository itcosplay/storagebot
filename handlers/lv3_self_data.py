from aiogram import types
from aiogram.dispatcher import FSMContext

from data import promo
from loader import dp, bot
from states import NaturalPerson
from utils import validate_user_name
from utils import message_before_booking
from keyboards import pay_kb


@dp.callback_query_handler(state='self_data')
async def set_date_from_buttons(
    call: types.CallbackQuery,
    state: FSMContext
):
    await call.answer()
    await call.message.delete()

    if call.data == 'book':

        message_data = await call.message.answer('Введите ФИО')
        await state.update_data(message_to_delete=message_data.message_id)

        await NaturalPerson.fio.set()

    else:

        message_data = await call.message.answer('Введите промокод')
        await state.update_data(message_to_delete=message_data.message_id)

        await NaturalPerson.promo.set()


@dp.message_handler(state=NaturalPerson.promo)
async def set_weeks_amount(message:types.Message, state:FSMContext):
    state_data = await state.get_data()
    await bot.delete_message(message.chat.id, state_data['message_to_delete'])
    await message.delete()

    if message.text == promo:
        final_sum = round(state_data['final_sum'] * 0.8)
        await state.update_data(final_sum=final_sum)
        message_data = await message.answer('Ваш промокод подтвержен! Введите ФИО')
        await state.update_data(message_to_delete=message_data.message_id)
        await NaturalPerson.fio.set()

    else:
        message_to_user = message_before_booking(state_data)
        await message.answer('Такого промокода нет...\n' + message_to_user, 
        reply_markup=pay_kb())
        await state.set_state('self_data')


@dp.message_handler(state=NaturalPerson.fio)
async def set_weeks_amount(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    await bot.delete_message(message.chat.id, state_data['message_to_delete'])
    await message.delete()

    if not validate_user_name(message.text):
        message_data = await message.answer(
            text=('Не получилось обработать данные. \n'
                  'Введите ФИО, как у вас в паспорте.')
        )
        await state.update_data(message_to_delete=message_data.message_id)
        return

    await state.update_data(fio=message.text)

    message_data = await message.answer('Введите серию и номер паспорта')
    await state.update_data(message_to_delete=message_data.message_id)
    await NaturalPerson.passport.set()


@dp.message_handler(state=NaturalPerson.passport)
async def set_weeks_amount(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    await bot.delete_message(message.chat.id, state_data['message_to_delete'])
    await message.delete()

    await state.update_data(passport=message.text)

    message_data = await message.answer('Введите дату рождения в формате дд.мм.гггг')
    await state.update_data(message_to_delete=message_data.message_id)
    await NaturalPerson.birthday.set()

