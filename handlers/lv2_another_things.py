from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from states import NaturalPerson
from utils import validate_size_cell
from utils import validate_cell_period
from keyboards import pay_kb


@dp.message_handler(state=NaturalPerson.cell_size)
async def set_cell_size(message:types.Message, state:FSMContext):
    state_data = await state.get_data()
    await bot.delete_message(message.chat.id, state_data['message_to_delete'])
    await message.delete()

    cell_size = validate_size_cell(message.text)

    if cell_size is False:
        return

    await state.update_data(cell_size=cell_size)

    message_to_user = 'Стоимость ячейки - 599 руб - первый 1 кв.м.,' + \
    ' далее +150 руб за каждый кв.м в месяц' + \
    '\n\nВведите период хранения цифрой:' + \
    '(от 1 до 12 месяцев)'

    message_data = await message.answer(message_to_user)
    await state.update_data(message_to_delete=message_data.message_id)

    await NaturalPerson.cell_period.set()


@dp.message_handler(state=NaturalPerson.cell_period)
async def set_cell_period(message:types.Message, state:FSMContext):
    state_data = await state.get_data()
    await bot.delete_message(message.chat.id, state_data['message_to_delete'])
    await message.delete()

    cell_period = validate_cell_period(message.text)

    if cell_period is False:
        return

    await state.update_data(cell_period=cell_period)

    message_to_user = 'заказ сформирован'

    await message.answer (
        message_to_user,
        reply_markup=pay_kb()
    )
    
    await state.set_state('self_data')
    # await NaturalPerson.fio.set()