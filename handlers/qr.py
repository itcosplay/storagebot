import qrcode
import secrets
import string
import os
from PIL import Image, ImageDraw

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot

# alphabet = string.ascii_letters + string.digits
# password = ''.join(secrets.choice(alphabet) for i in range(20))
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data(password)
# qr.make(fit=True)
# img = qr.make_image(fill_color="black", back_color="white")
# img.save("./data/qrcode.jpg", "JPEG")


@dp.message_handler(Command(commands='qr'))
async def get_qr(message: types.Message):
    text = 'Here must be geo'

    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(password)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("./data/qrcode.jpg", "JPEG")

    photo = open(
        './data/qrcode.jpg',
        'rb'

    )

    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,

    )

    path = os.path.join("./data/qrcode.jpg")
    os.remove(path)
