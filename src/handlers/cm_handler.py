from aiohttp import web


async def cm_incoming_handler(request):

    return web.json_response({"hello": "cm"})