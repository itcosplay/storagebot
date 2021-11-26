import qrcode
import secrets
import string
import os
from PIL import Image, ImageDraw

from aiogram import types
from aiogram.dispatcher.filters import Command
from utils import get_qr
from utils import delete_user_qr

from loader import dp, bot


@dp.message_handler(Command(commands='qr'))
async def send_qr(message: types.Message):
    photo = get_qr(message.from_user.id)
    
    await bot.send_photo (
        chat_id=message.from_user.id,
        photo=photo,
    )

    delete_user_qr(message.from_user.id)

    return
