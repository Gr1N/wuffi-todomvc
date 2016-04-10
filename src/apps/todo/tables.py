# -*- coding: utf-8 -*-

import sqlalchemy as sa

__all__ = (
    'item',
)


_metadata = sa.MetaData()

item = sa.Table(
    'item', _metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('completed', sa.Boolean, nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('order', sa.Integer, nullable=True),
)
