# -*- coding: utf-8 -*-

from wuffi.views.generic import RetrieveView

from apps.todo import tables

__all__ = (
    'TodoView',
)


class TodoView(RetrieveView):
    select = (
        tables.item,
    )

    def get_where(self):
        return tables.item.c.id == self.request.match_info['id']
