from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
db = Dispatcher(bot=bot)


@db.message_handler(commands=['hello'])
async def start_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f'hello {massage.from_user.first_name}')
    await massage.reply('пока что всё')


@db.message_handler(commands=['quiz'])
async def quiz1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)

    ques = 'откуда мем?'
    answer = [
        'от верблюда',
        'ъуъ',
        'шрек',
        'какой мем, я к семье пошел',
        'наелся и спит',
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


@db.message_handler()
async def echo(massage: types.Message):
    await bot.send_message(massage.from_user.id, massage.text)
    await massage.answer('что-то еще?')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
