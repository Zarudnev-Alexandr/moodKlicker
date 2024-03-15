from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src import Item, Boost, User, Bought


async def get_shop(session: AsyncSession) -> list[Item]:
    result = await session.execute(select(Item))
    return result.unique().scalars().all()


async def get_item(session: AsyncSession, id):
    item = await session.get(Item, id)
    return item


async def add_item_to_shop(session: AsyncSession, item_name: str, price: int, boost_value: int, x_boost_value: int):

    new_item = Item(name=item_name, price=price)
    session.add(new_item)
    await session.flush()  # Flush, чтобы получить id нового предмета

    # Создаем соответствующий ему буст
    new_boost = Boost(boost=boost_value, x_boost=x_boost_value, item_id=new_item.id)
    session.add(new_boost)
    await session.commit()  # Фиксируем изменения

    if new_item and new_boost:
        return [new_item, new_boost]


async def add_boost_to_item(session: AsyncSession, item_id: int, boost_value: int, x_boost_value: int):

    new_boost = Boost(boost=boost_value, x_boost=x_boost_value, item_id=item_id)
    session.add(new_boost)
    await session.commit()

    if new_boost:
        return new_boost


async def buy_item(session: AsyncSession, user, item):
    new_bought = Bought(user_id=user.telegram_id, item_id=item.id)
    session.add(new_bought)
    await session.commit()

    if new_bought:
        user.number_of_clicks = user.number_of_clicks - item.price
        await session.commit()
        await session.flush()
        return [user]
