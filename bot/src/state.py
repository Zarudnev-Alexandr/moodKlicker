from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.commands import UserAddPassword
from src.keyboards import confirm_user_password_kb

router = Router(name="state-router")


@router.message(UserAddPassword.waiting_for_password, F.text)
async def user_add_state_wating_for_password(message: Message, state: FSMContext,):
    password = message.text.strip()

    if not password:
        await message.answer("Пожалуйста, укажи корректный пароль. Пустой ввод не допускается.")
        return

    if len(password) > 30:
        await message.answer(
            "Длина введенного пароля слишком большая. Максимум 30 символов.")
        return

    if len(password) < 5:
        await message.answer(
            "Длина введенного пароля слишком маленькая. Минимум 5 символов.")
        return

    await state.update_data(password=password)
    await message.answer(text=f"Введено: {password}. Все правильно?", reply_markup=confirm_user_password_kb())
    await message.delete()
