from Modules.CreerClasses import CreerClasses
from Modules.FileManager import FileManager
from Modules.DataExtractor import DataExtractor

# Pour la version où les dossiers sont organisés en projets
manager = FileManager()
liste = manager.lister_dossiers("Projets")
print(liste)

chemin = "Projets\\" + liste[0] + "\Solutions"
liste = manager.lister_fichiers(chemin)
print(liste)

print("Récupération des fichiers du dossier Projet_1")
liste = manager.lister_fichiers("Projets\Projet_3")
print(liste)
print("-------------------------")

# Le user sélectionne un projet dans la liste -> renvoie "Projet_1
# S'affiche le fichier de données à gauche -> fonction qui retourne les (le) fichiers du dossier "Projet_1"
# S'affiche à droite les fichiers du sous-dossier solutions -> fonction qui retourne les(le) fichier du dossier
# En fait, on garde la fonction mais on oblige la récupération que des fichiers et on prend le nom en paramètre.
# Faire une variable qui créé le chemin avec le projet choisi
# Faire une variable statique dans la classe qui utilise la fonction pour "Projets" et "Solutions"


# On remplace l'input par la sélection du fichier avec les boutons par l'utilisateur
indice = int(input("Choisissez le fichier")) # Donner 0, il n'y a qu'un fichier pour le test
fichier = liste[indice]
print()

# On extrait les données du fichier
extractor = DataExtractor()
donnees = extractor.extraction("Projets\Projet_3\\" + fichier)
print(donnees)
print("-------------------------")

# On fournit une liste de liste au créateur de classes
# Il prend le premier élément qui est le nb de producteurs et de clients et créé les bornes
# Il parcourt la liste de l'indice 1 à nb_producteurs +1
# Il créé à chaque itération un nouvel objet Producteur dans lequel il place les différents arguments
# Il fait de même en parcourant les éléments à partir de l'indice nb_clients à la fin.
# Il créé une instance Client à chaque itération en mettant les bons arguments

createur = CreerClasses(donnees)
liste_producteurs = createur.getProducteurs()
liste_clients = createur.getClients()
liste_demandes = createur.getDemandes()

# Si on veut le producteur n°1 par exemple (sachant qu'ils vont de producteur 0 à 4
print(liste_producteurs[1])
print("-------------------------")

# Si on veut le client n°5 par exemple (sachant qu'ils vont de 5 à 9)
print(liste_clients[0])
print("-------------------------")

# Si on veut afficher toutes les demandes
for demande in liste_demandes:
    print(demande)
print("-------------------------")

# Extraction fichier solution
donnees = extractor.extraction("Projets/Projet_3/Solutions/routes_1_pt.txt")
for ligne in donnees:
    print(ligne)