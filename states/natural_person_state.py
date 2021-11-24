from aiogram.dispatcher.filters.state import StatesGroup, State


class NaturalPerson(StatesGroup):
    storage_adress = State()
    what_to_store = State()