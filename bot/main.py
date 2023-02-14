#пук пук
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

from pornhub_api import PornhubApi

def getporn(s: str) -> str:
    return('суперпорно с конями и ' + s)

API_TOKEN: str = '6177352917:AAFZSo4wP_R_Rmc-9jGcXoCXZLSHMQVxdRQ'

api = PornhubApi()

#объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Словарь, в котором будут храниться пользователи
users: dict = {}

#хэндлер на "/start" + добавление новых пользователей в словарь
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ бот для поиска порно')

    if message.from_user.id not in users:
        users[message.from_user.id] = {
                                        'wanna_nudes': False
                                        }

#хэнд на  "/help"
@dp.message(Command(commands=["help"]))
async def process_start_command(message: Message):
    await message.answer('текст который выводится при хелп')


#на "/sendnudes"
@dp.message(Command(commands=["sendnudes"]))
async def process_sendnudes_command(message: Message):
    users[message.from_user.id]['wanna_nudes'] = True
    await message.answer('напишите интересующий вас жанр')

#ваще всё кроме команд, работает потому что размещен после предыдущих хэндов
@dp.message()
async def send_echo(message: Message):
    if users[message.from_user.id]['wanna_nudes']:
        porn = getporn(message.text)
        await message.answer('вот ваше порно: ' + porn)
    else:
        await message.send_copy(chat_id=message.chat.id)



if __name__ == '__main__':
    dp.run_polling(bot)