import unittest
from Modules import filtres
from Metier.demiJour import DemiJour
from Metier.client import Client
from Metier.producteur import Producteur
from Metier.tache import Tache
from Metier.tournee import Tournee


class TestFiltre(unittest.TestCase):
    dj1 = DemiJour(2, "Lundi AM")
    dj2 = DemiJour(7, "Jeudi M")
    dj3 = DemiJour(4, "Mardi AM")
    dj4 = DemiJour(9, "Vendredi M")
    dj5 = DemiJour(3, None)
    dj6 = DemiJour(10, "Vendredi AM")

    client0 = Client(16.46466, -135.46464213, [dj2, dj5])
    client1 = Client(36.667846, 145.345433, [dj1])
    client2 = Client(33.46436643, -43.6454364, [dj4, dj2])

    producteur3 = Producteur(14.3346546, -113.361565, 120.34, [dj1, dj4])
    producteur4 = Producteur(24.646498465, 134.3464677, 50.65, [dj2, dj4])
    producteur5 = Producteur(56.2346, -54.13456, 26.1, [dj1, dj3, dj6])

    tache1 = Tache("P", 57.2, producteur5, client1, "10h")
    tache2 = Tache("D", 45.98, client2, producteur4, "16h")
    tache3 = Tache("D", 89.1, client0, producteur4, "11h")
    tache4 = Tache("P", 23.2, producteur3, client1, "14h")
    tache5 = Tache("P", 38.56, producteur5, client0, "9h")

    tournee0 = Tournee(dj2, producteur5, [tache2])
    tournee1 = Tournee(dj4, producteur4, [tache3, tache5])
    tournee2 = Tournee(dj3, producteur3, [tache4, tache1])

    def test_filtre_client(self):
        # Test du filtrage selon des clients

        resultA = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [], [2], [])
        resultB = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [], [0], [])

        self.assertCountEqual(resultA, [TestFiltre.tournee0])
        self.assertCountEqual(resultB, [TestFiltre.tournee1])
        # dans le cas de tournee 2 on ne peux pas le filtrer par client car il en a pas d assoccier

    def test_filtre_producteur(self):
        # Test du filtrage selon des producteurs

        resultA = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [3, 5], [],
                                         [])
        resultB = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [3, 4], [],
                                         [])

        self.assertCountEqual(resultA, [TestFiltre.tournee0, TestFiltre.tournee2])
        self.assertCountEqual(resultB, [TestFiltre.tournee1, TestFiltre.tournee2])

    def test_filtre_demiJour(self):
        # Test du filtrage selon des demi-journées

        resultA = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [], [],
                                         [7, 9])
        resultB = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [], [], [4])

        self.assertCountEqual(resultA, [TestFiltre.tournee0, TestFiltre.tournee1])
        self.assertCountEqual(resultB, [TestFiltre.tournee2])

    def test_filtre_all(self):
        # Test du filtrage selon des clients, producteurs et demi-journées

        resultA = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [4], [0], [9])
        resultB = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [5], [], [7])

        self.assertCountEqual(resultA, [TestFiltre.tournee1])
        self.assertCountEqual(resultB, [TestFiltre.tournee0])

    def test_filtre_nothing(self):
        # Test du filtrage sans

        result = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [], [], [])

        self.assertCountEqual(result, [TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2])


if __name__ == '__main__':
    unittest.main()
