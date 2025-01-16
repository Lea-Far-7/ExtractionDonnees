import unittest

from Modules.convertisseur import Convertisseur 
from decimal import Decimal, getcontext

class TestConvertisseur(unittest.TestCase):

    def test_floatToDecimal(self, nb):
        result = Convertisseur.float_to_decimal(0.1)
        self.assertEqual(result, "0.100000001490116119384765625")

    def test_decimalToFloat(self, nb):
        result = Convertisseur.decimal_to_float(2.1234567890123456789)
        self.assertEqual(result, 2.1234567890123457)
        
if __name__ == '__main__':
    unittest.main()