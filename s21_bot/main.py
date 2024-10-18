import asyncio
import logging
import signal
import sys

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs

from s21_bot import main_router
from s21_bot.config import bot_token


def signal_handler(sig, frame):
    """обработчик остановки бота для удобства."""
    logging.info("Bot has stoped!")
    sys.exit(0)


async def main():
    """запуск поллинга для бота."""
    # подключаем обработчик сигнала завершения бота
    signal.signal(signal.SIGINT, signal_handler)

    # подключаем логгирование
    logging.basicConfig(level=logging.INFO)

    # получаем токен и создаем объект бота
    bot = Bot(token=bot_token[:46])

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(main_router)

    setup_dialogs(dp)

    # удаляем вебхуки и запускаем бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
