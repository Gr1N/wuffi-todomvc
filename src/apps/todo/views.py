# -*- coding: utf-8 -*-

from wuffi import validation
from wuffi.views.generic import ListCreateView, RetrieveUpdateDestroyView

from apps.todo import schemas, tables

__all__ = (
    'TodosView',
    'TodoView',
)


class TodosView(ListCreateView):
    table = tables.item

    order_by = tables.item.c.id

    validator_class = validation.Validator
    validation_schema = schemas.item

    def get_created_headers(self, obj):
        location = self.request.app.router['todos:details'].url(parts={
            'id': obj.id,
        })

        return {
            'Location': location,
        }


class TodoView(RetrieveUpdateDestroyView):
    table = tables.item

    validator_class = validation.Validator
    validation_schema = schemas.item
