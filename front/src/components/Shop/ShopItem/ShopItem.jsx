import { buyItem } from '../../../http/Shop'
import './ShopItem.scss'
import Modal from '../../Modal/Modal'

export const ShopItem = ({ shop, user, openModal, closeModal, setTitleModal, setTextModal, setEmojiModal, updateShop }) => {

  let isItemBought = () => {
    if (user?.bought?.find(user_item => shop.id === user_item.item_id)) {
      return true
    } else {
      return false
    }
  }

  let handleBuyItem = async () => {
    let boughtItem = await buyItem(user?.telegram_id, shop.id)
    if (boughtItem?.status === 405) {
      setTitleModal('Невозможно купить предмет')
      setTextModal('У тебя уже куплен этот предмет')
      setEmojiModal('🤷‍♂️')
      openModal()
    }
    if (boughtItem?.status === 403) {
      setTitleModal('Невозможно купить предмет')
      setTextModal('У тебя не хватает кликов на покупку')
      setEmojiModal('💸')
      openModal()
    }
    if (boughtItem?.status === 200) {
      setTitleModal('Предмет куплен');
      setTextModal('Вообще все с кайфом');
      setEmojiModal('🥳');
      openModal();
      updateShop();
    }
  }

  return (
    <div className={`shopItem ${isItemBought() ? 'shopItem--bought' : ''}`}>
      <div className="shopItem__inner"
        onClick={() => { if (!isItemBought()) { handleBuyItem() } }}
      >
        <h4 className="shopItem__title">{shop.name}</h4>
        <ul className='shopItem__list'>
          {shop?.boost?.map((item, index) =>
            <li className='shopItem__list-item'>
              {(item?.boost !== 0) &&
                <div>Boost: +{item?.boost}</div>
              }
              {(item?.x_boost !== 1) &&
                <div>Boost: x{item?.x_boost}</div>
              }
            </li>
          )}
        </ul>
        <p className="shopItem__price">Цена: {shop.price}</p>
      </div>
    </div>
  )
}