import unittest

from Metier.demiJour import DemiJour

class TestDemiJour(unittest.TestCase):

    # Creation de demiJours
    dj1 = DemiJour(2, "Lundi AM")
    dj2 = DemiJour(5, "Mercredi M")

    def testAffichage(self):
        result = DemiJour.__str__(TestDemiJour.dj1)
        self.assertEqual(result, "DemiJour 1 : Lundi AM")

    def testAffichageSimple(self):
        result = DemiJour.__repr__(TestDemiJour.dj2)
        self.assertEqual(result, "Mercredi M")


if __name__ == '__main__':
    unittest.main()