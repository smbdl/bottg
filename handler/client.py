from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, db
from keyboard.client_kb import start_markup


@db.message_handler(commands=['start'])
async def start_handler(massage: types.Message):
    await bot.send_message(massage.chat.id, f"What's up, @{massage.from_user.username}",
                           reply_markup=start_markup)


@db.message_handler(commands=['quiz'])
async def quiz1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)

    ques = 'откуда мем?'
    answer = [
        'от верблюда',
        'ъуъ',
        'наелся и спит',
        'мем? cемья важнее',
    ]
    photo = open('media/f0e1c3b4b532fbc70a73e022ffcf35f2_fitted_1332x0.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    # await massage.answer_poll()
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='семья важна',
        open_period=15,
        reply_markup=markup
    )


@db.message_handler(commands=['info'])
async def info_hand(massage: types.Message):
    await massage.answer('I am Gosha :)')


def reg_client(db: Dispatcher):
    db.register_message_handler(start_handler, commands=['start'])
    db.register_message_handler(quiz1, commands=['quiz'])
    db.register_message_handler(info_hand, commands=['info'])
