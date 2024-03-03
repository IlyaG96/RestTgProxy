from aiohttp import web
from aiohttp.web import Request
from services.logging_service import LoggingService
from models.integration_log_message import create_message


async def telegram_incoming_handler(request: Request):
    logging_service: LoggingService = request.app["logging_service"]
    try:
        body: dict = await request.json()
    except Exception as e:
        return web.json_response({"success": "false"})

    await logging_service.log(create_message(body).model_dump())
    return web.json_response({"hello": "tm"})
