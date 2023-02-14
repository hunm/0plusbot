#пук пук
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from pornhub_api import PornhubApi


API_TOKEN: str = '6177352917:AAFZSo4wP_R_Rmc-9jGcXoCXZLSHMQVxdRQ'

api = PornhubApi()

#объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


#хэнд на "/start" и "/help"
@dp.message(Command(commands=["start", "help"]))
async def process_start_command(message: Message):
    await message.answer('текст который выводится при старт и хелп')


#на "/sendnudes"
@dp.message(Command(commands=["sendnudes"]))
async def process_sendnudes_command(message: Message):
    await message.answer('ответ с порно')


#ваще всё кроме команд, работает потому что размещен после предыдущих хэндов
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается '
                                 'методом send_copy')


if __name__ == '__main__':
    dp.run_polling(bot)