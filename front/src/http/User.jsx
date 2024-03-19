import { API_URL } from '../globalSettings/apiUrl';
import axios from 'axios';


export const getUser = async (telegram_id, setter) => {
  try {
    const response = await axios.get(`${API_URL}users/${telegram_id}`, {
      headers: {
        'Content-Type': 'application/json',
        'ngrok-skip-browser-warning': 'true'
      },
    });

    if (response.status === 200) {
      setter(true);
    } else if (response.status === 404) {
      setter(false);
      await loginUser(telegram_id, setter);
    } else {
      throw new Error(`Unexpected status code: ${response.status}`);
    }
  } catch (error) {
    console.error(error);
    setter(false);
  }
};


export const loginUser = async (telegram_id, setter) => {
  try {
    const response = await fetch(`${API_URL}users/login?telegram_id=${telegram_id}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
    });

    if (response.status === 200) {
      setter(true);
    } else if (response.status === 400) {
      setter(false);
    } else {
      throw new Error(`Unexpected status code: ${response.status}`);
    }
  } catch (error) {
    console.error(error);
    setter(false);
  }
};

export const getUserInfo = async (telegram_id, setter) => {
  try {
    const response = await axios.get(`${API_URL}users/${telegram_id}`, {
      headers: {
        'Content-Type': 'application/json',
        'ngrok-skip-browser-warning': 'true'
      },
    });

    if (response.status === 200) {
      setter(response.data);
    } else {
      throw new Error(`Unexpected status code: ${response.status}`);
    }
  } catch (error) {
    console.error(error);
    setter([]);
  }
};


export const putIncrementClick = async (telegram_id, setCurentNumberOfClicks) => {
  let response = await fetch(`${API_URL}users/increment_clicks/${telegram_id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
  });

  let data = await response.json()
  setCurentNumberOfClicks(data);

}


export const getCurrentNumberOfClicks = async (telegram_id, setter) => {
  try {
    const response = await axios.get(`${API_URL}users/${telegram_id}/number_of_clicks`, {
      headers: {
        'Content-Type': 'application/json',
        'ngrok-skip-browser-warning': 'true'
      },
    });

    const data = response.data;

    if (response.status === 200) {
      setter(data);
    } else {
      setter(0);
    }
  } catch (error) {
    console.error(error);
    setter(0);
  }
};