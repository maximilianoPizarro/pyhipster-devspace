
from enum import Enum, auto

###
# The MetodoDePago enumeration
###

class MetodoDePago(Enum): 
    EFECTIVO = "efectivo"
    CUPON = "cupon"

    value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

