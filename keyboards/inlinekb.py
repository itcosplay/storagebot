from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from utils.get_nearest_storage_boxes import get_nearest_storage_boxes


def select_storage_kb(location):
    keyboard = InlineKeyboardMarkup()

    for box_id, box_location in get_nearest_storage_boxes(location).items():
        keyboard.add(
            InlineKeyboardButton(
                text=f'{box_location.get("address")}, {box_location.get("distance_to_user")}',
                callback_data=box_id,
            )
        )
    return keyboard


def what_to_store_kb():
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text='сезонные вещи',
            callback_data='season_things'
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='другое',
            callback_data='another_things'
        )
    )

    return keyboard


def season_things_kb():
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text='лыжи',
            callback_data='ski'
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='сноуборд',
            callback_data='snowboard'
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='велосипед',
            callback_data='bicycle'
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='комплект колес',
            callback_data='wheel'
        )
    )

    return keyboard


def weeks_or_months_kb():
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text='недели',
            callback_data='weeks'
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='месяцы',
            callback_data='months'
        )
    )

    return keyboard


def pay_kb():
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text='забронировать',
            callback_data='book'
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text='забронировать c промокодом',
            callback_data='promo'
        )
    )

    return keyboard


def back_kb():
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text='Назад',
            callback_data='back'
        )
    )

    return keyboard
