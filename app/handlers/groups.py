from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums import ChatType
import logging

logging.basicConfig(level=logging.INFO)
from app.services.translate import translate_text, detect_language

from app.users.dao import UserDAO

router = Router()


@router.message(F.text, F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}))
async def handle_group_message(message: Message):
    try:
        sender_lang: str = await detect_language(message.text)
        all_users = await UserDAO.find_all()
        for user in all_users:
            # if user.tg_id == message.from_user.id:
            #     continue
            if user.language != sender_lang and user.tg_id != message.from_user.id:
                translated = await translate_text(
                    text=message.text,
                    dest_lang=sender_lang,
                )
                await message.bot.send_message(
                    chat_id=user.tg_id,
                    text=f"🌍 {translated}",
                )
    except Exception as e:
        logging.error(f"Error in handle_group_message: {e}")
