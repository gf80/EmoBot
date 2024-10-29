import datetime
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from app.states import Mood

from sqlalchemy.orm import Session

import app.keyboards as kb

from help import get_score

from database import create_result_test, create_test, get_tests, get_results_last_month
from visualize import mood_diagramma

_answers = ["Никогда", "Редко", "Довольно часто", "Почти всегда"]
id_test = 1

async def first_question(message: Message, state: FSMContext):
    if message.text in _answers:
        await state.set_state(Mood.second)
    else:
        await message.answer("Нет такого варианта ответа.\nПопробуйте снова")
        await state.set_state(Mood.first)
        return 
    await state.update_data(first=get_score(_answers, message.text))
    await message.answer("2. Как часто вы чувствуете удовлетворение от своей жизни?")


async def second_question(message: Message, state: FSMContext):
    if message.text in _answers:
        await state.set_state(Mood.third)
    else:
        await message.answer("Нет такого варианта ответа.\nПопробуйте снова")
        await state.set_state(Mood.second)
        return 
    await state.update_data(second=get_score(_answers, message.text))
    await message.answer("3. Как часто вы чувствуете негативные эмоции, такие как гнев, раздражение или печаль?")


async def third_question(message: Message, state: FSMContext):
    if message.text in _answers:
        await state.set_state(Mood.forth)
    else:
        await message.answer("Нет такого варианта ответа.\nПопробуйте снова")
        await state.set_state(Mood.third)
        return 
    await state.update_data(third=get_score(_answers, message.text))
    await message.answer("4. Как часто вы чувствуете, что можете справиться с трудностями?")


async def forth_question(message: Message, state: FSMContext):
    if message.text in _answers:
        await state.set_state(Mood.fifth)
    else:
        await message.answer("Нет такого варианта ответа.\nПопробуйте снова")
        await state.set_state(Mood.forth)
        return 
    await state.update_data(forth=get_score(_answers, message.text))
    await message.answer("5. Как часто вам удается сохранять позитивный настрой в течение дня?")


async def fifth_question(message: Message, state: FSMContext, session: Session):
    if message.text not in _answers:
        await message.answer("Нет такого варианта ответа.\nПопробуйте снова")
        await state.set_state(Mood.fifth)
        return 

    data = await state.get_data()
    score = sum([int(data[i]) for i in data])

    create_result_test(session=session, id_user=message.from_user.id, id_test=id_test, score=score)

    await state.clear()

    await message.answer(f"Отлично, вы прошли тест. Ваш результат {score}", reply_markup=kb.remove)

    if score <= 5:
        await message.answer("Низкий уровень настроения. Возможно, требуется внимание к улучшению эмоционального состояния.")
    elif score <= 10:
        await message.answer("Средний уровень настроения. Возможны колебания, но в целом настроение остается удовлетворительным.")
    else:
        await message.answer("Высокий уровень настроения. Вероятно, вы чувствуете себя позитивно большую часть времени.")

    data = get_results_last_month(session, message.from_user.id, id_test)
    date = [d['date_passed'] for d in data]
    height = [d['score'] for d in data]

    image_path = await mood_diagramma(message.from_user.id, id_test, date, height)
    await message.answer_photo(photo=FSInputFile(image_path), caption="Вот ваш график!")