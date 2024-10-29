import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html
from app.handlers import router
from config import *
from sqlalchemy.orm import Session

from config import Config

config = Config()

async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(token=config.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен!")

