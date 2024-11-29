# Créé par leleo, le 18/11/2024 en Python 3.7
from os import listdir, path

"""
    Cette classe regroupe toutes les opérations concernant la recherche de fichiers
    -> lister_fichiers : renvoie une liste des noms des fichiers d'un répertoire donné
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
            print(f"Le répertoire {contenu_repertoire} n'existe pas.")
            return []

"""
import os

directory = 'Donnees'
for entry in os.scandir(directory):
    if entry.is_file() and entry.name.endswith('.txt'):
        print(entry.name)
"""