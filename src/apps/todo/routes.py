# -*- coding: utf-8 -*-

from wuffi.core.urls import UrlDispatcher

from apps.todo.views import todo


router = UrlDispatcher()
router.add_route('GET', '/', todo)
