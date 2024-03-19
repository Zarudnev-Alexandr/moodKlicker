import { API_URL } from '../globalSettings/apiUrl';
import axios from 'axios';

export const getShop = async (setter) => {
  try {
    const response = await axios.get(`${API_URL}shop`, {
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

export const buyItem = async (telegram_id, item_id) => {
  const response = await fetch(`${API_URL}shop/${telegram_id}/buy/${item_id}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
  });

  let data = await response.json();
  return ({ data: data, status: response.status });
};