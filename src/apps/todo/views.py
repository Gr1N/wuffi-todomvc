# -*- coding: utf-8 -*-

from wuffi.views.generic import ListView, RetrieveView

from apps.todo import tables

__all__ = (
    'TodosView',
    'TodoView',
)


class TodosView(ListView):
    table = tables.item

    order_by = tables.item.c.id


class TodoView(RetrieveView):
    table = tables.item
