from aiogram import Dispatcher
from aiogram import types


async def set_default_commands(dp: Dispatcher) -> None:
    await dp.bot.set_my_commands(
        [
            types.BotCommand("help", "help"),
            types.BotCommand("start", "start using bot"),
            types.BotCommand("request", "find porn by request"),
            types.BotCommand("categories", "find bot by categories"),
            types.BotCommand("best", "get best porn"),
        ]
    )