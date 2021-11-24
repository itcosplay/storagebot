from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart


from loader import dp, bot
from states import NaturalPerson

from keyboards import select_storage_kb
from keyboards import what_to_store_kb


@dp.message_handler(CommandStart())
async def get_select_storage(message:types.Message):
    text = 'Привет! Я помогу вам арендовать личную ячейку для хранения вещей. Давайте посмотрим адреса складов, чтобы выбрать ближайший!'

    await bot.send_message (
        chat_id=message.from_user.id, 
        text=text,
        reply_markup=select_storage_kb()
    )
    await NaturalPerson.storage_adress.set()


@dp.callback_query_handler(state=NaturalPerson.storage_adress)
async def get_choose_thing_type (
    call:types.CallbackQuery,
    state:FSMContext
):
    await call.answer()
    await call.message.delete()
    await state.update_data(storage_adress=call.data)
    await NaturalPerson.what_to_store.set()

    await call.message.answer (
        text='Что хотите хранить?',
        reply_markup=what_to_store_kb()
    )


@dp.callback_query_handler(state=NaturalPerson.what_to_store)
async def set_date_from_buttons (
    call:types.CallbackQuery,
    state:FSMContext
):
    await call.answer()
    await call.message.delete()
    await state.update_data(what_to_store=call.data)
    
    data_state = await state.get_data()
    adress = data_state['storage_adress']
    type_of_things = data_state['what_to_store']

    await call.message.answer (
        text=f'собранные данные: {adress}; {type_of_things}'
    )

    await state.finish()