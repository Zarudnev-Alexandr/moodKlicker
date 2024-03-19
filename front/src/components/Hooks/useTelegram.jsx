import { useState } from "react";

const tg = window.Telegram.WebApp;

export function useTelegram() {

  let [isUserLogin, setIsUserLogin] = useState(false);
  

  const onToggleButton = () => {
    if (tg.MainButton.isVisible) {
      tg.MainButton.hide()
    }else{
      tg.MainButton.show()
    }
  }


  return{
    tg, 
    telegram_id: tg.initDataUnsafe?.user?.id,
    // telegram_id: 1,
    onToggleButton,
    isUserLogin,
    setIsUserLogin,
  }
}