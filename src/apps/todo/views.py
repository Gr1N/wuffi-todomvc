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


class TodoView(RetrieveUpdateDestroyView):
    table = tables.item

    validator_class = validation.Validator
    validation_schema = schemas.item
