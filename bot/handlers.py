from aiogram import types
from bot.loader import bot
from bot.loader import db
from bot.loader import dp

from porn_api import getporn_from_request, getbestporn, getporn_from_category


@dp.message_handler(commands="start")
async def start_message(message: types.Message) -> None:
    """welcome message."""
    if await db.verification(message.from_user.id):
        await bot.send_message(message.chat.id, "Привет!\nЯ бот для поиска порно")
    else:
        if message.from_user.first_name != "None":
            name = message.from_user.first_name
        elif message.from_user.username != "None":
            name = message.from_user.username
        elif message.from_user.last_name != "None":
            name = message.from_user.last_name
        else:
            name = ""
        await db.add_user(message.from_user.id, name)
        await bot.send_message(message.chat.id, "Привет!\nЯ бот для поиска порно. Я тебя запомнил)")


@dp.message_handler(commands=("help", "info", "about"))
async def give_info(message: types.Message) -> None:
    """the target of this bot."""
    await bot.send_message(message.chat.id, "текст который выводится при хелп")


@dp.message(commands="request")
async def send_request_command(message: types.Message):
    await db.update_wanna_porn(message.from_user.id, True)
    await message.answer('напишите ваш запрос')


@dp.message(commands="best")
async def send_best_command(message: types.Message):
    porn = getbestporn()
    for i in range(10):
        await message.answer(porn[i])


@dp.message(commands="categories")
async def send_category_command(message: types.Message):
    await db.update_wanna_categoried_porn(message.from_user.id, True)
    await message.answer('напишите интересующий вас жанр, один из:\n asia, ebony, gay_sex, orgy\n пожалуйста, '
                         'не пишите другие жанры, я пока не умею их обрабатывать :с')


@dp.message()
async def send_echo(message: types.Message):
    user_wanna_porn = db.get_user_wanna_porn()
    user_wanna_categoried_porn = db.get_user_wanna_categoried_porn()
    if user_wanna_porn:
        porn = getporn_from_request(message.text)
        for i in range(10):
            await message.answer('порно по запросу ' + message.text + ':\n' + porn[i])
        db.update_wanna_porn(message.from_user.id, False)

    elif user_wanna_categoried_porn:
        porn = getporn_from_category(message.text)
        for i in range(10):
            await message.answer('вот ваше порно:\n' + porn[i])
        db.get_user_wanna_categoried_porn(message.from_user.id, False)

    else:
        await message.send_copy(chat_id=message.chat.id)
