from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src import get_session, get_user
from src.utils.shop import get_shop, add_item_to_shop, add_boost_to_item, buy_item, get_item

shop_router = APIRouter()


@shop_router.get("")
async def get_shop_func(session: AsyncSession = Depends(get_session)):
    shop = await get_shop(session=session)

    if shop:
        return shop
    else:
        raise HTTPException(status_code=404, detail="Магазин пуст")


@shop_router.post("/add_item")
async def add_item_to_shop_func(item_name: str,
                                price: int,
                                boost_value: int,
                                x_boost_value: int,
                                session: AsyncSession = Depends(get_session)):
    new_item = await add_item_to_shop(session=session,
                                      item_name=item_name,
                                      price=price,
                                      boost_value=boost_value,
                                      x_boost_value=x_boost_value)
    if new_item:
        return new_item
    else:
        raise HTTPException(status_code=400, detail="Не удалось создать предмет в магазине")


@shop_router.post("/{item_id}/add_boost")
async def add_boost_to_item_func(item_id: int,
                                 boost_value: int,
                                 x_boost_value: int,
                                 session: AsyncSession = Depends(get_session)):
    new_boost = await add_boost_to_item(session=session,
                                        item_id=item_id,
                                        boost_value=boost_value,
                                        x_boost_value=x_boost_value, )

    if new_boost:
        return new_boost
    else:
        raise HTTPException(status_code=400, detail="Не удалось добавить буст в предмет")


@shop_router.post("/{telegram_id}/buy/{item_id}")
async def buy_item_func(telegram_id: int,
                        item_id: int,
                        session: AsyncSession = Depends(get_session)):

    user = await get_user(session=session, telegram_id=telegram_id)
    item = await get_item(session=session, id=item_id)

    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    if not item:
        raise HTTPException(status_code=404, detail="Предмет в магазине не найден")

    if item.id in (bought_item.item_id for bought_item in user.bought):
        raise HTTPException(status_code=405, detail="У вас уже куплен этот предмет")

    if user.number_of_clicks < item.price:
        raise HTTPException(status_code=403, detail="У вас не хватает кликов на покупку")

    new_bought = await buy_item(session, user, item)

    if new_bought:
        return new_bought
    else:
        raise HTTPException(status_code=400, detail="Не удалось купить предмет")

