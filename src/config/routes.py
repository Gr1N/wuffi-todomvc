# -*- coding: utf-8 -*-

from aiohttp import web, web_urldispatcher


async def index(request):
    return web.Response(body=b'I am index!')


async def rset(request):
    cache = request.app['cache']
    await cache.set('key', 'value')

    return web.json_response()


async def rget(request):
    cache = request.app['cache']
    value = await cache.get('key')

    return web.json_response(data=value)


router = web_urldispatcher.UrlDispatcher()
router.add_route('GET', '/', index)
router.add_route('GET', '/rset', rset)
router.add_route('GET', '/rget', rget)
