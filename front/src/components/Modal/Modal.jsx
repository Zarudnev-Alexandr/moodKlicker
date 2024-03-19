import React, { useState } from 'react';
import './Modal.scss';

const Modal = ({ isOpen, onClose, title, text, emoji }) => {
  if (!isOpen) {
    return null;
  }

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal">
        <div className="modal-header">
          <h2>{title}</h2>
          {/* <button className="close-button" onClick={onClose}>×</button> */}
        </div>
        <div className="modal-content">
          <p>{text}</p>
          {emoji && <span role="img" aria-label="Emoji">{emoji}</span>}
        </div>
      </div>
    </div>
  );
};

export default Modal;