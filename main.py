from src.application import init_app
from src.app_config import Config
from aiohttp import web
import asyncio


async def main():
    app = await init_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, Config.HOST, Config.PORT)
    print(f"Starting server at {Config.HOST}:{Config.PORT}")
    await site.start()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
