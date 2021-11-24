from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import bot_token

# from utils.db_api.sqlite import Database
# db = Database()
# some_data = db.get_some_data()

bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
# dp = Dispatcher(bot)
dp = Dispatcher(bot, storage=storage)