from telethon import events
from logger import logger
from integration_logger.services.logging_service import LoggingService
from integration_logger.utils import with_global_logging_service


@with_global_logging_service
async def second_message_handler(event: events.NewMessage(), logging_service: LoggingService):
    logger.info(f"Incoming message from {event.chat.id} message:{event.message.message}")

    await event.respond("Второе сообщение получено!")


# @with_global_logging_service
# async def telegram_incoming_handler(request: CustomRequest, logging_service: LoggingService):
#
#     try:
#         body: dict = await request.json()
#     except Exception as e:
#         return web.json_response({"success": "false"})
#
#     await logging_service.log(create_message(body).model_dump())
#     return web.json_response({"hello": "tm"})