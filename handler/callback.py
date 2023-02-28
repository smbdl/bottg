from aiogram import types, Dispatcher
from config import bot, db


@db.callback_query_handler(text='button')
async def quiz2(call: types.CallbackQuery):
    ques = 'откуда мем?'
    answer = [
        'от верблюда',
        'ъуъ',
        'шрек',
        'мем? семья важнее',
        'наелся и спит',
    ]
    photo2 = open('media/u-suka-10.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo2)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='ъуъ',
        open_period=15,

    )


def reg_hand_callback(db: Dispatcher):
    db.register_callback_query_handler(quiz2, text='button')
