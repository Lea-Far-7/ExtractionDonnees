from decimal import Decimal, getcontext

"""
Cette classe a un but purement esthétique pour faciliter la compréhension du code
"""
class Convertisseur:

    def __init__(self):

        getcontext().prec = 28 # Détermine la précision de la conversion


    def float_to_decimal(self, nb:float) -> Decimal:
        """
        Convertit un nombre flottant en Décimal pour des calculs de précision avec python
        :param nb: Un nombre flottant
        :return: Un décimal
        """
        return Decimal(str(nb))

    def decimal_to_float(self, nb:Decimal) -> float:
        """
        Convertit un Décimal en nombre flottant
        :param nb: Un Décimal
        :return: Un nombre flottant
        """
        return float(nb)