from aiogram.types import KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton


def inline_keyboards():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(text='Telegram', url='https://t.me/su_kiut'),
        InlineKeyboardButton(text='Instagram', url='https://instagram.com/kiut__su?igshid=YmMyMTA2M2Y=')
    )
    return markup
