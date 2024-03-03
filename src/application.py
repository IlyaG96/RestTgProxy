from aiohttp import web

from constants import LOGGING_SERVICE
from routes.routes import setup_routes
from services.logging_service import LoggingService


async def init_app():
    logging_service: LoggingService = LoggingService()

    app: web.Application = web.Application()
    app[LOGGING_SERVICE] = logging_service
    setup_routes(app)

    return app
