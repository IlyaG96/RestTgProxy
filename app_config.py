import os
from functools import lru_cache
from pydantic_settings import BaseSettings


class _Config(BaseSettings):
    DEBUG: bool = bool(os.environ.get("DEBUG", ))
    HOST: str = os.environ.get("HOST", "0.0.0.0")
    PORT: int = int(os.environ.get("PORT", 10000))
    INTEGRATION_LOG_ON: bool = bool(os.environ.get("INTEGRATION_LOG_ON", 1))
    INTEGRATION_LOG_URI: str = os.environ.get("INTEGRATION_LOG_HOST", "http://127.0.0.1:10000/log")


@lru_cache
def get_app_config():
    return _Config()
