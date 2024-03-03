from src.application import init_app
from app_config import Config
from aiohttp import web
import asyncio
from src.logger.logger import logger

async def main():
    app = await init_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, Config.HOST, Config.PORT)
    logger.info(f"Starting server at {Config.HOST}:{Config.PORT}")
    await site.start()

    while True:
        await asyncio.sleep(1)


asyncio.run(main())
