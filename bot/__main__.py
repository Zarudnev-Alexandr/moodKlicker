import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from src import commands, state, callbacks
from config_reader import config
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode='HTML')

    dp = Dispatcher()
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    dp.include_router(commands.router)
    dp.include_router(state.router)
    dp.include_router(callbacks.router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
