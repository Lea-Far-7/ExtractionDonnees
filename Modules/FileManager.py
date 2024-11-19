# Créé par leleo, le 18/11/2024 en Python 3.7
from os import listdir, path

"""
    Cette classe regroupe toutes les opérations concernant la recherche de fichiers
    -> lister_fichiers : renvoie une liste des noms des fichiers d'un répertoire donné
"""

class FileManager :

    def __init__(self, chemin_vers_repertoire):
        self.repertoire = chemin_vers_repertoire

    def lister_fichiers(self):
        try:
            contenu_repertoire = listdir(self.repertoire)
            # Filtrer pour ne garder que les fichiers
            #fichiers = [f for f in contenu if path.isfile(path.join(repertoire, f))]
            #return fichiers
            return contenu_repertoire
        except FileNotFoundError:
            print(f"Le répertoire {self.repertoire} n'existe pas.")
            return []

"""
import os

directory = 'Donnees'


for entry in os.scandir(directory):
    if entry.is_file() and entry.name.endswith('.txt'):
        print(entry.name)
"""