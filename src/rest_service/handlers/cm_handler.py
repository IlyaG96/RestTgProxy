from logger import logger
from aiohttp.web import Request
from src.rest_service.services import telegram_service


async def service_model_incoming_handler(request: Request):
    logger.info(f"Received data from model service: {request.text()}")

    await telegram_service.send()




