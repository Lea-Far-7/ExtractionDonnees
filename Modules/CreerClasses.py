from Metier.producteur import Producteur
from Metier.client import Client
from Metier.demiJour import DemiJour

"""
Cette classe doit créer les instances de producteurs et de clients présents dans le fichier concerné.
Le fichier est fourni à la classe sous forme de liste de listes. Chaque sous-liste correspondant à une ligne du fichier.
Et chaque ligne du fichier étant un producteur ou un client
"""

class CreerProducteursClients:

    def __init__(self, fichier : list):
        self.fichier = fichier
        self.producteurs = []
        self.clients = []

    """
    Cette méthode retourne la liste des Producteur présents dans le fichier.
    """
    def creerProducteurs(self) -> list:

        nbProducteurs = self.getNbProducteurs()
        # Les partenaires sont une liste de Prodcteurs.
        # Ceux-ci ne sont pas encore créés, on va donc stocker leurs numéros dans une liste temporaire
        partners_tempo = []

        # On parcourt le fichier de la première ligne au nombre de producteurs + 1

        for i in range(1, nbProducteurs + 1):
            # On récupère la ligne courante
            producteur = self.fichier[i]
            # On crée une variable indice comme pointeur que l'on va incrémenter
            # au fur et à mesure de l'avancée dans la ligne.
            indice = 0

            # Les informations récupérées étant des chaînes de caractères, il est nécessaire de les convertir
            latitude = float(producteur[indice])
            indice += 1
            longitude = float(producteur[indice])
            indice += 1

            nbDispos = int(producteur[indice])
            indice += 1
            dispos = []

            for jour in range(indice, nbDispos + indice):
                dispos.append( DemiJour(int (producteur[jour]) ) )

            indice += nbDispos

            capacity = float(producteur[indice])
            indice += 1

            nbPartners = int(producteur[indice])
            indice += 1
            partners_tempo.append([producteur[p] for p in range(indice, nbPartners + indice)])

            # On crée le producteur avec une liste de partenaires vide pour l'instant
            self.producteurs.append(Producteur(latitude, longitude, capacity, dispos, []))

        # On sort de la boucle, tous les producteurs sont créés
        # On va remplir les listes de partenaires actuellement vides
        # On utilise un zip qui associe les éléments de même indice entre deux entités itérables
        # Ici, le producteur n avec la liste de partenaires n
        for prod, partners_ids in zip(self.producteurs, partners_tempo):
            # On accède au paramètre partners du Producteur
            # et on lui assigne la liste par compréhension des Producteurs désignés
            prod.partners = [self.producteurs[int(id)] for id in partners_ids]

        return self.producteurs

    """
    Cette méthode retourne la liste des Client présents dans le fichier.
    """
    def creerClients(self) -> list:

        # indice de la première ligne de client = nombre de producteurs + 1
        debutClients = self.getNbProducteurs() + 1

        # On parcourt le fichier de debutClients à la fin du fichier
        for i in range(debutClients, len(self.fichier)):
            client = self.fichier[i]
            # On crée une variable indice comme pointeur que l'on va incrémenter
            # au fur et à mesure de l'avancée dans la ligne.
            indice = 0

            latitude = float(client[indice])
            indice += 1
            longitude = float(client[indice])
            indice += 1

            nbDispos = int(client[indice])
            indice += 1
            dispos = []

            for jour in range(indice, nbDispos + indice):
                dispos.append( DemiJour(int (client[jour]) ) )

            indice += nbDispos

            self.clients.append(Client(latitude, longitude, dispos))

            """
            Implémenter les demands
            """

        return self.clients

    def getNbProducteurs(self) -> "int" :
        # On regarde combien de lignes sont des producteurs
        if self.fichier:
            # La première ligne du fichier correspond au nombre de producteurs et de clients
            nbProducteurs = int(self.fichier[0][0])
        else:
            # Si le fichier (la liste) est vide
            nbProducteurs = 0
        return nbProducteurs