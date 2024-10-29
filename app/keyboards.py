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

balance_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="0", )],
                                              [KeyboardButton(text="1")],
                                              [KeyboardButton(text="2")],
                                              [KeyboardButton(text="3")],
                                              [KeyboardButton(text="4")],
                                              [KeyboardButton(text="5")],
                                              [KeyboardButton(text="6")],
                                              [KeyboardButton(text="7")],
                                              [KeyboardButton(text="8")],
                                              [KeyboardButton(text="9")],
                                              [KeyboardButton(text="10")]],
                                              resize_keyboard=True, input_field_placeholder="Выберите один из вариантов...")

def get_keyboard(texts: list):
    buttons = [[KeyboardButton(text=text)] for text in texts]
    k = ReplyKeyboardMarkup(keyboard=buttons,
                                  resize_keyboard=True)
    return k


remove = ReplyKeyboardRemove()