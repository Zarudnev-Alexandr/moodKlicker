from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.commands import UserAddPassword
from src.http import update_user_password
from src.keyboards import main_kb

router = Router(name="callbacks-router")


@router.callback_query(F.data.startswith("password_confirm"))
async def callback_debtor_add(callback: CallbackQuery, state: FSMContext,):

    telegram_id = callback.from_user.id
    state_data = await state.get_data()
    password = state_data['password']
    new_password = update_user_password(telegram_id=telegram_id, password=password,)

    if new_password:
        await callback.message.answer("Пароль успешно установлен🔥")
        await callback.message.delete()
        await state.clear()
    else:
        await callback.message.answer("Ошибка❌", reply_markup=main_kb())


@router.callback_query(F.data.startswith("password_rewrite"))
async def callback_debtor_rewrite(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Давай перепишем. Введи пароль: ")
    await state.set_state(UserAddPassword.waiting_for_password)
    await callback.message.delete()
