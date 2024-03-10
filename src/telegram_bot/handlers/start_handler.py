from telethon import events
from logger import logger


async def start_handler(event: events.NewMessage()):
    logger.info(f"Incoming message from {event.chat.id} message:{event.message.message}")
    await event.respond(event.message.message)
