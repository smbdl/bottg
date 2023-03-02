from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text


class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    region = State()
    photo = State()
    submit = State()


async def fsm_start(massage: types.Message):
    if massage.chat.type == 'private':
        await FSMAdmin.name.set()
        await massage.answer('как тиба звать родной?')
    else:
        await massage.answer('го 1 на 1')


async def load_name(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:  # храниться кеш
        date['id'] = massage.from_user.id
        date['username'] = massage.from_user.username
        date['name'] = massage.text
        print(date)
    await FSMAdmin.next()  # переключатель состояния
    await massage.answer('сколько живешь?')


async def load_age(massage: types.Message, state: FSMContext):
    if not massage.text.isdigit():
        await massage.answer("пиши числа родной")
    elif not 18 <= int(massage.text) <= 99:
        await massage.answer('ты не такой как все')
    else:
        async with state.proxy() as date:
            date['age'] = massage.text
            print(date)
        await FSMAdmin.next()
        await massage.answer('какой ты пол?')


async def load_gender(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:  # храниться кеш
        date['gender'] = massage.text
        print(date)
    await FSMAdmin.next()  # переключатель сост
    await massage.answer('откуда?')


async def load_region(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:  # храниться кеш
        date['region'] = massage.text
        print(date)
    await FSMAdmin.next()  # переключатель сост
    await massage.answer('фотку кинь да?')


def reg_hand_anketa(db: Dispatcher):
    db.register_message_handler(fsm_start, commands=['reg'])
    db.register_message_handler(load_name, state=FSMAdmin.name)
    db.register_message_handler(load_age, state=FSMAdmin.age)
    db.register_message_handler(load_gender, state=FSMAdmin.gender)
    db.register_message_handler(load_region, state=FSMAdmin.region)