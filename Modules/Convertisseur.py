from decimal import Decimal, getcontext

class Convertisseur:
    def __init__(self):
        getcontext().prec = 28

    def float_to_decimal(self, nb:float) -> Decimal:
        return Decimal(str(nb))

    def decimal_to_float(self, nb:Decimal) -> float:
        return float(nb)