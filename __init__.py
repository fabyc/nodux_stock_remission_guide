#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.pool import Pool
from .shipment import *
from .move import *

def register():
    Pool.register(
        ShipmentOut,
        ShipmentInternal,
        Move,
        module='nodux_stock_remission_guide', type_='model')
