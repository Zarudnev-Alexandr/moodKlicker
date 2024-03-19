import { useEffect, useState } from 'react'
import './Shop.scss'
import { ShopItem } from './ShopItem/ShopItem'
import { getShop } from '../../http/Shop'
import { useTelegram } from '../Hooks/useTelegram'
import { getUserInfo } from '../../http/User'
import Modal from '../Modal/Modal'

export let Shop = ({ props }) => {

  const { telegram_id, } = useTelegram();

  let [shop, setShop] = useState([])
  let [user, setUser] = useState({})
  let [titleModal, setTitleModal] = useState('')
  let [textModal, setTextModal] = useState('')
  let [emojiModal, setEmojiModal] = useState('')

  const [isOpen, setIsOpen] = useState(false);

  const openModal = () => {
    setIsOpen(true);
  };

  const closeModal = () => {
    setIsOpen(false);
  };

  useEffect(() => {
    getShop(setShop)
    getUserInfo(telegram_id, setUser)
  }, [telegram_id])

  let updateShop = () => {
    getShop(setShop)
    getUserInfo(telegram_id, setUser)
  }

  return (
    <div className='shop'>
      {shop?.map(item =>
        <ShopItem shop={item}
          user={user}
          openModal={openModal}
          closeModal={closeModal} 
          setTitleModal={setTitleModal}
          setTextModal={setTextModal}
          setEmojiModal={setEmojiModal}
          updateShop={updateShop}
          />)}
      <Modal
        isOpen={isOpen}
        onClose={closeModal}
        title={titleModal}
        text={textModal}
        emoji={emojiModal}
      />
    </div>
  )
}