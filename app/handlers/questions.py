from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from app.keyboards.for_questions import get_yes_no_kb, get_rus_en_kb
from app.users.dao import UserDAO

router = Router()


@router.message(Command("settings"))
async def cmd_start(message: Message) -> None:
    await message.answer(
        "вам переводить?",
        reply_markup=get_yes_no_kb()
    )


@router.message(F.text.lower() == "да")
async def answer_yes(message: Message) -> None:
    await message.answer(
        "с какого языка вам переводить?",
        reply_markup=get_rus_en_kb()
    )


@router.message(F.text.lower() == "ru")
async def answer_yes(message: Message) -> None:
    await UserDAO.add_user(message.from_user, language="ru", translate_mode=True)
    await message.answer(
        "bobr kurwa!",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text.lower() == "en")
async def answer_yes(message: Message) -> None:
    await UserDAO.add_user(message.from_user, language="en", translate_mode=True)
    await message.answer(
        "бобр курва!",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text.lower() == "нет")
async def answer_no(message: Message) -> None:
    await UserDAO.add_user(message.from_user, language="en", translate_mode=False)
    await message.answer(
        "Жаль...",
        reply_markup=ReplyKeyboardRemove()
    )
