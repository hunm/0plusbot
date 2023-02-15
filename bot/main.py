#пук пук
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

from porn_api import getporn_from_request, getbestporn, getporn_from_category

API_TOKEN: str = '6177352917:AAFZSo4wP_R_Rmc-9jGcXoCXZLSHMQVxdRQ'

#объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Словарь, в котором будут храниться пользователи
users: dict = {}

#переменная, определяющая, сколько видосиков отправится челу :)
lim = 10

#хэндлер на "/start" + добавление новых пользователей в словарь
#из минусов - слетает после каждого запуска, надо заново писать старт
@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('Привет!\nЯ бот для поиска порно')

    if message.from_user.id not in users:
        #по умолчанию ставит хочет_порно в фолс для всех
        users[message.from_user.id] = {
                                        'wanna_porn': False,
                                        'wanna_categoried_porn' : False
                                        }

#хэнд на  "/help"
@dp.message(Command(commands=["help"]))
async def help_command(message: Message):
    await message.answer('текст который выводится при хелп')


#на "/request", ставит хочет_порно в тру
@dp.message(Command(commands=["request"]))
async def send_request_command(message: Message):
    users[message.from_user.id]['wanna_porn'] = True
    await message.answer('напишите ваш запрос')

#на "/best", сразу кидает порно
@dp.message(Command(commands=["best"]))
async def send_best_command(message: Message):
    porn = getbestporn()
    for i in range(lim):
        await message.answer(porn[i])

#на "/categories", ставит хочет_порно в тру
@dp.message(Command(commands=["categories"]))
async def send_category_command(message: Message):
    users[message.from_user.id]['wanna_categoried_porn'] = True
    await message.answer('напишите интересующий вас жанр, один из:\n asia, ebony, gay_sex, orgy\n пожалуйста, не пишите другие жанры, я пока не умею их обрабатывать :с')

#если чел хочет порно, кидает порно + ставит статус хочет_порно в фолс, если не хочет, кидает ему его же сообщ
@dp.message()
async def send_echo(message: Message):
    if users[message.from_user.id]['wanna_porn']:
        porn = getporn_from_request(message.text)
        for i in range(lim):
            await message.answer('порно по запросу ' + message.text + ':\n' + porn[i])
        users[message.from_user.id]['wanna_porn'] = False

    elif users[message.from_user.id]['wanna_categoried_porn']:
        porn = getporn_from_category(message.text)
        for i in range(lim):
            await message.answer('вот ваше порно:\n' + porn[i])
        users[message.from_user.id]['wanna_categoried_porn'] = False

    else:
        await message.send_copy(chat_id=message.chat.id)



if __name__ == '__main__':
    dp.run_polling(bot)