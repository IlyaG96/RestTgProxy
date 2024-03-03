from src.clients.loggigng_client import LoggingClient

from app_config import Config


class LoggingService:
    def __init__(self, logging_client: LoggingClient = None):
        self.logging_client = logging_client or LoggingClient(
            base_url=f'{Config.INTEGRATION_LOG_HOST}:{Config.INTEGRATION_LOG_PORT}{Config.INTEGRATION_LOG_ENDPOINT}'
        )

    async def log(self, message):
        if not Config.INTEGRATION_LOG_ON:
            return
        await self.logging_client.send_log(message)
