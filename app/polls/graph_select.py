import datetime
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.states import Mood

from sqlalchemy.orm import Session

import app.keyboards as kb

from database import get_results_last_month, get_tests


async def graph_create(message: Message, state: FSMContext, session: Session):
    data = get_tests(session, message.from_user.id)
    for test in data:
        if test["name"] == message.text:
            rows = get_results_last_month(session, message.from_user.id, test["id"])
            for row in rows:
                print(f"Тест ID: {row.id_test}, Результат: {row.score}, Дата: {row.date_passed}")
            break
    await state.clear()