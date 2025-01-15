import unittest

from Metier.producteur import Producteur
from Metier.demiJour import DemiJour
from Metier.acteur import Acteur

class TestProducteur(unittest.TestCase):

    # Creation de demiJours
    dj1 = DemiJour(3, "Mardi M")
    dj2 = DemiJour(4, "Mardi AM")
    dj3 = DemiJour(7, "Jeudi M")
    dj4 = DemiJour(10, "Vendredi AM")

    # Creation de producteurs
    producteur0 = Producteur(35.31654, 132.3155, 50.2, [dj1, dj3], [producteur1])
    producteur1 = Producteur(-146.34687, -34.3454, 57.8, [dj2], [])
    producteur2 = Producteur(164.35468, 34.534454, 20.4, [dj3, dj4], [producteur0, producteur1])

    def test_addPartner(self):
        result = Producteur.addPartner(TestProducteur.producteur1, TestProducteur.producteur0)
        self.assertIn(TestProducteur.producteur0, TestProducteur.producteur1.partners)

    def test_removePartner(self):
        result = Producteur.removePartner(TestProducteur.producteur2, TestProducteur.producteur0)
        self.assertNotIn(TestProducteur.producteur0, TestProducteur.producteur2.partners)

    def test_affichageInfos(self):
        result = Producteur.__str__(TestProducteur.producteur0)
        self.assertEqual(result, "Producteur 0 : \nCoordonnées : (35.316540 ; 132.315500) \nCapacité : 50.2 kg \nPartenaires : producteurs 1")

    def test_affichageSimple(self):
        result = Producteur.__repr__(TestProducteur.producteur1)
        self.assertEqual(result, "Producteur 1")

if __name__ == '__main__':
    unittest.main()