from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    kb.button(text="Да")
    kb.button(text="Нет")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def get_rus_en_kb() -> ReplyKeyboardMarkup:
    kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    kb.button(text="ru")
    kb.button(text="en")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
