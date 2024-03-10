import aiohttp
import json

from logger import logger


class LoggingClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = aiohttp.ClientSession()

    async def send_log(self, message):
        try:
            async with self.session.post(f"{self.base_url}", data=json.dumps({"message": message})) as response:
                logger.info(f"Sending integration log: {response.reason} with data: {message}")
                if not response.ok != 200:
                    logger.error(f"ERROR sending log: {response.reason}, status: {response.status}")
                logger.info(f"SUCCESS Sending integration log: {response.reason}")

        except Exception as e:
            logger.error(f"ERROR during sending integration log: {e.__str__()}")
        finally:
            await self.close()

    async def close(self):
        await self.session.close()
