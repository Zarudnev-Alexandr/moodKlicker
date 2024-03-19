from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.db import get_session
from src.utils import get_user, create_user, increment_clicks
from src.utils.users import add_password, get_user_for_password

users_router = APIRouter()


@users_router.get("/{telegram_id}")
async def get_user_route(telegram_id: int, session: AsyncSession = Depends(get_session)):
    user = await get_user(session=session, telegram_id=telegram_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="Такого пользователя не существует")


@users_router.post("/login")
async def login_user_route(telegram_id: int, session: AsyncSession = Depends(get_session)):
    user = await get_user(session=session, telegram_id=telegram_id)
    if user:
        return JSONResponse(
            content={"message": "Пользователь уже зарегистрирован", "status_code": 200},
            status_code=200
        )
    else:
        new_user = await create_user(session=session, telegram_id=telegram_id)
        if new_user:
            return new_user
        else:
            raise HTTPException(status_code=400, detail="Не удалось создать пользователя")


@users_router.put("/increment_clicks/{telegram_id}")
async def increment_clicks_route(telegram_id: int, session: AsyncSession = Depends(get_session)):
    user = await get_user(session=session, telegram_id=telegram_id)

    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    new_count_clicks = await increment_clicks(session=session, user=user, )
    return new_count_clicks


@users_router.get("/{telegram_id}/number_of_clicks")
async def get_current_number_of_clicks(telegram_id: int, session: AsyncSession = Depends(get_session)):
    user = await get_user(session=session, telegram_id=telegram_id)
    if user:
        return user.number_of_clicks
    else:
        raise HTTPException(status_code=404, detail="Такого пользователя не существует")


@users_router.put("/password/{telegram_id}")
async def password_func(telegram_id: int, password: str, session: AsyncSession = Depends(get_session)):
    user = await get_user(session=session, telegram_id=telegram_id)

    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    if len(str(password)) < 5:
        raise HTTPException(status_code=401, detail="Слишком короткий пароль")

    if len(str(password)) > 30:
        raise HTTPException(status_code=402, detail="Слишком длинный пароль")

    new_password = await add_password(session=session, user=user, password=password, )
    return new_password


@users_router.put("/{telegram_id}/discord/{password}")
async def get_user_for_password_func(telegram_id: int, password: str, session: AsyncSession = Depends(get_session)):
    user = await get_user_for_password(session=session, telegram_id=telegram_id, password=password)
    if user:
        # Вычисляем количество кликов для конвертации
        convert_clicks = user.number_of_clicks // 10000
        written_off_clicks = convert_clicks * 10000
        remaining_clicks = user.number_of_clicks - written_off_clicks

        # Обновляем данные пользователя в базе данных
        user.number_of_clicks -= written_off_clicks
        await session.commit()

        # Возвращаем результат в формате JSON
        return {
            "number_of_clicks": user.number_of_clicks + written_off_clicks,
            "written_off_clicks": written_off_clicks,
            "remaining_clicks": remaining_clicks,
            "convert_clicks": convert_clicks
        }
    else:
        raise HTTPException(status_code=404, detail="Неверный telegram id или пароль")