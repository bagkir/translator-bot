import asyncio
from aiogram import Bot, Dispatcher

from config import settings

from app.middleware.token_check import TokenCheckMiddleware
from app.handlers import questions
from app.handlers.groups import router as groups_router

from config_logger import setup_logger

root_logger = setup_logger('app')

async def main():
    try:
        root_logger.info("Starting bot initialization...")

        root_logger.debug("Creating bot instance")
        bot = Bot(token=settings.BOT_TOKEN.get_secret_value())

        root_logger.debug("Configuring dispatcher")
        dp = Dispatcher()

        root_logger.debug("Adding middleware")
        dp.callback_query.outer_middleware(TokenCheckMiddleware)

        root_logger.info("Including routers")
        dp.include_router(questions.router)
        dp.include_router(groups_router)

        root_logger.info("Bot starting polling...")
        await dp.start_polling(bot)
    except Exception as e:
        root_logger.critical(f"Bot crashed with error: {str(e)}", exc_info=True)
        raise
    finally:
        root_logger.info("Bot has been stopped")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        root_logger.error((f"Exception"), exc_info=True)