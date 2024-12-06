import unittest

from Modules.filtres import filtreTournees
from Metier.demiJour import DemiJour
from Metier.client import Client
from Metier.producteur import Producteur
from Metier.tache import Tache
from Metier.tournee import Tournee



class TestFiltre(unittest.TestCase):

    # TODO : Créer des objets métiers (j'ai mis 3 mais on peut en faire plus ou moins selon les besoins des tests)
    # TODO : Créer 3 objets DemiJour
    # TODO : Créer 3 objets Clients avec les DemiJour créés avant en dispo (pas tous)
    # TODO : Créer 3 objets Producteurs avec les DemiJour créés avant en dispo (pas tous), pas besoin de spécifier partners
    # TODO : Créer 3 objets Tache avec les Producteurs et Clients créés avant
    # TODO : Créer 3 objets Tournees avec pour chacune un DemiJour, un Producteur et au moins une des Taches créées avant

    # TODO : Pour la suite il faut au moins avoir lu la documentation de la fonction filtreTournees dans Modules/filtres.py


    @unittest.skip # TO DELETE
    def test_filtre_client(self):

        # Test du filtrage selon des clients

        # TODO : Faire appel à la fonction filtreTournees() avec en paramètres la liste des tournées créées et une liste de plusieurs ID de Client
        # result = filtreTournees(listeTournees, None, listeIdClient, None)

        # TODO : Effectuer une assertion pour vérifier si le résultat de l'appel à la fonction est conforme à ce qui devrait être obtenu
        #  Il faut donc déterminer les tournées qui correspondent aux critères de filtrage (ici les ID des Clients choisis)
        #  La plupart du temps pour les tests on utilise assertEqual(a,b)
        #  Mais ici on veut comparer 2 listes d'objets indépendamment de l'ordre, on utilise donc assertCountEqual(list1,list2)
        # self.assertCountEqual(result, listeTourneesAttendues)

        # TODO : On peut éventuellement faire plusieurs tests avec des filtrages différents sur les Clients

        pass # TO DELETE


    @unittest.skip # TO DELETE
    def test_filtre_producteur(self):

        # Test du filtrage selon des producteurs

        # TODO : Adapter ce qui a été fait avant pour tester cette fois-ci le filtrage par producteur

        pass  # TO DELETE


    @unittest.skip # TO DELETE
    def test_filtre_demiJour(self):

        # Test du filtrage selon des demi-journées

        # TODO : Adapter ce qui a été fait avant pour tester cette fois-ci le filtrage par demi-jours

        pass  # TO DELETE


    @unittest.skip # TO DELETE
    def test_filtre_all(self):

        # Test du filtrage selon des clients, producteurs et demi-journées

        # TODO : Adapter ce qui a été fait avant pour tester cette fois-ci le filtrage sur tout
        #  Les tournées doivent maintenant respecter 3 contraintes (sur Clients, Producteurs, demiJour) pour être prise en compte

        pass  # TO DELETE


    @unittest.skip # TO DELETE
    def test_filtre_nothing(self):

        # Test du filtrage sans

        # TODO : On doit vérifier qu'on obtient bien la même liste de Tournee avant et après filtrage

        pass  # TO DELETE



if __name__ == '__main__':
    unittest.main()