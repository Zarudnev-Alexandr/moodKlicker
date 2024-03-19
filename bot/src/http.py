import requests

from config_reader import config

url = config.url.get_secret_value()


def get_user(telegram_id: int):
    try:
        response = requests.get(f"{url}users/{telegram_id}")
        response.raise_for_status()  # Проверяем статус ответа

        # Если статус ответа 200 (OK), возвращаем данные ответа в формате JSON
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка при выполнении запроса: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None


def update_user_password(telegram_id, password):

    params = {
        "password": password
    }

    try:
        response = requests.put(f"{url}users/password/{telegram_id}", params=params)
        response.raise_for_status()  # Проверяем статус ответа

        # Если статус ответа 200 (OK), возвращаем новый пароль пользователя
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка при обновлении пароля: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None
