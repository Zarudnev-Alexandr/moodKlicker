import { useEffect } from 'react';
import { Button } from './components/Button/Button';
import { ClickerButton } from './components/ClickerButton/ClickerButton';
import './App.css';

const tg =window.Telegram.WebApp;

function App() {

  useEffect(() => {
    tg.ready();
  }, [])

  const onClose = () => {
    tg.close()
  }

  return (
    <div className="App">
      {/* <Button>Кнопка</Button> */}
      <div className="container">
        <div className="clicker__wrapper">
          <ClickerButton emoji='🤨'></ClickerButton>
        </div>
      </div>
    </div>
  );
}

export default App;
