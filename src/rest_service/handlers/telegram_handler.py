from aiohttp import web

from logger import logger
from rest_service.models.aiohttp_overrided_models import CustomRequest
from rest_service.services.logging_service import LoggingService
from rest_service.models.integration_log_message import create_message
from rest_service.utils import with_global_logging_service


@with_global_logging_service
async def telegram_incoming_handler(request: CustomRequest, logging_service: LoggingService):
    logger.info(f"Hello from tm handler")

    try:
        body: dict = await request.json()
    except Exception as e:
        return web.json_response({"success": "false"})

    await logging_service.log(create_message(body).model_dump())
    return web.json_response({"hello": "tm"})


@with_global_logging_service
async def telegram_manual_handler(request: dict, logging_service: LoggingService):
    #is message valid?
    await logging_service.log(create_message(request).model_dump())
