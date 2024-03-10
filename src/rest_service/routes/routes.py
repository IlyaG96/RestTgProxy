from aiohttp import web
from rest_service.handlers.model_service_handler import service_model_incoming_handler
from rest_service.handlers.log_handler import debug_log_handler


def setup_routes(app: web.Application):
    app.router.add_post('/post', service_model_incoming_handler)
    app.router.add_get('/cm', service_model_incoming_handler)
    app.router.add_post('/log', debug_log_handler)
    return app
