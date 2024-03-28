from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from src.http import get_user
from src.keyboards import main_kb, site_kb

router = Router(name="commands-router")


class UserAddPassword(StatesGroup):
    waiting_for_password = State()
    waiting_for_confirm_password = State()


@router.message(Command(commands=["cancel"]))
@router.message(F.text.lower() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.delete()
    await message.answer(
        text="Ввод отменен",
    )


@router.message(CommandStart())
async def cmd_start(message: Message):
    # await message.answer(text=f"Перейти на сайт", reply_markup=confirm_debtor_fullname_kb())
    await message.answer(text=f'Привет, {message.from_user.full_name}! \nНажав на кнопку "Начать кликать", '
                              f'ты зайдешь в игру.\n'
                              f'Чтобы вывести заработанные клики на наш сервер в дискорде, '
                              f'нажми на соответствующую кнопку на клавиатуре снизу↘',
                         reply_markup=main_kb())


@router.message(F.text.lower() == "подключить дискорд🔗")
async def discord(message: Message, state: FSMContext):
    telegram_id = message.from_user.id

    user = get_user(telegram_id)

    if user is None:
        await message.answer("Ты еще даже не поиграл, а уже хочешь что-то вывести. Давай покликаем сначала")
        await state.clear()
        return

    await message.answer(f"Твой telegram id: <code>{telegram_id}</code>, используешь  это потом в дискорде. \n"
                         f"Напиши пароль для дискорда: ")
    await state.set_state(UserAddPassword.waiting_for_password)


@router.message(F.text.lower() == "начать кликать👆")
async def start_game_func(message: Message):
    await message.answer("Давай покликаем😍", reply_markup=site_kb())
