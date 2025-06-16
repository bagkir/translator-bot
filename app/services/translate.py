from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat

from app.config import settings
from app.config_logger import setup_logger

logger = setup_logger(__name__)

giga = GigaChat(
    credentials=settings.AUTH_KEY.get_secret_value(),
    verify_ssl_certs=False,
)
messages = [
    SystemMessage(content="Ты бот-программист, который переводит сообщения в Telegram.")
]


async def detect_language(text) -> str:
    logger.debug("detecting language...")
    ru_chars = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

    count_ru = sum(1 for char in text.lower() if char in ru_chars)
    count_en = len([char for char in text.lower() if char.isascii()])

    try:
        if count_ru > count_en:
            return "ru"
        return "en"
    except Exception as e:
        logger.error(f"Detecting language error: {e}")
        raise


async def translate_text(text: str, dest_lang: str) -> str:
    logger.debug("Translating language...")
    translation_prompt = f"Переведи текст '{text}' с "

    if dest_lang == 'ru':
        translation_prompt += "русского на английский:"
    elif dest_lang == 'en':
        translation_prompt += "английского на русский:"
    else:
        return "Невозможно определить язык!"

    try:
        messages.append(HumanMessage(content=translation_prompt))
        result = giga.invoke(messages)
        messages.append(result)
        return result.content.strip()
    except Exception as e:
        logger.error(f"Translating language error: {e}")
        raise
