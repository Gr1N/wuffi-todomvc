# -*- coding: utf-8 -*-

from aiohttp import web

from wuffi.core.urls import UrlDispatcher


async def index(request):
    return web.Response(body=b'Wuff Wuff')


router = UrlDispatcher()
router.add_route('GET', '/', index)
router.include_routes('/todo', 'apps.todo.routes')
