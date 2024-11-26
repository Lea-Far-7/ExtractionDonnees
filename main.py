from Modules.CreerClasses import CreerClasses
from Modules.FileManager import FileManager
from Modules.DataExtractor import DataExtractor

print("Récupération des fichiers du dossier Donnees")
manager = FileManager("Donnees")
liste = manager.lister_fichiers()
print(liste)
print("-------------------------")

# On remplace l'input par la sélection du fichier avec les boutons par l'utilisateur
indice = int(input("Choisissez le fichier")) # Donner 0, il n'y a qu'un fichier pour le test
fichier = liste[indice]

# On extrait les données du fichier
extractor = DataExtractor("Donnees\\" + fichier)
donnees = extractor.extraction()
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