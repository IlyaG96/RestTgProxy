from src.rest_service.application import create_app
from src.telegram_bot.application import create_bot
from app_config import get_app_config
import asyncio

app_config = get_app_config()


async def main():
    bot = await create_bot(app_config)
    app = await create_app(app_config)

    await app.set_bot(bot)

    await asyncio.gather(
        bot.run(),
        app.run(),
    )

asyncio.run(main())
