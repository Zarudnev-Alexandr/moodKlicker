import { useContext, useEffect } from 'react';
import { useTelegram } from '../Hooks/useTelegram'
import './PaintClicks.scss'
import { main_context } from '../Hooks/useStats_main';
import { getCurrentNumberOfClicks } from '../../http/User';
import { useInterface } from '../Hooks/useInteface';

export const PaintClicks = () => {

  const { isUserLogin, telegram_id } = useTelegram()
  let { currentPage } = useInterface()
  let { curentNumberOfClicks, setCurentNumberOfClicks } = useContext(main_context);

  useEffect(() => {
    getCurrentNumberOfClicks(telegram_id, setCurentNumberOfClicks)
  }, [isUserLogin, currentPage])


  return (
    <div className="paintClicks">
      <h1>{curentNumberOfClicks}</h1>
    </div>
  )
}