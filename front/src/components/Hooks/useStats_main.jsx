import React, { createContext, useState, useRef, useEffect } from "react";

export const main_context = createContext();

export const MainProvider = ({ children }) => {
  const [bgList, setBgList] = useState([
    'radial-gradient(circle, rgba(255, 204, 204, 1) 0%, rgba(255, 255, 153, 1) 50%, rgba(204, 229, 255, 1) 100%)', // 😭
    'radial-gradient(circle, rgba(255, 224, 204, 1) 0%, rgba(255, 255, 153, 1) 50%, rgba(204, 255, 204, 1) 100%)', // 😢
    'radial-gradient(circle, rgba(255, 229, 204, 1) 0%, rgba(255, 255, 153, 1) 50%, rgba(204, 229, 255, 1) 100%)', // 😖
    'radial-gradient(circle, rgba(255, 204, 255, 1) 0%, rgba(204, 255, 255, 1) 50%, rgba(255, 255, 153, 1) 100%)', // 😞
    'radial-gradient(circle, rgba(204, 204, 255, 1) 0%, rgba(255, 204, 255, 1) 50%, rgba(255, 255, 153, 1) 100%)', // 😕
    'radial-gradient(circle, rgba(255, 204, 204, 1) 0%, rgba(255, 255, 153, 1) 50%, rgba(204, 255, 204, 1) 100%)', // 🙁
    'radial-gradient(circle, rgba(255, 255, 204, 1) 0%, rgba(204, 255, 255, 1) 50%, rgba(255, 204, 255, 1) 100%)', // 😐
    'radial-gradient(circle, rgba(204, 255, 204, 1) 0%, rgba(204, 204, 255, 1) 50%, rgba(255, 255, 153, 1) 100%)', // 😏
    'radial-gradient(circle, rgba(255, 204, 204, 1) 0%, rgba(255, 255, 153, 1) 50%, rgba(204, 229, 255, 1) 100%)', // 😉
    'radial-gradient(circle, rgba(255, 224, 204, 1) 0%, rgba(255, 255, 153, 1) 50%, rgba(204, 255, 204, 1) 100%)', // 😌
    'radial-gradient(circle, rgba(255, 229, 204, 1) 0%, rgba(255, 255, 153, 1) 50%, rgba(204, 229, 255, 1) 100%)', // 😎
    'radial-gradient(circle, rgba(255, 204, 255, 1) 0%, rgba(204, 255, 255, 1) 50%, rgba(255, 255, 153, 1) 100%)', // 🥰
    'radial-gradient(circle, rgba(204, 204, 255, 1) 0%, rgba(255, 204, 255, 1) 50%, rgba(255, 255, 153, 1) 100%)', // 🤩
  ]);


  const [currentBg, setCurrentBg] = useState(0);
  let [curentNumberOfClicks, setCurentNumberOfClicks] = useState(0);


  useEffect(() => {
    document.body.style.background = bgList[currentBg];
  }, [currentBg, bgList]);


  return (
    <main_context.Provider
      value={{
        bgList,
        curentNumberOfClicks,
        setCurrentBg,
        setCurentNumberOfClicks
      }}
    >
      {children}
    </main_context.Provider>
  );
};