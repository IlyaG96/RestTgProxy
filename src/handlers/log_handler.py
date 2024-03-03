from aiohttp import web


async def debug_log_handler(request: web.Request):
    try:
        body: dict = await request.json()
    except Exception as e:
        return web.json_response({"success": "false"})

    return web.json_response({"hello": "tm"})