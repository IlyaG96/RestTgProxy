from src.application import init_app
from app_config import get_app_config
from aiohttp import web
import asyncio
from src.logger.logger import logger



async def main():
    app_config = get_app_config()
    app = await init_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, app_config.HOST, app_config.PORT)
    logger.info(f"Starting server at {app_config.HOST}:{app_config.PORT}")
    await site.start()

    while True:
        await asyncio.sleep(1)


asyncio.run(main())
