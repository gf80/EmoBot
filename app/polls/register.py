from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.states import Register

from sqlalchemy.orm import Session

from database import create_user

import app.keyboards as kb



# Функция для обработки возраста
async def ask_age(message: Message, state: FSMContext):
    await state.update_data(name=message.text)  # сохраняем имя
    await state.set_state(Register.age)
    data = await state.get_data()
    await message.answer(f"Хорошо, {data['name']}, Сколько Вам лет?")

# Функция для обработки пола
async def ask_gender(message: Message, state: FSMContext):
    await state.update_data(age=message.text)  # сохраняем возраст
    await state.set_state(Register.gender)
    await message.answer(f"Какого вы пола?", reply_markup=kb.gender_keyboard)

# Функция для завершения регистрации и сохранения данных в базу
async def complete_registration(message: Message, state: FSMContext, session: Session):
    await state.update_data(gender=message.text)  # сохраняем пол
    data = await state.get_data()
    print(data)
    # Создаём или обновляем пользователя в базе данных
    create_user(session, id=message.from_user.id, name=data['name'], age=int(data['age']), gender=data['gender'])
    await message.answer(f"Приятно с вами познакомиться, {data['name']}! 🎉\n"
                         f"Возраст: {data['age']} лет\n"
                         f"Пол: {data['gender']}", 
                         reply_markup=kb.remove)
    await message.answer("Отлично, давай начнем исправлять твое эмоциональное состояние\n"
                             "Вот, какие тесты я могу тебе предложить:\n\n"
                             "/mood - Тест на настроение\n"
                             "/balance - Тест для круга баланса", 
                             reply_markup=kb.remove)
    await state.clear()