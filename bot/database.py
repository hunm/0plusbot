from asyncio import AbstractEventLoop
from loguru import logger
from typing import Optional

import asyncpg


class Database:
    def __init__(
        self,
        name: Optional[str],
        user: Optional[str],
        password: Optional[str],
        host: Optional[str],
        port: Optional[str],
        loop: AbstractEventLoop,
        pool: asyncpg.pool.Pool,
    ) -> None:
        self.name = name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.loop = loop
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                database=name,
                user=user,
                password=password,
                host=host,
                port=port,
            )
        )

    async def create_tables(self) -> None:
        """create tables in the database."""
        with open("bot/sql/init.sql", "r") as f:
            sql = f.read()
        await self.pool.execute(sql)

    async def close_database(self) -> None:
        await self.pool.close()

    async def add_user(self, user_id: int, name: str) -> None:
        """add a new user to the database."""
        await self.pool.execute(f"INSERT INTO Users VALUES({user_id}, '{name}'")
        logger.info(f"added new user | user_id: {user_id}; name: {name}")

    async def update_wanna_porn(self, user_id: int, is_wanna: bool) -> None:
        """make is wanna porn flag True"""
        await self.pool.execute(f"UPDATE Users SET is_wanna_porn = {str(is_wanna).capitalize()} WHERE user_id = {user_id}")

    async def update_wanna_categoried_porn(self, user_id: int, is_wanna: bool) -> None:
        """make is wanna categoried porn flag True"""
        await self.pool.execute(f"UPDATE Users SET is_wanna_categoried_porn = {str(is_wanna).capitalize()} WHERE user_id = {user_id}")

    async def get_user_wanna_porn(self, user_id: int) -> bool:
        """get is user wanna porn flag"""
        is_wanna_porn = await self.pool.fetchval(f"SELECT is_wanna_porn FROM Users WHERE user_id = {user_id}")
        return True if is_wanna_porn == "TRUE" else False

    async def get_user_wanna_categoried_porn(self, user_id: int) -> bool:
        """get is user wanna porn flag"""
        is_wanna_categoried_porn = await self.pool.fetchval(f"SELECT is_wanna_categoried_porn FROM Users WHERE user_id = {user_id}")
        return True if is_wanna_categoried_porn == "TRUE" else False

