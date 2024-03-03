from aiohttp import web

from src.logger.logger import logger


async def cm_incoming_handler(request):
    logger.info(f"Hello from cm handler")


    return web.json_response({"hello": "cm"})