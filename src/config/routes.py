# -*- coding: utf-8 -*-

from aiohttp import web, web_urldispatcher


async def index(request):
    return web.Response(body=b'I am index!')


router = web_urldispatcher.UrlDispatcher()
router.add_route('GET', '/', index)
