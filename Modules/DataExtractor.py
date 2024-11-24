# Créé par leleo, le 18/11/2024 en Python 3.7
from csv import reader

class DataExtractor:
    def __init__(self, chemin_vers_fichier:str, delimiteur=" "):
        self.chemin_vers_fichier = chemin_vers_fichier
        self.delimiteur = delimiteur

    def extraction(self) -> list:
        # Utilise reader qui retourne un objet de type readerObject
        # Dois renvoyer une liste de liste
        try:
            with open(self.chemin_vers_fichier, "r") as fichier:
                lignes = (l.strip() for l in fichier)
                lecteur = reader(lignes, delimiter = self.delimiteur)
                # On utilise une liste par compréhension pour convertir le reader
                # en liste et itérer sur chaque ligne
                tabFichier = [l for l in lecteur]
                return tabFichier
        except FileNotFoundError:
            print(f"Le fichier {self.chemin_vers_fichier} n'existe pas")
            return []