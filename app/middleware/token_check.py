from aiogram import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from aiogram.types import Message, TelegramObject

from app.services.is_access_tocken import check_access_token
from app.services.get_acces_token import get_token

from app.config_logger import setup_logger

logger = setup_logger(__name__)


class TokenCheckMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        logger.info("Checking token...")

        try:
            if check_access_token() is False:
                get_token()
            return await handler(event, data)
        except Exception as e:
            logger.error(f"Token check failed: {str(e)}", exc_info=True)
            raise
