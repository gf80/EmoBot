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
    graph_test = State()


# Класс для опроса для круга баланса
class CirculBalance(StatesGroup):
    health = State()
    finance = State()
    work = State()
    development = State()
    family = State()
    social = State()
    relax = State()
    spirituality = State()