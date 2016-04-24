#!/usr/bin/env python

import asyncio
import os

from aiohttp import web

from wuffi import get_application


os.environ.setdefault('WUFFI_SETTINGS_MODULE', 'config.settings.base')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(get_application(loop=loop))
    web.run_app(app)
