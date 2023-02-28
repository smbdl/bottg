from aiogram import Bot, Dispatcher, types
from decouple import config

TOKEN = config('TOKEN')
ADMIN = (974793573, )
bot = Bot(TOKEN)
db = Dispatcher(bot=bot)
