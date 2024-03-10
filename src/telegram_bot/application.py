import asyncio
import time
from abc import ABC, abstractmethod
from typing import Optional

import pydantic_settings
from telethon import TelegramClient, errors
from pydantic_settings import BaseSettings
from logger import logger
from .handlers import setup_handlers
from telethon.sessions import MemorySession


class TelegramBotInterface(ABC):
    @abstractmethod
    def create(self, app_config: BaseSettings):
        raise NotImplementedError
        
    @abstractmethod
    def run(self):
        raise NotImplementedError


class ConcreteTelegramBot(TelegramBotInterface, ABC):
    bot: TelegramClient

    @classmethod
    async def create(cls, app_config: BaseSettings):
        self: ConcreteTelegramBot = cls()
        self.bot: TelegramClient = await self.__init_bot(app_config)
        setup_handlers(self.bot)
        return self

    async def run(self):
        await self.bot.start()
        logger.info(f"Bot started")
        await self.bot.run_until_disconnected()

    @staticmethod
    async def __init_bot(app_config: pydantic_settings.BaseSettings) -> TelegramClient:
        bot: Optional[TelegramClient] = None
        try:
            bot: TelegramClient = await TelegramClient(MemorySession(), app_config.API_ID, app_config.API_HASH).start(
                bot_token=app_config.BOT_TOKEN
            )
            logger.info(f"Bot object init success")
        except errors.FloodWaitError as e:
            logger.info(f"Have to sleep {e.seconds} seconds")

            print(f"Have to sleep {e.seconds} seconds")
            await asyncio.sleep(e.seconds)

        return bot #TODO FIXME


async def create_bot(app_config: BaseSettings):
    bot: ConcreteTelegramBot = await ConcreteTelegramBot.create(app_config)
    return bot
