from aiohttp import web
from pydantic_settings import BaseSettings
from rest_service.routes.routes import setup_routes
import asyncio

from logger.logger import logger
from telegram_bot.application import _TelegramBot


class _WebApplication:
    app: web.Application
    app_config: BaseSettings
    bot: _TelegramBot
    
    @classmethod
    async def create(cls, app_config: BaseSettings):
        self = cls()
        self.app: web.Application = await self.__init_app()
        self.app_config = app_config
        setup_routes(self.app)
        return self

    async def set_bot(self, bot: _TelegramBot):
        self.bot = bot

    async def run(self):
        if self.app is not None:
            runner = web.AppRunner(self.app)
            await runner.setup()
            site = web.TCPSite(runner, self.app_config.HOST, self.app_config.PORT)
            await site.start()
            logger.info(f"Started server at {self.app_config.HOST}:{self.app_config.PORT}")
            await asyncio.Event().wait()

        raise Exception("There is no app object!")

    @staticmethod
    async def __init_app():
        app: web.Application = web.Application()
        setup_routes(app)
        logger.info(f"App init success")
        return app


async def create_app(app_config: BaseSettings):
    app: _WebApplication = await _WebApplication.create(app_config)
    return app
