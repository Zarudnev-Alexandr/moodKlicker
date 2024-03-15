import React, { useState, useEffect, useContext } from 'react';
import './ClickerButton.scss';
import { main_context } from '../Hooks/useStats_main';
import { useTelegram } from '../Hooks/useTelegram';
import { getUserInfo, putIncrementClick } from '../../http/User';

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

const getRandomTransform = () => {
  const amountX = Math.random() * 12 + 1; // Генерируем случайное число для определения величины движения
  const amountY = Math.random() * 12 + 1; 
  const rotate = (Math.random() * 12) - 6;
  return `translate(${amountX}px, ${amountY}px) rotate(${rotate}deg)`;
};

const getDirection = () => {
  const randomX = Math.floor(Math.random() * 101) - 50; // Генерируем случайное число в диапазоне от -100 до 100
  return randomX;
};


export const ClickerButton = (props) => {

  const { telegram_id } = useTelegram()

  let {setCurrentBg, bgList, setCurentNumberOfClicks } = useContext(main_context);

  const [clicks, setClicks] = useState([]);
  const [emojiIndex, setEmojiIndex] = useState(0); // Индекс текущего эмодзи
  const [continuousClicks, setContinuousClicks] = useState(0); // Количество непрерывных кликов
  const emojis = ['😭', '😢', '😖', '😞', '😕', '🙁', '😐', '😏', '😉', '😌', '😎', '🥰', '🤩']; // Массив доступных эмодзи
  const clicksLimit = 10; // Лимит кликов
  const timeoutDelay = 5000; // Задержка для таймаута (в миллисекундах)
  const [userInfo, setUserInfo] = useState({});
  const [currentBoost, setCurrentBoost] = useState(1)

  const handleClick = (event) => {
    const button = event.currentTarget.querySelector('.ClickerButton-button');
    let direction = getDirection();
    let directionClass = direction < 0 ? 'click-left' : 'click-right';

    setTimeout(() => {
      const randomTransform = getRandomTransform();
      button.style.transform = randomTransform;
      void button.offsetWidth;
    }, 100); // Выполняем через 0.1 секунды

    const boundingRect = event.currentTarget.getBoundingClientRect();
    const newClick = {
      id: getRandomInt(999999999),
      x: event.clientX - boundingRect.left,
      y: event.clientY - boundingRect.top,
      opacity: 1,
      clickColor: `rgb(${getRandomInt(255)}, ${getRandomInt(255)}, ${getRandomInt(255)})`,
      direction: directionClass,
      
    };
    setClicks((state) => [...state, newClick]);
    setContinuousClicks(prevClicks => prevClicks + 1);
    putIncrementClick(telegram_id, setCurentNumberOfClicks);
    setTimeout(() => {
      setClicks(prevClicks => prevClicks.filter((click) => click.id !== newClick.id));
    }, 1000);
  };

  useEffect(() => {
    const timeoutId = setTimeout(() => {
      setContinuousClicks(prevClicks => Math.max(0, prevClicks - clicksLimit));
      if (emojiIndex !== 0) {
        setEmojiIndex(prevIndex => (prevIndex - 1) % emojis.length);
        setCurrentBg(prevIndex => (prevIndex - 1) % emojis.length);
      }
    }, timeoutDelay);

    return () => {
      clearTimeout(timeoutId);
    };
  }, [continuousClicks, emojiIndex]);


  //Возвращаем челика в начальное положение
  useEffect(() => {
    const timeoutId = setTimeout(() => {
      const button = document.querySelector('.ClickerButton-button');
      if (button) {
        button.style.transform = 'translate(0px, 0px) rotate(0deg)';
      }
    }, 1500);

    return () => clearTimeout(timeoutId); // отменяем timeout при размонтировании компонента
  }, [continuousClicks]);

  useEffect(() => {
    getUserInfo(telegram_id, setUserInfo)
  }, [])

  useEffect(() => {
    let user_boost = 0
    let user_xboost = 1
    userInfo?.bought?.map((bought_item) => {
      bought_item?.items?.boost?.map((boost_item) => {
        user_boost += boost_item.boost
        user_xboost *= boost_item.x_boost
      })
    })
    setCurrentBoost((1 + user_boost) * user_xboost)
  }, [userInfo])


  useEffect(() => {
    if (continuousClicks >= clicksLimit) {
      if (emojiIndex != emojis.length - 1) {
        setEmojiIndex(prevIndex => (prevIndex + 1) % emojis.length);
        setCurrentBg(prevIndex => (prevIndex + 1) % emojis.length);
      }

      setContinuousClicks(0);
    }
  }, [continuousClicks]);

  return (
    <div className="ClickerButton-container" onClick={handleClick}>
      <button className="ClickerButton-button">
        {emojis[emojiIndex]}
      </button>
      {clicks.map((click, index) => (
        <span
          key={click.id}
          className={`ClickerButton-click ${click.direction}`}
          style={{
            '--clickY': `${click.y}px`,
            top: click.y,
            left: click.x,
            opacity: click.opacity,
            color: click.clickColor
          }}
        >
          {currentBoost}
        </span>
      ))}
    </div>
  );
};
