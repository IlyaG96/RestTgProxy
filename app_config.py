import os

class Config:
    DEBUG = os.environ.get("DEBUG", "False") == "True"
    HOST = os.environ.get("HOST", "127.0.0.1")
    PORT = int(os.environ.get("PORT", 10000))
    INTEGRATION_LOG_ON = bool(os.environ.get("INTEGRATION_LOG_ON", 1))
    INTEGRATION_LOG_HOST = os.environ.get("INTEGRATION_LOG_HOST", "http://127.0.0.1")
    INTEGRATION_LOG_ENDPOINT = os.environ.get("INTEGRATION_LOG_ENDPOINT", "/log")
    INTEGRATION_LOG_PORT = int(os.environ.get("INTEGRATION_LOG_PORT", 10000))
