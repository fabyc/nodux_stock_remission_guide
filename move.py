# -*- coding: utf-8 -*-

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

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
