import pydantic_settings
from telethon import TelegramClient
from pydantic_settings import BaseSettings
from logger import logger
from .handlers import setup_handlers
from telethon.sessions import MemorySession


class _TelegramBot:
    bot: TelegramClient

    @classmethod
    async def create(cls, app_config: BaseSettings):
        self: _TelegramBot = cls()
        self.bot: TelegramClient = await self.__init_bot(app_config)
        setup_handlers(self.bot)
        return self

    async def run(self):
        if self.bot is not None:
            await self.bot.start()
            logger.info(f"Bot started")
            await self.bot.run_until_disconnected()
        raise Exception("There is no bot object!")

    @staticmethod
    def __init_bot(app_config: pydantic_settings.BaseSettings) -> TelegramClient:
        bot: TelegramClient = TelegramClient(MemorySession(), app_config.API_ID, app_config.API_HASH).start(
            bot_token=app_config.BOT_TOKEN
        )
        logger.info(f"Bot init success")
        return bot


async def create_bot(app_config: BaseSettings):
    bot: _TelegramBot = await _TelegramBot.create(app_config)
    return bot
