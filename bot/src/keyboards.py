from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


def confirm_debtor_fullname_kb():
    kb = [
        [
            InlineKeyboardButton(text="Сайт", web_app=WebAppInfo(url='https://6632-194-87-199-70.ngrok-free.app')),
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard