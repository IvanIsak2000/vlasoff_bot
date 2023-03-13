
import logging
import time
import datetime
import os
import sys

try:

    from aiogram import Bot, Dispatcher, executor, types
    print('бот работает!')

except:

    os.system('pip install aiogram')
    os.system('cls')
    print('aiogram установлен!')
    print('бот работает!')
    from aiogram import Bot, Dispatcher, executor, types

try:
    from config import API_TOKEN as API_TOKEN
except:
    print('токен не найден!!')
    _exit = input('нажмите любую клавишу для выхода!')
    exit()

logging.basicConfig(
    level=logging.INFO,
    filename="vlasoff_journal.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s")


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

commands = '\nКоманды:\n/id\n/help\n/admin\n/group\n/about'
community = 'https://vk.com/thecommonwealth2020'
repo = 'https://github.com/IvanIsak2000/vlasoff_bot'
admin = 'https://vk.com/a.vlasov04'


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f'Вечер в хату, господа, я Vlasoff bot.\nЯ буду следить за чатом.{commands}')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply(f'Здарова фраер {str(message.from_user.username)}{commands}')


@dp.message_handler(commands=['id'])
async def id(message: types.Message):
    chat_id = message.chat.id
    await message.reply(f'Слышь фраерок, id этого чата: {chat_id}')


@dp.message_handler(commands=['group'])
async def id(message: types.Message):
    await message.reply(f'Сообщество: {community}')


@dp.message_handler(commands=['about'])
async def id(message: types.Message):
    await message.reply(f'Репа: {repo}')


@dp.message_handler(commands=['admin'])
async def id(message: types.Message):
    await message.reply(f'Председатель движения: {admin}')

    logging.info(
        f'{message} {message.from_user.id} {message.from_user.first_name} {message.from_user.last_name} {message.from_user.username}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
