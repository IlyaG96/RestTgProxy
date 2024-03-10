from aiohttp import web
from pydantic_settings import BaseSettings
from rest_service.routes.routes import setup_routes
import asyncio

from logger.logger import logger
from rest_service.services.telegram_service import ConcreteTelegramService
from telegram_bot.application import ConcreteTelegramBot


class _WebApplication:
    app: web.Application
    app_config: BaseSettings
    bot_service: ConcreteTelegramService
    
    @classmethod
    async def create(cls, app_config: BaseSettings):
        self = cls()
        self.app: web.Application = await self.__init_app()
        self.app_config = app_config
        setup_routes(self.app)
        return self

    async def set_bot(self, bot: ConcreteTelegramBot):
        self.bot_service = ConcreteTelegramService(bot)
        self.app.bot = self.bot_service

    async def run(self):
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, self.app_config.HOST, self.app_config.PORT)
        await site.start()
        logger.info(f"Started server at {self.app_config.HOST}:{self.app_config.PORT}")
        while True:
            await asyncio.sleep(0.1)

    @staticmethod
    async def __init_app():
        app: web.Application = web.Application()
        setup_routes(app)
        logger.info(f"App init success")
        return app


async def create_app(app_config: BaseSettings):
    app: _WebApplication = await _WebApplication.create(app_config)
    return app
