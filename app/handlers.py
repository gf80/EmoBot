from aiogram import F, Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from sqlalchemy.orm import Session
import app.polls as polls
import app.keyboards as kb

from database import *

from app.states import *


router = Router()

# Начальная команда start
@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(Register.name)
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}! 👋 \n"
                         "Я — твой личный помощник для заботы о твоём эмоциональном здоровье! 💙\n"
                        "\n"
                        "С моей помощью ты сможешь:\n"
                        "\n"
                        "  · Следить за своим настроением и выявлять важные изменения 📊\n"
                        "  · Анализировать свои эмоции и лучше понимать их 🌈\n"
                        "  · Получать советы по тому, как справляться со стрессом и поддерживать внутреннее равновесие 🧘‍♂️\n"
                        "\n"
                        "Я буду напоминать тебе о том, что важно заботиться о себе и своём внутреннем мире.\n"
                        )
    await message.answer("Давай познакомимся для начала. Скажи, как мне к тебе лучше обращаться? 😊")

# Обработка команды /me для вывода информации о пользователе
@router.message(Command(commands="me"))
async def me_handler(message: Message):
    user = get_user(session, message.from_user.id)
    if user:
        await message.answer(f"Ваши данные:\n"
                             f"Имя: {user.name}\n"
                             f"Возраст: {user.age}\n"
                             f"Пол: {user.gender}")
        await message.answer("Отлично, давай начнем исправлять твое эмоциональное состояние\n"
                             "Вот, какие тесты я могу тебе предложить:\n\n"
                             "/mood - Тест на настроение")

# Старт теста на настроение
@router.message(Command(commands="mood"))
async def mood_handler(message: Message, state: FSMContext):
    await state.set_state(Mood.first)
    await message.answer("1. Как часто вы чувствуете себя бодрым и энергичным?", reply_markup=kb.mood_keyboard)

# Команда для постороения графиков
@router.message(Command(commands="graph"))
async def graph_handler(message: Message, state: FSMContext):
    tests = get_tests(session, message.from_user.id)
    name_tests = [name["name"] for name in tests]
    await message.answer("Выберите какой график вам показать", reply_markup=kb.graph_keyboard(name_tests))
    await state.set_state(GraphSelection.waiting_for_test)

# Создать граф
@router.message(GraphSelection.waiting_for_test)
async def graph_create_handler(message: Message, state: FSMContext):
    await polls.graph_select.graph_create(message, state, session)

# Обработка ввода имени
@router.message(Register.name)
async def register_name_handler(message: Message, state: FSMContext):
    await polls.register.ask_age(message, state)

# Обработка ввода возраста
@router.message(Register.age)
async def register_age_handler(message: Message, state: FSMContext):
    await polls.register.ask_gender(message, state)

# Обработка ввода пола и завершение регистрации
@router.message(Register.gender)
async def register_gender_handler(message: Message, state: FSMContext):
    await polls.register.complete_registration(message, state, session)

# Обработка ввода первого ответа
@router.message(Mood.first)
async def mood_first_handler(message: Message, state: State):
    await polls.mood.first_question(message, state)

# Обработка ввода второго ответа
@router.message(Mood.second)
async def mood_second_handler(message: Message, state: State):
    await polls.mood.second_question(message, state)

# Обработка ввода третьего ответа
@router.message(Mood.third)
async def mood_third_handler(message: Message, state: State):
    await polls.mood.third_question(message, state)

# Обработка ввода четвертого ответа
@router.message(Mood.forth)
async def mood_forth_handler(message: Message, state: State):
    await polls.mood.forth_question(message, state)

# Обработка ввода пятого ответа
@router.message(Mood.fifth)
async def mood_fifth_handler(message: Message, state: State):
    await polls.mood.fifth_question(message, state, session)

# Обработчик для всех остальных сообщений
@router.message()
async def echo_handler(message: Message):
    await message.answer("Я не понимаю эту команду. Попробуйте /start или /me.")

