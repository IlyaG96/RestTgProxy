from telethon import TelegramClient
from telethon import events

from .start_handler import start_handler


def setup_handlers(bot: TelegramClient):
    bot.add_event_handler(start_handler, events.NewMessage())