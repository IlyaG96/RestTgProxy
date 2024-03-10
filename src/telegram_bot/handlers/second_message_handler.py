from telethon import events
from logger import logger
from integration_logger.services.logging_service import LoggingService
from integration_logger.utils import with_global_logging_service


@with_global_logging_service
async def second_message_handler(event: events.NewMessage(), logging_service: LoggingService = None):
    logger.info(f"Incoming message from {event.chat.id} message:{event.message.message}")
    await logging_service.log(message="hi")
    await event.respond("Второе сообщение получено!")
