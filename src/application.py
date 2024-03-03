from aiohttp import web

from src.constants import LOGGING_SERVICE
from src.routes.routes import setup_routes
from src.services.logging_service import LoggingService


async def init_app():
    logging_service: LoggingService = LoggingService()

    app: web.Application = web.Application()
    app[LOGGING_SERVICE] = logging_service
    setup_routes(app)

    return app
