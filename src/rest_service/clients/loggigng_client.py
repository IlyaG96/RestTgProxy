import aiohttp
import json


class LoggingClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = aiohttp.ClientSession()

    async def send_log(self, message):
        try:
            async with self.session.post(f"{self.base_url}", data=json.dumps({"message": message})) as response:
                if not response.ok != 200:
                    print(f"Error sending log: {response.reason}")
                print(f"Sending log: {response.reason}")
        except Exception as e:
            pass
    async def close(self):
        await self.session.close()
