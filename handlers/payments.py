from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot


@dp.message_handler(Command(commands='pay'))
async def get_pay(message:types.Message):
    text = 'Here must be payments'

    await bot.send_message (
        chat_id=message.from_user.id, 
        text=text,
    )