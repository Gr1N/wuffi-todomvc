# -*- coding: utf-8 -*-

from wuffi.core.urls import UrlDispatcher

from apps.todo import views


router = UrlDispatcher()
router.add_route('*', '/{id}', views.TodoView)
