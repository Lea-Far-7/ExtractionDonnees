import unittest

from Metier.client import Client
from Metier.demande import Demande
from Metier.demiJour import DemiJour
from Metier.producteur import Producteur
from Metier.tache import Tache
from Metier.tournee import Tournee
from Modules.CreerClasses import CreerClasses
from Modules.DataExtractor import DataExtractor
from Modules.FileManager import FileManager

class TestDonnees(unittest.TestCase):
    manager = FileManager()
    extractor = DataExtractor()
    createur = CreerClasses()

    nom_fichier_donnees = manager.lister_fichiers("../Projets/Projet_3")[0] # instanceInfos_2.txt
    nom_fichier_solution_bon = manager.lister_fichiers("../Projets/Projet_3/Solutions")[0] # routes_0_pt.txt
    nom_fichier_solution_faux = manager.lister_fichiers("../Projets/Projet_3/Solutions")[3] # routes_2_pt2.txt

    fichier_donnees = extractor.extraction("../Projets/Projet_3/" + nom_fichier_donnees)
    fichier_solution_bon = extractor.extraction_solution("../Projets/Projet_3/Solutions/" + nom_fichier_solution_bon)
    fichier_solution_faux = extractor.extraction_solution("../Projets/Projet_3/Solutions/" + nom_fichier_solution_faux)

    liste_disposP = [DemiJour(num) for num in range(10)]
    dispos_client1 = [2,3,4,5,0,1]
    liste_disposC1 = [DemiJour(num) for num in dispos_client1]
    dispos_client7 = [8,9,0,1]
    liste_disposC7 = [DemiJour(num) for num in dispos_client7]
    dispos_client9 = [6,7,8,9,2,3]
    liste_disposC9 = [DemiJour(num) for num in dispos_client9]

    prod0 = Producteur(47.5088063062821, 0.8066315057392832, 200.0, liste_disposP)
    prod1 = Producteur(364683356.667846, 3456464.345433, 200.0, liste_disposP) #bidon
    prod2 = Producteur(47.490643223533596, 0.3740700174623114, 200.0, liste_disposP)
    prod3 = Producteur(345465456.3346546, 3136546.361565, 120.34, liste_disposP) #bidon
    prod4 = Producteur(47.42499256105147, 0.7950538795010083, 200.0, liste_disposP)

    cl5 = Client(47.41165454791928, 0.8018887634197662, liste_disposC1)
    cl6 = Client(3336764.46436643, 43453443.6454364, liste_disposC1) #bidon
    cl7 = Client(47.3782962603544, 1.0621713144859313, liste_disposC7)
    cl8 = Client(16664646464.46466, 1354653341.46464213, liste_disposC7) #bidon
    cl9 = Client(47.337952003427446, 0.6072525512906997, liste_disposC9)

    com1 = Demande(cl5, prod4, 26.69)

    liste_taches_t1_bon = [Tache('P', 23.22, prod0, cl7, '14:00'),
                           Tache('P', 27.86, prod0, cl9, '14:00'),
                           Tache('D', 23.22, cl7, prod0, '14:20'),
                           Tache('D', 27.86, cl9, prod0, '14:50')]

    liste_taches_t1_faux = [Tache('P', 23.06, prod4, cl7, '14:00'),
                            Tache('P', 23.22, prod4, cl7, '14:00'),
                            Tache('P', 27.86, prod4, cl9, '14:00'),
                            Tache('P', 25.55, prod4, cl9, '14:00'),
                            Tache('D', 23.06, cl7, prod2, '14:17'),
                            Tache('D', 23.22, cl9, prod0, '14:17'),
                            Tache('D', 27.86, cl9, prod0, '14:17'),
                            Tache('D', 25.55, cl9, prod4, '14:47')]

    t1_bon = Tournee(DemiJour(9), prod0, liste_taches_t1_bon)

    t1_faux =Tournee(DemiJour(9), prod4, liste_taches_t1_faux)

    def test_FileManager_dossiers(self):
        # Tests de la recherche et du listage de dossiers

        # Quand il y a uniquement des dossiers dans le répertoire :
        resultA = TestDonnees.manager.lister_dossiers("../Projets")
        # Quand il y a des dossiers et des fichiers dans le répertoire :
        resultB = TestDonnees.manager.lister_dossiers("..\Projets\Projet_1")
        # Quand il n'y a que des fichiers :
        resultC = TestDonnees.manager.lister_dossiers("..\Projets\Projet_2\Solutions")

        self.assertListEqual(resultA, ["Projet_1", "Projet_2", "Projet_3", "Projet_4"],
                             "Test File Manager dossiers uniquement échoué")

        self.assertListEqual(resultB, ["Solutions"],
                             "Test File Manager dossiers et fichiers échoué")

        self.assertListEqual(resultC, [],
                             "Test File Manager aucun dossiers échoué")

    def test_FileManager_fichiers(self):
        # Tests de la recherche et du listage de fichiers

        # Quand il y a uniquement des dossiers dans le répertoire :
        resultA = TestDonnees.manager.lister_fichiers("..\Projets")
        # Quand il y a des dossiers et des fichiers dans le répertoire :
        resultB = TestDonnees.manager.lister_fichiers("..\Projets\Projet_1")
        # Quand il n'y a que des fichiers :
        resultC = TestDonnees.manager.lister_fichiers("..\Projets\Projet_2\Solutions")

        self.assertListEqual(resultA, [],
                             "Test File Manager aucun fichiers échoué")

        self.assertListEqual(resultB, ["exemple.txt"],
                             "Test File Manager dossiers et fichiers échoué")

        self.assertListEqual(resultC, ["routes_0_pt.txt", "routes_1_pt.txt", "routes_2_pt.txt"],
                             "Test File Manager fichiers uniquement échoué")

    def test_DataExtractor(self):
        # Tests des extractions des lignes des fichiers

        # Extraction d'un fichier de données
        resultA = TestDonnees.extractor.extraction("../Projets/Projet_3/" + TestDonnees.nom_fichier_donnees)
        # Extraction d'un fichier solution
        resultB = TestDonnees.extractor.extraction_solution("../Projets/Projet_3/Solutions/" + TestDonnees.nom_fichier_solution_bon)

        self.assertListEqual(resultA[0], ['5', '10'],
                             "Test 1 DataExtractor fichiers de données échoué")

        self.assertListEqual(resultA[1], ['47.5088063062821', '0.8066315057392832', '10', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '200', '3', '4', '1', '3'],
                             "Test 2 DataExtractor fichiers de données échoué")

        self.assertListEqual(resultB[0], [['0', '5'],
                                          ['8', '11', '12', '5'],
                                          ['P', '24.40', '0', '5', '14:00'],
                                          ['P', '29.95', '0', '11', '14:00'],
                                          ['P', '28.44', '0', '8', '14:00'],
                                          ['P', '21.17', '0', '12', '14:00'],
                                          ['D', '28.44', '8', '0', '14:24'],
                                          ['D', '29.95', '11', '0', '14:30'],
                                          ['D', '21.17', '12', '0', '14:52'],
                                          ['D', '24.40', '5', '0', '15:16']],
                             "Test 1 DataExtractor fichiers solution échoué")

        self.assertListEqual(resultB[1], [['0', '9'],
                                          ['7', '9'],
                                          ['P', '23.22', '0', '7', '14:00'],
                                          ['P', '27.86', '0', '9', '14:00'],
                                          ['D', '23.22', '7', '0', '14:20'],
                                          ['D', '27.86', '9', '0', '14:50']],
                             "Test 2 DataExtractor fichiers solution échoué")


    def test_createur_classes_donnees(self):
        # Tests de la création des instances de classe correspondant aux fichiers de données
        TestDonnees.createur.load_donnees(TestDonnees.fichier_donnees)

        # Pour les producteurs :
        resultA = self.createur.getProducteurs()

        # Pour les clients :
        resultB = self.createur.getClients()

        # Pour les commandes :
        resultC = self.createur.getDemandes()

        self.assertEqual(resultA[0].id, TestDonnees.prod0.id, "Test création producteur échoué")
        self.assertEqual(resultB[0].id, TestDonnees.cl5.id, "Test création client échoué")
        self.assertEqual(resultC[0].idDemande, TestDonnees.com1.idDemande, "Test création commande échoué")


    def test_createur_classes_solution(self):
        # Tests de la création des tournées correspondant aux fichiers solution

        # Avec un fichier solution correct :
        resultA = self.createur.getTournees(TestDonnees.fichier_solution_bon, TestDonnees.nom_fichier_solution_bon)

        # Avec un fichier solution contenant des erreurs
        resultB = self.createur.getTournees(TestDonnees.fichier_solution_faux, TestDonnees.nom_fichier_solution_faux)
        resultC = self.createur.getTournees(TestDonnees.fichier_solution_faux, TestDonnees.nom_fichier_solution_faux)

        self.assertEqual(resultA[1].demiJour.num, TestDonnees.t1_bon.demiJour.num)
        # En cliquant sur "Yes" de la MessageBox
        self.assertEqual(resultB[4].demiJour.num, TestDonnees.t1_faux.demiJour.num)
        # En cliquant sur "NO" de la MessageBox
        self.assertEqual(resultC, [])

if __name__ == '__main__':
    unittest.main()


# Le user sélectionne un projet dans la liste -> renvoie "Projet_1"
# S'affiche le fichier de données à gauche -> fonction qui retourne les (le) fichiers du dossier "Projet_1"
# S'affichent à droite les fichiers du sous-dossier solutions -> fonction qui retourne les(le) fichier du dossier
# En fait, on garde la fonction mais on oblige la récupération que des fichiers et on prend le nom en paramètre.
# Faire une variable qui crée le chemin avec le projet choisi
# Faire une variable statique dans la classe qui utilise la fonction pour "Projets" et "Solutions"





# On fournit une liste de liste au créateur de classes
# Il prend le premier élément qui est le nb de producteurs et de clients et créé les bornes
# Il parcourt la liste de l'indice 1 à nb_producteurs +1
# Il créé à chaque itération un nouvel objet Producteur dans lequel il place les différents arguments
# Il fait de même en parcourant les éléments à partir de l'indice nb_clients à la fin.
# Il créé une instance Client à chaque itération en mettant les bons arguments