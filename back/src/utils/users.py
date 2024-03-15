from datetime import datetime
from typing import Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src import User


async def get_user(session: AsyncSession, telegram_id: int) -> Type[User] | None:
    user = await session.get(User, telegram_id)
    return user


async def create_user(session: AsyncSession, telegram_id: int) -> User:
    user = User(telegram_id=telegram_id)
    session.add(user)
    await session.commit()
    return user


async def increment_clicks(session: AsyncSession, user):
    user_boost = 0
    user_xboost = 1
    for bought_item in user.bought:  # Итерируемся по списку купленных предметов
        for boost_item in bought_item.items.boost:  # Итерируемся по списку усилений для каждого купленного предмета
            user_boost += boost_item.boost
            user_xboost *= boost_item.x_boost

    user.number_of_clicks += ((1 + user_boost) * user_xboost)
    user.time_of_last_click = datetime.now()

    await session.commit()
    return user.number_of_clicks
