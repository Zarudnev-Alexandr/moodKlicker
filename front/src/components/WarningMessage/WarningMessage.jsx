import React from 'react';
import './WarningMessage.scss';

export const WarningMessage = () => {
  return (
    <div className="warning-container">
      <div className="telegram-logo">
        <img src="https://telegram.org/img/t_logo.png"></img>
      </div>
      <p className="warning-text">
        Пожалуйста, войдите только через Telegram для корректной работы.
      </p>
      <p className="bot-link">
        <strong>Ссылка на бота:</strong> <a href="https://t.me/moodClickerBot">https://t.me/moodClickerBot</a>
      </p>
      <div className="qr-code">
        <img src="http://qrcoder.ru/code/?https%3A%2F%2Ft.me%2FmoodClickerBot&4&0"></img>
      </div>
    </div>
  );
};