import os
from functools import lru_cache
from pydantic_settings import BaseSettings


class _Config(BaseSettings):
    DEBUG: bool = bool(os.environ.get("DEBUG", ))
    HOST: str = os.environ.get("HOST", "0.0.0.0")
    PORT: int = int(os.environ.get("PORT", 10000))
    INTEGRATION_LOG_ON: bool = bool(os.environ.get("INTEGRATION_LOG_ON", 1))
    INTEGRATION_LOG_URI: str = os.environ.get("INTEGRATION_LOG_HOST", "http://127.0.0.1:10000/log")
    BOT_TOKEN: str = os.environ.get("API_HASH", "111:22222KKK")
    API_ID: int = os.environ.get("API_ID", 123123123)
    API_HASH: str = os.environ.get("API_HASH", "9KKLL040")


@lru_cache
def get_app_config():
    return _Config()
