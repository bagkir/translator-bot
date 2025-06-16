from aiogram import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from aiogram.types import Message, TelegramObject

from app.services.is_access_tocken import check_access_token
from app.services.get_acces_token import get_token

from app.config_logger import py_logger


class TokenCheckMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        py_logger.debug(f"Processing: {event.chat}, {event.date}")

        if check_access_token() is False:
            get_token()

        py_logger.info(f"access token verified successful")

        try:
            return await handler(event, data)
        except Exception as e:
            py_logger.error(f"Middleware error: {e}")
