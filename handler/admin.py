from aiogram import types, Dispatcher
from config import bot

users = {}


async def python(massage: types.Message):
    user_name = massage.from_user.username
    if user_name:
        user_name = user_name
    else:
        user_name = massage.from_user.first_name
    if massage.from_user.username is not users:
        users[f'@{user_name}'] = massage.from_user.id
        print(users)

    else:
        pass


async def ban(message: types.Message):
    if message.chat.type != 'private':
        message_words = message.text.split()
        username = message_words[1]
        await bot.kick_chat_member(message.chat.id, user_id=users[f'{username}'])
        await message.answer('Он вышел сам!')
    else:
        await message.answer('Попутал')


def reg_ban(db: Dispatcher):
    db.register_message_handler(ban, commands=['ban'], commands_prefix=['!'])


def reg_hand_python(db: Dispatcher):
    db.register_message_handler(python)
