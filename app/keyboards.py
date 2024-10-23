from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import ReplyKeyboardRemove


gender_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Мужчина")],
                                       [KeyboardButton(text="Женщина")]],
                                       resize_keyboard=True, input_field_placeholder="Введите ваш пол...",
                                       one_time_keyboard=True)

remove = ReplyKeyboardRemove()