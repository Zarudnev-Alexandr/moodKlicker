import { useEffect, useState } from 'react';
import { ClickerButton } from './components/ClickerButton/ClickerButton';
import { MainProvider } from './components/Hooks/useStats_main';
import './App.css';
import { useTelegram } from './components/Hooks/useTelegram';
import { useInterface } from './components/Hooks/useInteface';
import { getCurrentNumberOfClicks, getUser, loginUser } from './http/User';
import { WarningMessage } from './components/WarningMessage/WarningMessage';
import { PaintClicks } from './components/PaintClicks/PaintClicks';
import { Button } from './components/Button/Button';
import { Shop } from './components/Shop/Shop';


function App() {


  const { tg, telegram_id, setIsUserLogin, isUserLogin } = useTelegram();
  const { currentPage, setCurrentPage } = useInterface()

  useEffect(() => {
    tg.ready();
    telegram_id &&
      loginUser(telegram_id, setIsUserLogin)

  }, [telegram_id])


  return (
    <MainProvider>
      {isUserLogin ?
        <>
          {currentPage === 'main' ? (
            <div className="App">
              <div className="container">
                <div className="clicker__wrapper">
                  <PaintClicks />
                  <ClickerButton emoji='🤨'></ClickerButton>
                  <div className="bottom">
                    <Button className='bottom__btn' name='Магазин' page='shop' setCurrentPage={setCurrentPage} currentPage={currentPage} />
                  </div>
                </div>
              </div>
            </div>
          ) : <></>}
          {currentPage === 'shop' ? (
            <>
              <Shop />
              {/* <div className="clicker__wrapper"> */}
              <div className="bottom bottom__shop">
                <Button className='bottom__btn' name='Продолжить кликать' page='main' setCurrentPage={setCurrentPage} currentPage={currentPage} />
              </div>
              {/* </div> */}
            </>
          ) : <></>}
        </>
        : <WarningMessage />}

    </MainProvider>
  );
}

export default App;
