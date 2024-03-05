import pydantic_settings
from telethon import TelegramClient
from .handlers import setup_handlers


async def init_bot(app_config: pydantic_settings.BaseSettings) -> TelegramClient:
    bot: TelegramClient = await TelegramClient('session_name', app_config.API_ID, app_config.API_HASH).start(
        bot_token=app_config.BOT_TOKEN
    )

    setup_handlers(bot)
    await bot.start()
    print("bot started")
    await bot.run_until_disconnected()