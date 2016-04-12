# -*- coding: utf-8 -*-

from wuffi.views.generic import ListView, RetrieveView

from apps.todo import tables

__all__ = (
    'TodosView',
    'TodoView',
)


class TodosView(ListView):
    select = (
        tables.item,
    )
    order_by = tables.item.c.id


class TodoView(RetrieveView):
    select = (
        tables.item,
    )

    def get_where(self):
        return tables.item.c.id == self.request.match_info['id']
