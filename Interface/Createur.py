from Metier.client import Client
from Metier.demande import Demande
from Metier.producteur import Producteur
from Metier.tournee import Tournee
from Modules.CreerClasses import CreerClasses
from Modules.DataExtractor import DataExtractor
from Modules.FileManager import FileManager

"""
Cette classe doit servir d'intermédiaire entre les classes d'affichage et les classes qui manipulent directement les données.
Les premières ne doivent jamais appeler directement les dernières.
Elle doit permettre de gérer les instances de classes de données :
-> FileManager : une seule pour l'application
-> DataExtractor : une seule pour l'application
-> CreerClasses : une seule par projet
"""

class Createur:

    def __init__(self):

        self.fileManager = FileManager()
        self.extracteur = DataExtractor()
        self.createur_classes = CreerClasses()

        self.projet = "" # Permet de créer une instance CreerClasses pour chaque projet
        self.solutions_loaded = {} # Sauvegarde les solutions du projet en cours déjà chargées


    def getDossiers(self) -> list:
        """
        On utilisera cette fonction seulement pour récupérer les noms de dossiers du dossier Projets
        :return: La liste des projets
        """
        return self.fileManager.lister_dossiers("Projets")


    def getFichiers(self, repertoire : str) -> list:
        """
        :param repertoire: le projet voulu et \Solutions si l'on veut les fichiers solution
        :return: La liste des fichiers du répertoire donné
        """
        return self.fileManager.lister_fichiers("Projets\\" + repertoire)


    def getContenuFichierDonnees(self, chemin_vers_fichier : str) -> list[list]:
        """
        :param chemin_vers_fichier: le projet \ le nom du fichier
        :return: La liste des lignes du fichier de données
        """
        return self.extracteur.extraction("Projets\\" + chemin_vers_fichier)


    def getActeurs(self, lignes : list, projet : str) -> (list[Producteur], list[Client]) :
        """
        Détecte un changement de projet et crée une nouvelle instance de CreerClasses le cas échéant.
        :param lignes: Liste de lignes
        :param projet: Le nom du projet en cours
        :return: La liste des Producteurs et la liste des Clients
        """
        if self.projet != projet :

            self.projet = projet
            self.solutions_loaded = {}

            self.createur_classes = CreerClasses()
            self.createur_classes.load_donnees(lignes)

            return self.createur_classes.getProducteurs(), self.createur_classes.getClients()

        return self.createur_classes.getProducteurs(), self.createur_classes.getClients()


    def getCommandes(self) -> list[Demande] :
        """
        :return: La liste des commandes si un projet a été sélectionné, une liste vide sinon
        """
        if self.projet :
            return self.createur_classes.getDemandes()
        return []


    def getContenuFichierSolution(self, nom_fichier : str) -> list:
        """
        :param nom_fichier: le nom du fichier solution
        :return: La liste des lignes du fichier solution
        """
        return self.extracteur.extraction_solution("Projets\\" + self.projet + "\Solutions\\" + nom_fichier)


    def getTournees(self, lignes : list, nom_fichier) -> list[Tournee] :
        """
        Prend en compte le dictionnaire des solutions déjà chargées, afin d'éviter l'exécution inutile d'une fonction coûteuse.
        :param lignes: La liste des lignes du fichier solution
        :param nom_fichier: Le nom du fichier solution
        :return: La liste des Tournées
        """
        if nom_fichier in self.solutions_loaded:
            return self.solutions_loaded[nom_fichier]
        else:
            tournees = self.createur_classes.getTournees(lignes, nom_fichier)
            if tournees:
                self.solutions_loaded[nom_fichier] = tournees
            return tournees