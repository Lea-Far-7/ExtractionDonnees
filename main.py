from Modules.CreerClasses import CreerProducteursClients
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

createur = CreerProducteursClients(donnees)
liste_producteurs = createur.creerProducteurs()
liste_clients = createur.creerClients()

# Si on veut le producteur n°2 par exemple
print(liste_producteurs[1])

# Si on veut le client n°1 par exemple
print(liste_clients[0])

"""
Verifier dans les dispos addDispos si la dispos n'est pas déjà dans la liste
Le numéro des clients est celui des acteurs, il n'est pas différencié !!
"""

"""
Est-ce qu'on fait une interface ? Genre Createur avec methode create implémenté par CreateurProducteurs et CreateurClient
Les noms d'interfaces sont préfixés par un I donc: ICreator
"""