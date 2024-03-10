from aiohttp import web

from rest_service.models.aiohttp_overrided_models import CustomRequest


async def debug_log_handler(request: CustomRequest):
    try:
        body: dict = await request.json()
    except Exception as e:
        return web.json_response({"success": "false"})

    return web.json_response({"hello": "tm"})