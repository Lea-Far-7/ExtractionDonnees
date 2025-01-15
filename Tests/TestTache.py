import unittest

from Metier.tache import Tache 
from Metier.acteur import Acteur
from Metier.demiJour import DemiJour

class TestTache(unittest.TestCase):

    # Creation de demiJours
    dj1 = (1, "Lundi M")
    dj2 = (6, "Mercredi AM")
    dj3 = (8, "Jeudi AM")

    # Creation d'acteurs
    acteur0 = Acteur(115.3546, -31.3156646, [dj2])
    acteur1 = Acteur(154.36546, 33.1546, [dj1, dj2])
    acteur2 = Acteur(-35.33546, 101.31346, [dj3])

    # Creation de taches
    tache1 = Tache("P", 23.1, acteur0, acteur2, "14h")
    tache2 = Tache("D", 43.5, acteur1, acteur0, "11h")
    tache3 = Tache("D", 21.9, acteur2, acteur0, "17h")

    def test_del(self):
        result = Tache.__del__(TestTache.tache3)
        self.assertEqual(Tache.nb, 2)

    def test_getType(self):
        result = Tache.getType(TestTache.tache1)
        self.assertEqual(result, "Pick-Up")

    def test_str(self):
        result = Tache.__str__(TestTache.tache2)
        assertEqual(result, "Tâche 2 : \nDrop-Off 43.5 chez Client 1 de Producteur 0 à 11h")

if __name__ == '__main__':
    unittest.main()