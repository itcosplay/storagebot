from aiogram import types
from aiogram.dispatcher import FSMContext

from data import price
from loader import dp, bot
from states import NaturalPerson
from utils import validate_thing_amount
from utils import validate_month_amount
from utils import validate_weeks_amount
from utils import get_season_things_price
from utils import message_before_booking
from utils import get_final_sum
from keyboards import weeks_or_months_kb
from keyboards import pay_kb


@dp.callback_query_handler(state=NaturalPerson.thing)
async def set_date_from_buttons (
    call:types.CallbackQuery,
    state:FSMContext
):
    await call.answer()
    await call.message.delete()

    await state.update_data(thing=call.data)

    message_data = await call.message.answer (
        'Укажите количество:\n(от 1 до 4)'
    )
    await state.update_data(message_to_delete=message_data.message_id)

    await NaturalPerson.thing_amount.set()


@dp.message_handler(state=NaturalPerson.thing_amount)
async def get_storage_date(message:types.Message, state:FSMContext):
    state_data = await state.get_data()
    await bot.delete_message(message.chat.id, state_data['message_to_delete'])
    await message.delete()

    thing = state_data['thing']
    amount = validate_thing_amount(message.text)

    if amount is False:
        message_data = await message.answer(
            'Пожалуйста, введите количество вещей числом не более 4'
        )
        await state.update_data(message_to_delete=message_data.message_id)
        await NaturalPerson.thing_amount.set()
        return

    await state.update_data(thing_amount=amount)

    price_text = get_season_things_price (
        thing, 
        amount, 
        price
    )
    
    if thing == 'wheel':
        message_text = price_text + \
        '\n\nВведите колличесво месяцев числом:' + \
        '\n(от 1 до 6)'
        message_data = await bot.send_message (
            message.chat.id,
            message_text
        )
        await NaturalPerson.month_amount.set()
        await state.update_data(message_to_delete=message_data.message_id)

    else:
        message_text = price_text + \
        '\n\nВыберите сроки храниния:'
        await bot.send_message (
            message.chat.id,
            message_text,
            reply_markup=weeks_or_months_kb()
        )
        await NaturalPerson.month_or_week.set()


@dp.callback_query_handler(state=NaturalPerson.month_or_week)
async def set_date_from_buttons (
    call:types.CallbackQuery,
    state:FSMContext
):
    await call.answer()
    await call.message.delete()

    await state.update_data(month_or_week=call.data)

    if call.data == 'weeks':
        time_storage = 'недель'
        avalible_amount = 4
        await NaturalPerson.weeks_amount.set()

    elif call.data == 'months':
        time_storage = 'месяцев'
        avalible_amount = 6
        await NaturalPerson.month_amount.set()

    message_data = await call.message.answer(
        f'Укажите количество {time_storage}:' + \
        f'\n(от 1 до {avalible_amount})'
    )
    await state.update_data(message_to_delete=message_data.message_id)


@dp.message_handler(state=NaturalPerson.month_amount)
async def set_month_amount(message:types.Message, state:FSMContext):
    state_data = await state.get_data()
    await bot.delete_message(message.chat.id, state_data['message_to_delete'])
    await message.delete()

    month_amount = validate_month_amount(message.text)

    if month_amount is False:
        message_data = await message.answer(
            'Пожалуйста, введите количество месяцев числом не более 6'
        )
        await state.update_data(message_to_delete=message_data.message_id)
        await NaturalPerson.month_amount.set()
        return

    await state.update_data(month_amount=month_amount)
    await state.update_data(weeks_amount=0)

    state_data = await state.get_data()
    final_sum = get_final_sum(state_data, price)
    await state.update_data(final_sum=final_sum)
    message_to_user = message_before_booking(state_data)

    await message.answer (
        message_to_user,
        reply_markup=pay_kb()
    )

    await state.set_state('self_data')
    # await state.finish()
    # await NaturalPerson.fio.set()


@dp.message_handler(state=NaturalPerson.weeks_amount)
async def set_weeks_amount(message:types.Message, state:FSMContext):
    state_data = await state.get_data()
    await bot.delete_message(message.chat.id, state_data['message_to_delete'])
    await message.delete()

    weeks_amount = validate_weeks_amount(message.text)

    if weeks_amount is False:
        message_data = await message.answer(
            'Пожалуйста, введите количество недель числом не более 4'
        )
        await state.update_data(message_to_delete=message_data.message_id)
        await NaturalPerson.weeks_amount.set()
        return

    await state.update_data(month_amount=0)
    await state.update_data(weeks_amount=weeks_amount)

    state_data = await state.get_data()
    final_sum = get_final_sum(state_data, price)
    await state.update_data(final_sum=final_sum)
    message_to_user = message_before_booking(state_data)

    await message.answer (
        message_to_user,
        reply_markup=pay_kb()
    )

    await state.set_state('self_data')
    # await state.finish()
    # await NaturalPerson.fio.set()
    