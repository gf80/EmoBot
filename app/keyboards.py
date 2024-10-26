from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import ReplyKeyboardRemove


gender_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Мужчина")],
                                       [KeyboardButton(text="Женщина")]],
                                       resize_keyboard=True, input_field_placeholder="Введите ваш пол...")

mood_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Никогда", )],
                                              [KeyboardButton(text="Редко")],
                                              [KeyboardButton(text="Довольно часто")],
                                              [KeyboardButton(text="Почти всегда")]],
                                              resize_keyboard=True, input_field_placeholder="Выберите один из вариантов...")

def graph_keyboard(tests: list):
    buttons = [[KeyboardButton(text=test)] for test in tests]
    graph_k = ReplyKeyboardMarkup(keyboard=buttons,
                                  resize_keyboard=True)
    return graph_k


remove = ReplyKeyboardRemove()