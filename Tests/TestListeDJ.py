import unittest

from Modules.listeDemiJours import ListeDemiJours 
from Metier.demiJour import DemiJour 

class TestListeDJ(unittest.TestCase):

    def test_getListe(cls):
        result = ListeDemiJours.getListeDJ(cls)
        cls.assertEqual(result, ["Lundi M", "Lundi AM", "Mardi M", "Mardi AM", "Mercredi M", "Mercredi AM", "Jeudi M", "Jeudi AM", "Vendredi M","Vendredi AM"])

    def test_getDJ(cls, i):
        result = ListeDemiJours.getDJ(cls, 5)
        cls.assertEqual("Mercredi AM")

if __name__ == '__main__':
    unittest.main()