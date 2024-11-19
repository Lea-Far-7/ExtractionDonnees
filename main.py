# Créé par leleo, le 18/11/2024 en Python 3.7

import os
from Modules.FileManager import FileManager
from Modules.DataExtractor import DataExtractor


# Chemins des répertoires
repertoire_donnees = "Donnees"
repertoire_solutions = "Solutions"

file_manager_donnees = FileManager(repertoire_donnees)
file_manager_solutions = FileManager(repertoire_solutions)

liste_fichiers_donnees = file_manager_donnees.lister_fichiers()
liste_fichiers_solution = file_manager_solutions.lister_fichiers()

print("Fichiers dans le répertoire 'Donnees':")
for fichier in liste_fichiers_donnees:
    print(fichier)

print("\nFichiers dans le répertoire 'Solutions':")
for fichier in liste_fichiers_solution:
    print(fichier)

# extraction de données
if liste_fichiers_donnees:
    chemin_fichier = os.path.join(repertoire_donnees, liste_fichiers_donnees[0])
    data_extractor = DataExtractor(chemin_fichier)
    donnees = data_extractor.extraction()
    print("\nDonnées extraites du premier fichier dans 'Donnees':")
    for ligne in donnees:
        print(ligne)

# extraction de solutions
if liste_fichiers_donnees:
    chemin_fichier = os.path.join(repertoire_solutions, liste_fichiers_solution[0])
    data_extractor = DataExtractor(chemin_fichier)
    donnees = data_extractor.extraction()
    print("\nDonnées extraites du premier fichier dans 'Solution':")
    for ligne in donnees:
        print(ligne)