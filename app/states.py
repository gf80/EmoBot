from aiogram.fsm.state import State, StatesGroup


# Класс регистрации пользова
class Register(StatesGroup):
    name = State()
    age = State()
    gender = State()


# Класс опросника настроения
class Mood(StatesGroup):
    first = State()
    second = State()
    third = State()
    forth = State()
    fifth = State()

# Класс выбора графика
class GraphSelection(StatesGroup):
    waiting_for_test = State()