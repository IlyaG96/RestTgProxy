from telethon import events

from integration_logger.models.integration_log_message import create_first_message
from integration_logger.services.logging_service import LoggingService
from integration_logger.utils import with_global_logging_service
from logger import logger


@with_global_logging_service
async def start_handler(event: events.NewMessage(), logging_service: LoggingService):
    logger.info(f"Incoming message from {event.chat.id} message:{event.message.message}")

    await logging_service.log(create_first_message(event).model_dump())
    await event.respond("Рад приветствовать!")
