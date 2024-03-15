import './Button.scss'

export const Button = ({ page, setCurrentPage, className, name, currentPage, ...otherProps }) => {
  const handleClick = () => {

    // console.log('Click event:', page); // Отладочный вывод для проверки
    // console.log('currentPage', currentPage); // Отладочный вывод для проверки
    // if (page && setCurrentPage && currentPage !== page) {
      setCurrentPage(page);
    // }
  };

  return (
    <button {...otherProps} className={`button ${className}`} onClick={handleClick}>
      <svg className="button__shape" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
        <path className="button__path" d="M0,0 C0,0 100,0 100,0 C100,0 100,100 100,100 C100,100 0,100 0,100 C0,100 0,0 0,0 z" />
      </svg>
      <span className="button__content">
        {name}
      </span>
    </button>
  );
};