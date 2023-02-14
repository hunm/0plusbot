#пук пук
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

from porn_api import getporn_from_request, getporn_from_category

API_TOKEN: str = '6177352917:AAFZSo4wP_R_Rmc-9jGcXoCXZLSHMQVxdRQ'

#объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Словарь, в котором будут храниться пользователи
users: dict = {}

#хэндлер на "/start" + добавление новых пользователей в словарь
#из минусов - слетает после каждого запуска, надо заново писать старт
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ бот для поиска порно')

    if message.from_user.id not in users:
        #по умолчанию ставит хочет_порно в фолс для всех
        users[message.from_user.id] = {
                                        'wanna_porn': False
                                        }

#хэнд на  "/help"
@dp.message(Command(commands=["help"]))
async def process_start_command(message: Message):
    await message.answer('текст который выводится при хелп')


#на "/sendnudes", ставит хочет_порно в тру
@dp.message(Command(commands=["sendnudes"]))
async def process_sendnudes_command(message: Message):
    users[message.from_user.id]['wanna_porn'] = True
    await message.answer('напишите интересующий вас жанр')


#если чел хочет порно, кидает порно + ставит статус хочет_порно в фолс, если не хочет, кидает ему его же сообщ
@dp.message()
async def send_echo(message: Message):
    if users[message.from_user.id]['wanna_nudes']:
        porn = getporn_from_request(message.text)
        await message.answer('вот ваше порно: ' + porn)
        users[message.from_user.id]['wanna_porn'] = False
    else:
        await message.send_copy(chat_id=message.chat.id)



if __name__ == '__main__':
    dp.run_polling(bot)
