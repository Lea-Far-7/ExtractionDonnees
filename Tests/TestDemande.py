import unittest

from Metier.demande import Demande
from Metier.producteur import Producteur
from Metier.client import Client
from Metier.demiJour import DemiJour
from Metier.acteur import Acteur

class TestDemande(unittest.TestCase):

    # Creation de demiJours
    dj1 = DemiJour(2, "Lundi AM")
    dj2 = DemiJour(3, "Mardi M")
    dj3 = DemiJour(6, "Mercredi AM")

    # Creation de producteurs
    producteur0 = Producteur(35.31365, -34.3456, 32.7, [dj2], [])
    producteur1 = Producteur(31.31313, 145.31555, 56.1, [dj1, dj3], [])

    # Creation de clients
    client2 = Client(31.4564, -134.34654, [dj1, dj2])
    client3 = Client(56.31354, 112.4546, [dj2, dj3])

    # Creation de demandes
    demande0 = Demande(client2, producteur1, 23.4)
    demande1 = Demande(client3, producteur0, 50.6)
    demande2 = Demande(client2, producteur0, 12.7)

    def test_del(self):
        result = Demande.__del__(TestDemande.demande2)
        self.assertEqual(Demande.nb, 2)

    def test_Affichage(self):
        result = Demande.__str__(TestDemande.demande0)
        self.assertEqual(result, "Demande 0 : 23.4 kg de Client 2 à Producteur 1")

    def test_deleteAll(cls):
        result = Demande.deleteAll(cls):
        self.assertEqual(cls.nb, 0)

    def test_getNbDemandesActeurs(cls):
        result = Demande.getNbDemandesActeurs(cls)
        self.assertEqual(result, {})
        

    

if __name__ == '__main__':
    unittest.main()
