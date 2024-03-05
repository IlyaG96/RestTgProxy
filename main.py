from src.rest_service.application import init_app
from src.telegram_bot.application import init_bot
from app_config import get_app_config
import asyncio

app_config = get_app_config()


async def main():
    await asyncio.gather(
        init_bot(app_config),
        init_app(app_config),
    )

asyncio.run(main())
