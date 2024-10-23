import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html
from app.handlers import router
from config import *
from sqlalchemy.orm import Session


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен!")

