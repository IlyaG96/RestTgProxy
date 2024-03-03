from aiohttp import web
from handlers.cm_handler import cm_incoming_handler
from handlers.log_handler import debug_log_handler
from handlers.telegram_handler import telegram_incoming_handler


def setup_routes(app: web.Application):
    app.router.add_post('/tm', telegram_incoming_handler)
    app.router.add_post('/cm', cm_incoming_handler)
    app.router.add_post('/log', debug_log_handler)
    return app
