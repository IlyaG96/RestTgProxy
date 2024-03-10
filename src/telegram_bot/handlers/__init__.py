from telethon import TelegramClient
from telethon import events

from .start_handler import start_handler
from .second_message_handler import second_message_handler


def setup_handlers(bot: TelegramClient):
    bot.add_event_handler(start_handler, events.NewMessage(pattern='/start'))
    bot.add_event_handler(second_message_handler, events.NewMessage(pattern="далее"))