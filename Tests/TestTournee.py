import unittest

from Modules.Convertisseur import Convertisseur

from Metier.acteur import Acteur
from Metier.producteur import Producteur
from Metier.demiJour import DemiJour
from Metier.tache import Tache
from Modules.distance import distance
from Metier.tournee import Tournee
from Metier.client import Client 

class TestTournee(unittest.TestCase):

    # Creation de demiJours
    dj1 = DemiJour(2, "Lundi AM")
    dj2 = DemiJour(3, "Mardi M")
    dj3 = DemiJour(5, "Mercredi M")
    dj4 = DemiJour(8, "Jeudi AM")

    # Creation de producteurs
    producteur0 = Producteur(65.654654, -15.3154, 22.6, [dj1, dj2], [])
    producteur1 = Producteur(35.346546, 34.35454, 54.1, [dj1], [])
    producteur2 = Producteur(32.36546, -13.4564, 23.7, [dj3, dj4], [])

    # Creation de clients
    client3 = Client(12.365465, 64.346546, [dj1])
    client4 = Client(-56.316546, 13.3215, [dj2, dj4])
    client5 = Client(13.36546, 13.356456, [dj2])

    # Creation de taches
    tache1 = Tache("P", 59.1, producteur1, client3, "9:0")
    tache2 = Tache("D", 46.2, client4, producteur2, "15:0")
    tache3 = Tache("D", ,20.3, client5, producteur0, "12:0")
    tache4 = Tache("P", 37, producteur2, client5, "18:0")

    # Creation de tournees
    tournee0 = Tournee(dj2, producteur0, [tache2, tache3])
    tournee1 = Tournee(dj1, producteur2, [tache4])
    tournee2 = Tournee(dj4, producteur2, [tache1, tache2])

    def test_del(self):
        result = Tournee.__del__(TestTournee.tournee1)
        self.assertEqual(Tournee.nb, 2)

    def test_addTache(self):
        result = Tournee.addTache(TestTournee.tournee0, "P", 41, producteur1, client3, "14h")
        self.assertIn(result, TestTournee.tournee0.taches)

    def test_removeTache(self):
        result = Tournee.removeTache(TestTournee.tournee0, TestTournee.tache3)
        self.assertNotIn(TestTournee.tache3, TestTournee.tournee0.taches)

    def test_getIdLieux(self):
        result = Tournee.get_id_lieux(TestTournee.tournee2)
        self.assertEqual(result, [1, 4])

    def test_distance(self):
        result = Tournee.distance(TestTournee.tournee0)
        self.assertEqual(result, ([13.66, 7.67], 13.66, 21.33))

    def test_chargement(self):
        result = Tournee.chargement(TestTournee.tournee2)
        self.assertEqual(result, ([59.1, 12.9], 59.1, 59.1))

    def test_duree(self):
        result = Tournee.duree(TestTournee.tournee2):
        self.assertEqual(result, ([360], 360, 360))

    def test_affichage(self):
        result = Tournee.__str__(TestTournee.tournee0):
        self.assertEqual(result, "Tournée 0 :\n\tdj2 \n\tProducteur 0 \n\tTaches : \n\t\ttache2 \n\t\ttache3")

if __name__ == '__main__':
    unittest.main()
