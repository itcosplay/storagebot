
from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup


def get_location_kb():
    keybord = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,)
    keybord.add(
        KeyboardButton('Поделиться',
                       request_location=True,
                       )
    )
    return keybord
