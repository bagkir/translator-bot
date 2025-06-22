from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums import ChatType

from app.config_logger import setup_logger
from app.services.translate import translate_text, detect_language
from app.users.dao import UserDAO

router = Router()

logger = setup_logger(__name__)


@router.message(F.text, F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}))
async def handle_group_message(message: Message) -> None:
    logger.info("handle for translating")
    try:
        sender_lang: str = await detect_language(message.text)
        all_users = await UserDAO.find_all()
        for user in all_users:
            if user.language == sender_lang and user.tg_id != message.from_user.id:
                translated = await translate_text(
                    text=message.text,
                    dest_lang=sender_lang,
                )
                await message.bot.send_message(
                    chat_id=user.tg_id,
                    text=f"🌍 {translated}",
                )
    except Exception as e:
        logger.error(f"Error in handle_group_message: {e}")
