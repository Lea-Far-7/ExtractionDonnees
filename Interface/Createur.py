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

    def getDossiers(self) -> list:
        # On utilisera cette fonction seulement pour récupérer les noms de dossiers du dossier Projets
        return self.fileManager.lister_dossiers("..\Projets")

    def getFichiers(self, repertoire : str) -> list:
        # On précisera en paramètre le projet voulu et \Solutions si c'est ce que l'on veut récupérer
        return self.fileManager.lister_fichiers("..\Projets\\" + repertoire)

    def getContenuFichierDonnees(self, chemin_vers_fichier : str) -> list:
        # On précisera en paramètre le projet et le nom du fichier
        return self.extracteur.extraction("..\Projets\\" + chemin_vers_fichier)

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
        return self.extracteur.extraction_solution("..\Projets\\" + self.projet + "\Solutions\\" + nom_fichier)

    def getTournees(self, lignes : list) -> list[Tournee] :
        return self.createur_classes.getTournees(lignes)
        # Avec dictionnaire, si on remplace par un dictionnaire self.solution de interface alors on peut mémoriser les fichiers déjà loaded
        # Param : nom_fichier
        # if nom_fichier in self.solutions_loaded :
        # return self.solutions_loaded[nom_fichier]
        # else:
        # tournees = self.createur_classes.getTournees(lignes)
        # self.solutions_loaded[nom_fichier] = tournees
        # return self.solutions_loaded[nom_fichier]

        # Une fois cela fait, on ne recrée pas les tournées systématiquement

        # Pour modification de self.interface.solution en dictionnaire :

        # Faire modifications nécessaires dans PopupImport : self.fichiers_solutions devient à son tour un dictionnaire
        # Code affecté : boucle choixSolution dans __synchronisation_carte_tableau
        # self.fichiers_solutions[fichier] = (self.createur.getContenuFichierSolution(fichier))
        # liste_dico_fichier_tournees.append(self.createur.getTournees(self.fichiers_solutions[fichier])) -> ancien liste_tournees

        # Dans InterfacePrincipale : lecture dans update_menu_solutions
        # if choix in self.solution:
        # liste_tournees = self.createur.getTournees(self.solution[choix])

        # Dans PopupFiltre :
        # tournees_filtered = filtreTournees(self.createur.getTournees(self.interface.solution[nom_fichier], nom_fichier), producteurs_id, clients_id, demi_jours_num)
        # TODO : comment récupère t-on le nom du fichier dans la classe popupFiltre ? Parce que il peut y avoir plusieurs fichiers sélectionnés et choisis d'être affichés en même temps ?
        # Donc comment savoir sur quel fichier on applique le filtre ?
        # Ou est-ce qu'on l'applique sur tous, auquel cas, on parcours juste le dictionnaire ?

