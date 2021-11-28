from aiogram import types
from aiogram.dispatcher import FSMContext

from data import price
from loader import dp, bot
from states import NaturalPerson
from utils import validate_size_cell
from utils import validate_cell_period
from utils import message_before_booking
from utils import get_costs_cell_without_period
from keyboards import pay_kb
from keyboards import back_kb


@dp.message_handler(state=NaturalPerson.cell_size)
async def set_cell_size(message:types.Message, state:FSMContext):
    state_data = await state.get_data()
    await bot.delete_message(message.chat.id, state_data['message_to_delete'])
    await message.delete()

    cell_size = validate_size_cell(message.text)

    if cell_size is False:
        message_data = await message.answer(
            'Пожалуйста, введите размер ячеки цифрой от 1 до 10'
        )
        await state.update_data(message_to_delete=message_data.message_id)
        await NaturalPerson.cell_size.set()
        return

    await state.update_data(cell_size=cell_size)

    state_data = await state.get_data()

    cost_first_month, cost_other_month = get_costs_cell_without_period(state_data, price)

    message_to_user = f'Стоимость аренды составит: {cost_first_month} руб.,' + \
    f' далее +{cost_other_month} руб. за каждый месяц' + \
    '\n\nВведите период хранения цифрой:' + \
    '(от 1 до 12 месяцев)'

    message_data = await message.answer(
        message_to_user,
        reply_markup=back_kb()
    )
    await state.update_data(message_to_delete=message_data.message_id)

    await NaturalPerson.cell_period.set()


@dp.callback_query_handler(state=NaturalPerson.cell_period)
async def set_date_from_buttons (
    call:types.CallbackQuery,
    state:FSMContext
):
    await call.answer()
    await call.message.delete()

    message_data = await call.message.answer(
            text='Вы можете выбрать размер ячейки от от 1 до 10 кв.м' +
            ' на срок от 1 до 12 месяцев.' +
            '\nСтоимость 599 руб - первый 1 кв.м., ' +
            'далее +150 руб за каждый кв. метр в месяц.' +
            '\n\nВведите размер ячейки:' +
            '\n(от 1 до 10)'
        )
    await state.update_data(message_to_delete=message_data.message_id)
    await NaturalPerson.cell_size.set()
    return


@dp.message_handler(state=NaturalPerson.cell_period)
async def set_cell_period(message:types.Message, state:FSMContext):
    state_data = await state.get_data()
    await bot.delete_message(message.chat.id, state_data['message_to_delete'])
    await message.delete()
    cell_period = validate_cell_period(message.text)

    if cell_period is False:
        message_data = await message.answer(
            'Пожалуйста, введите период хранения цифрой от 1 до 12'
        )
        await state.update_data(message_to_delete=message_data.message_id)
        await NaturalPerson.cell_period.set()
        return

    await state.update_data(cell_period=cell_period)

    state_data = await state.get_data()
    message_to_user = message_before_booking(state_data)

    await message.answer (
        message_to_user,
        reply_markup=pay_kb()
    )
    
    await state.set_state('self_data')
    # await NaturalPerson.fio.set()