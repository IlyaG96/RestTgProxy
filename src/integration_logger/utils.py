import functools
from integration_logger.services.logging_service import get_or_create_logging_service


def with_global_logging_service(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        kwargs['logging_service'] = get_or_create_logging_service()
        return await func(*args, **kwargs)
    return wrapper
