# Créé par leleo, le 18/11/2024 en Python 3.7
from csv import reader

class DataExtractor:
    def __init__(self, delimiteur=" "):
        self.delimiteur = delimiteur

    def extraction(self, chemin_vers_fichier : str) -> list:
        """
        Extraire toutes les lignes d'un fichier en enlevant les espaces inutiles
        > Pour fichiers de données
        :param chemin_vers_fichier:
        :return: une liste de listes (chaque sous-liste étant une ligne du fichier)
        """
        try:
            with open(chemin_vers_fichier, "r") as fichier:
                lignes = (l.strip() for l in fichier) # On retire les espaces de fin de ligne
                lecteur = reader(lignes, delimiter = self.delimiteur) # objet de type readerObject
                # On utilise une liste par compréhension pour convertir le reader en liste et itérer sur chaque ligne
                tabFichier = [l for l in lecteur]
                return tabFichier
        except FileNotFoundError:
            print(f"Le fichier {chemin_vers_fichier} n'existe pas")
            return []


    def extraction_solution(self, chemin_vers_fichier : str) -> list:
        """
        Extraire d'un fichier les lignes qui contiennent des informations utiles
        > Pour fichiers de solutions
        :param chemin_vers_fichier:
        :return: liste de "listes de listes" (chaque sous-sous-liste étant une ligne du fichier et chaque sous-liste une tournée)
        """
        try:
            with open(chemin_vers_fichier, "r") as fichier:
                lignes = fichier.readlines()
                tournees = [] # liste de toutes les tournées
                tournee_en_cours = []

                for ligne in lignes:
                    ligne = ligne.strip() # On retire les espaces de fin de ligne
                    if ligne.startswith("-"): # On est à la fin de la tournée en cours
                        if tournee_en_cours:
                            tournees.append(tournee_en_cours)
                            tournee_en_cours = []
                    elif ligne: # On ignore les lignes vides
                        tournee_en_cours.append(ligne.split(self.delimiteur))
                # On ajoute la dernière tournée si elle n'est pas vide
                if tournee_en_cours:
                    tournees.append(tournee_en_cours)

            return tournees
        except FileNotFoundError:
            print(f"Le fichier {chemin_vers_fichier} n'existe pas")
            return []