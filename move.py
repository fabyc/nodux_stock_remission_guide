# -*- coding: utf-8 -*-

import collections
import logging
from decimal import Decimal
from trytond.pyson import Eval
from trytond.pyson import Id
from trytond.model import ModelSQL, Workflow, fields, ModelView
from trytond.transaction import Transaction
from trytond.wizard import Wizard, StateTransition, StateView, Button
from trytond.pool import Pool, PoolMeta

__all__ = ['Move']
__metaclass__ = PoolMeta

class Move():
    "Stock Move"
    __name__ = 'stock.move'

    internal = fields.Boolean('Movimiento Interno')

    @classmethod
    def __setup__(cls):
        super(Move, cls).__setup__()

    @classmethod
    def default_quantity(cls):
        return 1
