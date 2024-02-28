from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


def confirm_debtor_fullname_kb():
    kb = [
        [
            InlineKeyboardButton(text="Сайт", web_app=WebAppInfo(url='https://ya.ru')),
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard