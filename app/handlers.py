from aiogram import F, Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb


class Register(StatesGroup):
    name = State()
    age = State()
    gender = State()


router = Router()


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


@router.message(Register.name)
async def reister_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    data = await state.get_data()
    await message.answer(f"Хорошо, {data['name']}, Сколько Вам лет?")


@router.message(Register.age)
async def reister_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.gender)
    await message.answer(f"Какого вы пола?", reply_markup=kb.gender_keyboard)


@router.message(Register.gender)
async def reister_age(message: Message, state: FSMContext):
    await state.update_data(gender=message.text)
    data = await state.get_data()
    await message.answer(f"Приятно с вами познакомиться, {data['name']}\n"
                         f"Вам {data['age']} лет и вы {data['gender']}")
    await state.clear()


@router.message()
async def echo_handler(message: Message) -> None:
    pass
