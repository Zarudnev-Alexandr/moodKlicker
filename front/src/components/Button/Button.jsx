import './Button.scss'
export const Button = (props) => {

  return (
    <button {...props} className={'button ' + props.className}></button>
  )
}