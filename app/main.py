import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import settings

from app.middleware.tocken_check import TokenCheckMiddleware
from app.handlers import questions
from app.handlers.groups import router as groups_router

from config_logger import py_logger

logging.basicConfig(filename='bot_translater.log',
                    level=logging.INFO,
                    filemode="w",
                    format="%(asctime)s file - %(funcName)s, line - %(lineno)d %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


async def main():
    try:
        logger.info("Starting bot initialization...")

        logger.debug("Creating bot instance")
        bot = Bot(token=settings.BOT_TOKEN.get_secret_value())

        logger.debug("Configuring dispatcher")
        dp = Dispatcher()

        logger.debug("Adding middleware")
        dp.callback_query.outer_middleware(TokenCheckMiddleware)

        logger.info("Including routers")
        dp.include_router(questions.router)
        dp.include_router(groups_router)

        logger.info("Bot starting polling...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f"Bot crashed with error: {str(e)}", exc_info=True)
        raise
    finally:
        logger.info("Bot has been stopped")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        py_logger.error((f"Exception"), exc_info=True)