from Metier.client import Client
from Metier.demande import Demande
from Metier.producteur import Producteur
from Metier.tournee import Tournee
from Modules.CreerClasses import CreerClasses
from Modules.DataExtractor import DataExtractor
from Modules.FileManager import FileManager


class Createur:

    def __init__(self):
        self.fileManager = FileManager()
        self.extracteur = DataExtractor()
        self.createur_classes = CreerClasses()

        self.projet = "" # Permet de créer une instance CreerClasses pour chaque projet
        self.solutions_loaded = {}
        # Voir pour faire un dictionnaire de dictionnaire avec {projet : {nom_fichier : liste de tournees}}

    def getDossiers(self) -> list:
        # On utilisera cette fonction seulement pour récupérer les noms de dossiers du dossier Projets
        return self.fileManager.lister_dossiers("Projets")

    def getFichiers(self, repertoire : str) -> list:
        # On précisera en paramètre le projet voulu et \Solutions si c'est ce que l'on veut récupérer
        return self.fileManager.lister_fichiers("Projets\\" + repertoire)

    def getContenuFichierDonnees(self, chemin_vers_fichier : str) -> list:
        # On précisera en paramètre le projet et le nom du fichier
        print(self.extracteur.extraction("Projets\\" + chemin_vers_fichier))
        return self.extracteur.extraction("Projets\\" + chemin_vers_fichier)

    def getActeurs(self, lignes : list, projet : str) -> (list[Producteur], list[Client]) :
        # Avec la création unique des instances de la classe CreerClasses
        # On doit détecter lorsque le projet sélectionné a changé et créer une nouvelle instance.
        if self.projet != projet :
            self.projet = projet
            self.solutions_loaded = {}
            self.createur_classes = CreerClasses()
            self.createur_classes.load_donnees(lignes)
            return self.createur_classes.getProducteurs(), self.createur_classes.getClients()
        return self.createur_classes.getProducteurs(), self.createur_classes.getClients()

    def getCommandes(self) -> list[Demande] :
        if self.projet :
            return self.createur_classes.getDemandes()
        return []

    def getContenuFichierSolution(self, nom_fichier : str) -> list:
        # On précisera en paramètre le nom du fichier voulu
        print(self.extracteur.extraction_solution("Projets\\" + self.projet + "\Solutions\\" + nom_fichier))
        return self.extracteur.extraction_solution("Projets\\" + self.projet + "\Solutions\\" + nom_fichier)

    def getTournees(self, lignes : list, nom_fichier) -> list[Tournee] :
        if nom_fichier in self.solutions_loaded:
            return self.solutions_loaded[nom_fichier]
        else:
            tournees = self.createur_classes.getTournees(lignes, nom_fichier)
            if tournees:
                self.solutions_loaded[nom_fichier] = tournees
                print(tournees)
            return tournees