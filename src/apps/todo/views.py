# -*- coding: utf-8 -*-

from aiohttp import web

__all__ = (
    'todo',
)


async def todo(request):
    return web.Response(body=b'todo')
