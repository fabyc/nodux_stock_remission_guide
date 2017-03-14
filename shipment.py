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

__all__ = ['ShipmentOut', 'ShipmentInternal']

class ShipmentOut():
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.out'

    motivo_traslado = fields.Char('Motivo de Traslado', states={
        'required': Eval('state') == 'packed',
        'readonly': Eval('state') == 'done',
    })
    dir_destinatario = fields.Char(u'Dirección de LLegada de Productos', states={
        'required': Eval('state') == 'packed',
        'readonly': Eval('state') == 'done',
    })

    @classmethod
    def __setup__(cls):
        super(ShipmentOut, cls).__setup__()

class ShipmentInternal():
    "Internal Shipment"
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.internal'

    @classmethod
    def __setup__(cls):
        super(ShipmentInternal, cls).__setup__()
        cls.moves.domain[0] = [('from_location', '=', Eval('from_location'))]

    @classmethod
    def default_effective_date(cls):
        date = Pool().get('ir.date')
        date = date.today()
        return date

    @classmethod
    def default_planned_date(cls):
        date = Pool().get('ir.date')
        date = date.today()
        return date
