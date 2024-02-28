import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from bot import commands
from bot.keyboards import confirm_debtor_fullname_kb
from config_reader import config
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


async def main():
    bot = Bot(config.bot_token.get_secret_value())

    dp = Dispatcher()
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    dp.include_router(commands.router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
