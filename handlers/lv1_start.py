from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from states import NaturalPerson

from keyboards import select_storage_kb
from keyboards import what_to_store_kb
from keyboards import season_things_kb
from keyboards import get_location_kb


@dp.message_handler(CommandStart())
async def get_location(message: types.Message, state: FSMContext):
    await bot.delete_message(message.chat.id, message.message_id)
    text = ('Привет! Я помогу вам арендовать личную ячейку '
            'для хранения вещей. Давайте посмотрим адреса складов. '
            'Поделитесь своей локацией, чтобы выбрать ближайший!')

    await message.answer(text=text, reply_markup=get_location_kb())
    await NaturalPerson.location.set()


@dp.message_handler(state=NaturalPerson.location, content_types=['location', 'text'])
async def get_select_storage(message: types.Message, state: FSMContext):
    location = message.location
    if location:
        location = (location.latitude, location.longitude)
        await state.update_data(location=location)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Выбери ближаший склад',
        reply_markup=select_storage_kb(location)
    )
    await NaturalPerson.storage_adress.set()


@dp.callback_query_handler(state=NaturalPerson.storage_adress)
async def get_choose_thing_type(
    call: types.CallbackQuery,
    state: FSMContext
):
    await call.answer()
    await call.message.delete()
    await state.update_data(storage_adress=call.data)
    await NaturalPerson.what_to_store.set()

    await call.message.answer(
        text='Что хотите хранить?',
        reply_markup=what_to_store_kb()
    )


@dp.callback_query_handler(state=NaturalPerson.what_to_store)
async def set_date_from_buttons(
    call: types.CallbackQuery,
    state: FSMContext
):
    await call.answer()
    await call.message.delete()
    await state.update_data(what_to_store=call.data)

    if call.data == 'season_things':
        await call.message.answer(
            text=f'Выберите вещь',
            reply_markup=season_things_kb()
        )
        await NaturalPerson.thing.set()
        return

    elif call.data == 'another_things':
        message_data = await call.message.answer(
            text='Вы можете выбрать размер ячейки от от 1 до 10 кв.м' +
            ' на срок от 1 до 12 месяцев.' +
            '\nСтоимость 599 руб - первый 1 кв.м., ' +
            'далее +150 руб за каждый кв. метр в месяц.' +
            '\n\nВведите размер ячейки:' +
            '(от 1 до 10)'
        )
        await state.update_data(message_to_delete=message_data.message_id)
        await NaturalPerson.cell_size.set()
        return
