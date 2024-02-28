from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards import confirm_debtor_fullname_kb

router = Router(name="commands-router")


@router.message(CommandStart())
async def cmd_start(message: Message):
        await message.answer(text=f"Перейти на сайт", reply_markup=confirm_debtor_fullname_kb())
