import asyncio
import os
import time
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv
from keyboards import inline_keyboards

load_dotenv()

bot = Bot(os.getenv('TOKEN'), parse_mode='HTML')

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, f'''Привет! 😄
    
Вы можете оставить свою жалобу анонимно или отправить предложение здесь 💭

Спасибо, что поделились! 🤝🏼
----------------------------
Hello! 😄

You may leave your complaint anonymously or submit a proposal here 💭

Thanks for sharing! 🤝🏼''')


@dp.message_handler()
async def command_input(message: Message):
    print(type(message.chat.username))
    message_chat_id = message.chat.id
    group_id = '-1001949474863'
    if message.chat.username:
        await bot.send_message(group_id, f'{message.text}\n\nОтправил: @{message.chat.username}')
    if message.chat.username == 'None':
        await bot.send_message(group_id, f'{message.text}\n\nОтправил: Нету username')
    await asyncio.sleep(2)
    await bot.send_message(message_chat_id, '''Подписывайтесь на наши соц-сети\n\nSubscribe to our social networks''',
                           reply_markup=inline_keyboards())
    await asyncio.sleep(3)
    await bot.send_message(message_chat_id, '''Ваше сообшение было отпрвленно 🚀

Your message was sent 🚀''')


executor.start_polling(dp, skip_updates=True)
