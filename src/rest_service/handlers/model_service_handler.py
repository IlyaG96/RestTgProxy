from logger import logger

from rest_service.models.aiohttp_overrided_models import CustomRequest
from rest_service.services.telegram_service import ConcreteTelegramService


async def service_model_incoming_handler(request: CustomRequest):

    cm_raw_message: str = await request.text()

    logger.info(f"Received data from model service: {cm_raw_message}")
    bot: ConcreteTelegramService = request.app.bot

    await bot.send(message=cm_raw_message)




