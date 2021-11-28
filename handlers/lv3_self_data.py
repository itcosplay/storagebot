from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from states import NaturalPerson
# from utils import validate_thing_amount
# from utils import validate_month_amount
# from utils import validate_weeks_amount
# from utils import get_season_things_price
# from keyboards import weeks_or_months_kb
# from keyboards import pay_kb


@dp.callback_query_handler(state='self_data')
async def set_date_from_buttons (
    call:types.CallbackQuery,
    state:FSMContext
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

    await state.update_data(promo=message.text)
    await NaturalPerson.fio.set()



@dp.message_handler(state=NaturalPerson.fio)
async def set_weeks_amount(message:types.Message, state:FSMContext):
    state_data = await state.get_data()
    await bot.delete_message(message.chat.id, state_data['message_to_delete'])
    await message.delete()

    await state.update_data(fio=message.text)

    message_data = await message.answer('Введите серию и номер паспорта')
    await state.update_data(message_to_delete=message_data.message_id)
    await NaturalPerson.passport.set()


@dp.message_handler(state=NaturalPerson.passport)
async def set_weeks_amount(message:types.Message, state:FSMContext):
    state_data = await state.get_data()
    await bot.delete_message(message.chat.id, state_data['message_to_delete'])
    await message.delete()

    await state.update_data(passport=message.text)

    message_data = await message.answer('Введите дату рождения')
    await state.update_data(message_to_delete=message_data.message_id)
    await NaturalPerson.birthday.set()
    
# @dp.message_handler(state=NaturalPerson.birthday)


# @dp.message_handler(state=NaturalPerson.birthday)
# async def set_weeks_amount(message:types.Message, state:FSMContext):
#     state_data = await state.get_data()
#     await bot.delete_message(message.chat.id, state_data['message_to_delete'])
#     await message.delete()

#     await state.update_data(birthday=message.text)

#     message_data = await message.answer('ТУТ ОПЛАЧИВАЕТСЯ ЗАКАЗ')
#     await state.update_data(message_to_delete=message_data.message_id)

#     await state.set_state('payments')
#     await state.finish()
