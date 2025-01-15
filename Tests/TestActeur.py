import unittest

from Metier.acteur import Acteur
from Metier.demiJour import DemiJour

class TestActeur(unittest.TestCase):

    # Creations de plusieurs demiJours
    dj1 = DemiJour(1, "Lundi M")
    dj2 = DemiJour(5, "Mercredi M")
    dj3 = DemiJour(6, "Mercredi AM")
    dj4 = DemiJour(4, "Mardi AM")


    # Creation de plusieurs Acteurs
    acteur0 = Acteur(126.4654, -34.343643, [dj1, dj3])
    acteur1 = Acteur(23.45646, 134.46546, [dj2, dj4])
    acteur2 = Acteur(-32.36565, 46.3561153, [dj3])

    def test_delActeur(self):
        result = Acteur.__del__(TestActeur.acteur1)
        self.assertEqual(Acteur.nb, 2)

    def test_addDispo(self):
        result = Acteur.addDispo(TestActeur.acteur2, TestActeur.dj4)
        self.assertIn(TestActeur.dj4, TestActeur.acteur2.dispos)

    def test_removeDispo(self):
        result = Acteur.removeDispo(TestActeur.acteur0, TestActeur.dj1)
        self.assertNotIn(TestActeur.dj1, TestActeur.acteur0.dispos)

    def test_getInfosTournees(self):
        result = Acteur.getInfosTournees()


if __name__ == '__main__':
    unittest.main()