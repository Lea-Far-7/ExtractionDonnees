import unittest
from unittest import result

import self

from Modules import filtres
from Modules.filtres import filtreTournees
from Metier.demiJour import DemiJour
from Metier.client import Client
from Metier.producteur import Producteur
from Metier.tache import Tache
from Metier.tournee import Tournee



class TestFiltre(unittest.TestCase):

    # TODO : Créer des objets métiers (j'ai mis 3 mais on peut en faire plus ou moins selon les besoins des tests)
    # TODO : Créer 3 objets DemiJour

    dj1 = DemiJour(2, "Lundi AM")
    dj2 = DemiJour(7, "Jeudi M")
    dj3 = DemiJour(4, "Mardi AM")
    dj4 = DemiJour(9, "Vendredi M")
    dj5 = DemiJour(3, None)
    dj6 = DemiJour(10, "Vendredi AM")
    
    # TODO : Créer 3 objets Clients avec les DemiJour créés avant en dispo (pas tous)

    client0 = Client(16664646464.46466, 1354653341.46464213, [dj2,dj5])
    client1 = Client(364683356.667846, 3456464.345433, [dj1])
    client2 = Client(3336764.46436643, 43453443.6454364, [dj4, dj2])
    
    # TODO : Créer 3 objets Producteurs avec les DemiJour créés avant en dispo (pas tous), pas besoin de spécifier partners

    producteur3 = Producteur(345465456.3346546, 3136546.361565, 120.34, [dj1, dj4])
    producteur4 = Producteur(12464654.646498465, 34646544.3464677, 50.65, [dj2, dj4])
    producteur5 = Producteur(56454346.2346, 545434346.13456, 26.1, [dj1, dj3, dj6])
    
    # TODO : Créer 3 objets Tache avec les Producteurs et Clients créés avant

    tache1 = Tache("P", 57.2, producteur5, client1, "10h")
    tache2 = Tache("D", 45.98, client2, producteur4, "16h")
    tache3 = Tache("D", 89.1, client0, producteur4, "11h")
    tache4 = Tache("P", 23.2, producteur3, client1, "14h")
    tache5 = Tache("P", 38.56, producteur5, client0, "9h")
    
    # TODO : Créer 3 objets Tournees avec pour chacune un DemiJour, un Producteur et au moins une des Taches créées avant

    tournee0 = Tournee(dj2, producteur5, [tache1])
    tournee1 = Tournee(dj4, producteur4, [tache3, tache5])
    tournee2 = Tournee(dj3, producteur3, [tache4, tache1])

    # TODO : Pour la suite il faut au moins avoir lu la documentation de la fonction filtreTournees dans Modules/filtres.py


    def test_filtre_client(self):

        # Test du filtrage selon des clients

        # TODO : Faire appel à la fonction filtreTournees() avec en paramètres la liste des tournées créées et une liste de plusieurs ID de Client
        # result = filtreTournees(listeTournees, None, listeIdClient, None)

        resultA = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [], [1, 2], [])
        resultB = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [], [0, 2], [])

        # TODO : Effectuer une assertion pour vérifier si le résultat de l'appel à la fonction est conforme à ce qui devrait être obtenu
        #  Il faut donc déterminer les tournées qui correspondent aux critères de filtrage (ici les ID des Clients choisis)
        #  La plupart du temps pour les tests on utilise assertEqual(a,b)
        #  Mais ici on veut comparer 2 listes d'objets indépendamment de l'ordre, on utilise donc assertCountEqual(list1,list2)
        #self.assertCountEqual(result, listeTourneesAttendues)

        self.assertCountEqual(resultA, [TestFiltre.tournee0, TestFiltre.tournee2])
        self.assertCountEqual(resultB, [TestFiltre.tournee1])

        # TODO : On peut éventuellement faire plusieurs tests avec des filtrages différents sur les Clients





    def test_filtre_producteur(self):

        # Test du filtrage selon des producteurs

        # TODO : Adapter ce qui a été fait avant pour tester cette fois-ci le filtrage par producteur

        resultA = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [3,5], [], [])
        resultB = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [3,4], [], [])

        self.assertCountEqual(resultA, [TestFiltre.tournee0, TestFiltre.tournee1])
        self.assertCountEqual(resultB, [TestFiltre.tournee1, TestFiltre.tournee2])





    def test_filtre_demiJour(self):

        # Test du filtrage selon des demi-journées

        # TODO : Adapter ce qui a été fait avant pour tester cette fois-ci le filtrage par demi-jours

        resultA = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [], [], [1,3])
        resultB = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [], [], [2,4,5])

        self.assertCountEqual(resultA, [TestFiltre.tournee0, TestFiltre.tournee1])
        self.assertCountEqual(resultB, [TestFiltre.tournee2])





    def test_filtre_all(self):

        # Test du filtrage selon des clients, producteurs et demi-journées

        # TODO : Adapter ce qui a été fait avant pour tester cette fois-ci le filtrage sur tout
        #  Les tournées doivent maintenant respecter 3 contraintes (sur Clients, Producteurs, demiJour) pour être prise en compte

        resultA = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [3,4], [0,2], [1,3])
        resultB = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [3,5], [1,2], [2,4,5])

        self.assertCountEqual(resultA, [TestFiltre.tournee1])
        self.assertCountEqual(resultB, [TestFiltre.tournee0])





    def test_filtre_nothing(self):

        # Test du filtrage sans

        # TODO : On doit vérifier qu'on obtient bien la même liste de Tournee avant et après filtrage

        result = filtres.filtreTournees([TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2], [], [], [])

        self.assertCountEqual(result, [TestFiltre.tournee0, TestFiltre.tournee1, TestFiltre.tournee2])





if __name__ == '__main__':
    unittest.main()
