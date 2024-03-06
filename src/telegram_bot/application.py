import pydantic_settings
from telethon import TelegramClient
from .handlers import setup_handlers
from telethon.sessions import MemorySession


async def init_bot(app_config: pydantic_settings.BaseSettings) -> None:
    bot: TelegramClient = await TelegramClient(MemorySession(), app_config.API_ID, app_config.API_HASH).start(
        bot_token=app_config.BOT_TOKEN
    )

    setup_handlers(bot)
    await bot.start()
    print("bot started")
    await bot.run_until_disconnected()