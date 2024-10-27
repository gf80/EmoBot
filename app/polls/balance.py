import datetime
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from app.states import CirculBalance

from sqlalchemy.orm import Session

import app.keyboards as kb

from help import get_score

from database import create_result_test

from visualize import get_circul_balance


_answers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
id_test = 2

async def health_question(message: Message, state: FSMContext):
    if message.text in _answers:
        await state.set_state(CirculBalance.finance)
    else:
        await message.answer("Нет такого варианта ответа.\nПопробуйте снова")
        await state.set_state(CirculBalance.health)
        return 
    await state.update_data(health=message.text)
    await message.answer("Насколько вы чувствуете себя уверенно и стабильно в финансовом плане? (0–10)")


async def finance_question(message: Message, state: FSMContext):
    if message.text in _answers:
        await state.set_state(CirculBalance.work)
    else:
        await message.answer("Нет такого варианта ответа.\nПопробуйте снова")
        await state.set_state(CirculBalance.finance)
        return 
    await state.update_data(finance=message.text)
    await message.answer("Насколько вы довольны своей текущей работой или возможностями для самореализации? (0–10)")


async def work_question(message: Message, state: FSMContext):
    if message.text in _answers:
        await state.set_state(CirculBalance.development)
    else:
        await message.answer("Нет такого варианта ответа.\nПопробуйте снова")
        await state.set_state(CirculBalance.work)
        return 
    await state.update_data(work=message.text)
    await message.answer("Насколько вы удовлетворены своим личностным и профессиональным развитием? (0–10)")


async def development_question(message: Message, state: FSMContext):
    if message.text in _answers:
        await state.set_state(CirculBalance.family)
    else:
        await message.answer("Нет такого варианта ответа.\nПопробуйте снова")
        await state.set_state(CirculBalance.development)
        return 
    await state.update_data(development=message.text)
    await message.answer("Насколько вы довольны отношениями с семьей и близкими людьми? (0–10)")

async def family_question(message: Message, state: FSMContext):
    if message.text in _answers:
        await state.set_state(CirculBalance.social)
    else:
        await message.answer("Нет такого варианта ответа.\nПопробуйте снова")
        await state.set_state(CirculBalance.family)
        return 
    await state.update_data(family=message.text)
    await message.answer("Насколько вы удовлетворены своими дружескими и социальными отношениями? (0–10)")


async def social_question(message: Message, state: FSMContext):
    if message.text in _answers:
        await state.set_state(CirculBalance.relax)
    else:
        await message.answer("Нет такого варианта ответа.\nПопробуйте снова")
        await state.set_state(CirculBalance.social)
        return 
    await state.update_data(social=message.text)
    await message.answer("Насколько вы удовлетворены количеством и качеством своего отдыха и досуга? (0–10)")


async def relax_question(message: Message, state: FSMContext):
    if message.text in _answers:
        await state.set_state(CirculBalance.spirituality)
    else:
        await message.answer("Нет такого варианта ответа.\nПопробуйте снова")
        await state.set_state(CirculBalance.relax)
        return 
    await state.update_data(relax=message.text)
    await message.answer("Насколько вы чувствуете внутреннюю гармонию и удовлетворенность своей духовной жизнью? (0–10)")

async def spirituality_question(message: Message, state: FSMContext, session: Session):
    if message.text not in _answers:
        await message.answer("Нет такого варианта ответа.\nПопробуйте снова")
        await state.set_state(CirculBalance.spirituality)
        return 

    await state.update_data(spirituality=message.text)
    data = await state.get_data()
    score = sum([int(data[i]) for i in data])
    values = [int(data[i]) for i in data]

    print(values)

    create_result_test(session=session, id_user=message.from_user.id, id_test=id_test, score=score)

    await state.clear()
    await message.answer(f"Отлично, вы прошли тест. Ваш результат {score}", reply_markup=kb.remove)

    image_path = await get_circul_balance(values, message.from_user.id, id_test)
    print(image_path)
    await message.answer_photo(photo=FSInputFile(image_path), caption="Вот ваш график!")