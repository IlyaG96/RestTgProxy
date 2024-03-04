from aiohttp import web

from src.routes.routes import setup_routes


async def init_app():

    app: web.Application = web.Application()
    setup_routes(app)

    return app
