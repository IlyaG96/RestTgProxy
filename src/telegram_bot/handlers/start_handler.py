from telethon import events


async def start_handler(event: events.NewMessage()):
    await event.respond('Hello World!')