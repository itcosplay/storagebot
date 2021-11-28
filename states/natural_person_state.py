from aiogram.dispatcher.filters.state import StatesGroup, State


class NaturalPerson(StatesGroup):
    storage_adress = State()
    what_to_store = State()
    cell_size = State()
    cell_period = State()
    thing = State()
    thing_amount = State()
    month_or_week = State()
    weeks_amount = State()
    month_amount = State()
    final_sum = State()
    fio = State()
    passport = State()
    birthday = State()
    location = State()

    message_to_delete = State()
