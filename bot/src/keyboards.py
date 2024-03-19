from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup


def site_kb():
    kb = [
        [
            InlineKeyboardButton(text="Начать кликать👆", web_app=WebAppInfo(url='https://9806-109-61-223-205.ngrok-free.app')),
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def main_kb():
    kb = [
        [
            KeyboardButton(text="Начать кликать👆"),
            KeyboardButton(text="Подключить дискорд🔗"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def confirm_user_password_kb():
    kb = [
        [
            InlineKeyboardButton(text="Подтвердить", callback_data="password_confirm"),
            InlineKeyboardButton(text="Заново", callback_data="password_rewrite")
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard
