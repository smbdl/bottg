from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboard.client_kb import *


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
        await massage.answer('Имя: ', reply_markup=cancel_markup)
    else:
        await massage.answer('Только в лс')


async def load_name(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:  # храниться кеш
        date['id'] = massage.from_user.id
        date['username'] = massage.from_user.username
        date['name'] = massage.text
        print(date)
    await FSMAdmin.next()  # переключатель состояния
    await massage.answer('Возраст: ', reply_markup=cancel_markup)


async def load_age(massage: types.Message, state: FSMContext):
    if not massage.text.isdigit():
        await massage.answer("Только цифры")
    elif not 18 <= int(massage.text) <= 99:
        await massage.answer('Только 18-99')
    else:
        async with state.proxy() as date:
            date['age'] = massage.text
            print(date)
        await FSMAdmin.next()
        await massage.answer('Пол: ', reply_markup=gender_markup)


async def load_gender(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:  # храниться кеш
        date['gender'] = massage.text
        print(date)
    await FSMAdmin.next()  # переключатель сост
    await massage.answer('Регион: ', reply_markup=cancel_markup)


async def load_region(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:  # храниться кеш
        date['region'] = massage.text
        print(date)
    await FSMAdmin.next()  # переключатель сост
    await massage.answer('Фото: ', reply_markup=cancel_markup)


async def load_photo(massage: types.Message, state: FSMContext):
    print(massage)
    async with state.proxy() as date:
        date['photo'] = massage.photo[0].file_id

        await massage.answer_photo(date["photo"],
                                   caption=f'{date["name"]} {date["age"]}'
                                           f'{date["gender"]} @{date["username"]}')
    await FSMAdmin.next()
    await massage.answer('Все верно?', reply_markup=submit_markup)


async def submit(massage: types.Message, state: FSMContext):
    if massage.text.lower() == 'да':
        await massage.answer('ты под защитой', reply_markup=start_markup)
        #         подключение к бд и его сохранение
        await state.finish()
    elif massage.text == 'заново':
        await massage.answer('Имя: ', reply_markup=cancel_markup)
        await FSMAdmin.name.set()
    else:
        await massage.answer('не путай берега')


async def cancel_reg(massage: types.Message, state: FSMContext):
    currents_state = await state.get_state()  # проверка состояния
    if currents_state is not None:
        await state.finish()
        await massage.answer('ты больше не под защитой')


def reg_hand_anketa(db: Dispatcher):
    db.register_message_handler(fsm_start, commands=['reg'])
    db.register_message_handler(load_name, state=FSMAdmin.name)
    db.register_message_handler(load_age, state=FSMAdmin.age)
    db.register_message_handler(load_gender, state=FSMAdmin.gender)
    db.register_message_handler(load_region, state=FSMAdmin.region)
    db.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    db.register_message_handler(submit, state=FSMAdmin.submit)
