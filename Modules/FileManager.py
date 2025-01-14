from os import listdir, path, makedirs
from time import strftime, gmtime

"""
    Cette classe regroupe toutes les opérations concernant la recherche et la manipulation de fichiers
"""

class FileManager :

    def __init__(self):
        pass

    def lister_fichiers(self, repertoire : str) -> list:
        try:
            # Récupère tous les éléments dans le répertoire
            contenu_repertoire = listdir(repertoire)
            # Filtrage pour ne garder que les fichiers
            fichiers = [f for f in contenu_repertoire if path.isfile(path.join(repertoire, f))]
            return fichiers
        except FileNotFoundError:
            print(f"Le répertoire {repertoire} n'existe pas.")
            return []

    def lister_dossiers(self, repertoire : str) -> list:
        try:
            # Récupère tous les éléments dans le répertoire
            contenu_repertoire = listdir(repertoire)
            # Filtrage pour ne garder que les dossiers
            dossiers = [d for d in contenu_repertoire if path.isdir(path.join(repertoire, d))]
            return dossiers
        except FileNotFoundError:
            print(f"Le répertoire {repertoire} n'existe pas.")
            return []


    def creer_repertoire(self, repertoire):
        # Crée le répertoire fourni s'il n'existe pas déjà
        makedirs(repertoire, exist_ok=True)

    def creer_chemin_fichier(self, repertoire):
        # Crée une chaîne de caractères contenant le chemin vers un nouveau fichier
        # Dont le nom a la forme : capture_AAAAmmdd_hhs.png
        return path.join(repertoire, "capture_{}.png".format(strftime("%Y%m%d_%H%M%S", gmtime())))