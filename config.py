from aiogram import Bot, Dispatcher, types
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config('TOKEN')
ADMIN = (974793573,)
bot = Bot(TOKEN)
db = Dispatcher(bot=bot, storage=storage)
