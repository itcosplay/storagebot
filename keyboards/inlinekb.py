from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


def select_storage_kb():
    keyboard = InlineKeyboardMarkup()
    
    keyboard.add (
        InlineKeyboardButton (
            text='адрес склада 1',
            callback_data='adress_1'
        )
    )

    keyboard.add (
        InlineKeyboardButton (
            text='адрес склада 2',
            callback_data='adress_2'
        )
    )

    keyboard.add (
        InlineKeyboardButton (
            text='адрес склада 3',
            callback_data='adress_3'
        )
    )


    return keyboard


def what_to_store_kb():
    keyboard = InlineKeyboardMarkup()
    
    keyboard.add (
        InlineKeyboardButton (
            text='сезонные вещи',
            callback_data='season_things'
        )
    )

    keyboard.add (
        InlineKeyboardButton (
            text='другое',
            callback_data='another_things'
        )
    )

    return keyboard