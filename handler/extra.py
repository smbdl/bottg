from aiogram import types, Dispatcher
from config import bot, db


@db.message_handler()
async def echo(massage: types.Message):
    bad_words = ['дурак', 'болван', 'негр', 'гялдирбаш']
    username = f'@{massage.from_user.username}' \
               f'' if massage.from_user.username is not None else massage.from_user.first_name
    for word in bad_words:
        if word in massage.text.lower().replace(' ', ''):
            await bot.delete_message(massage.chat.id, massage.message_id)
            await massage.answer(f'осуждаю {username}')
    if massage.text == "он вышел сам!":
        await bot.pin_chat_message(massage.chat.id, massage.message_id)
    if massage.text == 'python':
        await bot.send_dice(massage.chat.id, emoji='🎯')


def reg_hand_extra(db:Dispatcher):
    db.register_message_handler(echo)