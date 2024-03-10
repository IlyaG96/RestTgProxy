from aiohttp.web import Request, Application

from rest_service.services.telegram_service import ConcreteTelegramService


class CustomRequest(Request):
    app: 'CustomApplication'


class CustomApplication(Application):
    bot: ConcreteTelegramService

