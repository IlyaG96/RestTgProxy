from aiohttp import web

from rest_service.routes.routes import setup_routes
import asyncio

from logger.logger import logger



async def init_app(app_config):

    app: web.Application = web.Application()
    setup_routes(app)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, app_config.HOST, app_config.PORT)
    await site.start()
    print("site started")
    logger.info(f"Starting server at {app_config.HOST}:{app_config.PORT}")
    await asyncio.Event().wait()

    return app
