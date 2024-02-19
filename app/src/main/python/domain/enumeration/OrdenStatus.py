
from enum import Enum, auto

###
# The OrdenStatus enumeration
###

class OrdenStatus(Enum): 
	COMPLETO = auto()
	PAGADO = auto()
	PENDIENTE = auto()
	CANCELADO = auto()
	RECHAZADO = auto()
