from Metier.demande import Demande
from Metier.producteur import Producteur
from Metier.client import Client
from Metier.demiJour import DemiJour
from Metier.tache import Tache
from Metier.tournee import Tournee

"""
Cette classe doit créer les instances de producteurs et de clients présents dans le fichier concerné.
Le fichier est fourni à la classe sous forme de liste de listes. Chaque sous-liste correspondant à une ligne du fichier.
Et chaque ligne du fichier étant un producteur ou un client.
"""

class CreerClasses:

    def __init__(self):
        self.producteurs = []
        self.clients = []
        self.demandes = []
        self.tournees = []
        self.donnees_loaded = False
        self.solutions_loaded = False


    def load_donnees(self, fichier : list):
        """
        Création des instances de Producteur et Client avec les méthodes privées
        `__creerProducteurs` et `__creerClients`
        Booléen self.donnees_loaded garantit l'unique instanciation des producteurs et des clients
        :param fichier:
        :return: void
        """
        if not self.donnees_loaded:
            self.__creerProducteurs(fichier)
            self.__creerClients(fichier)
            self.donnees_loaded = True


    def load_solutions(self, fichier : list):
        """
        Création des instances de Tournee avec la méthode privée
        `__creerTournees`
        Booléen self.solutions_loaded garantit l'unique instanciation des tournées
        :param fichier:
        :return: void
        """
        if not self.solutions_loaded:
            self.__creerTournees(fichier)
            self.solutions_loaded = True


    def getProducteurs(self) -> "list" :
        """
        :return: La liste des Producteurs
        """
        return self.producteurs


    def getClients(self) -> "list" :
        """
        :return: La liste des Clients
        """
        return self.clients


    def getDemandes(self) -> "list" :
        """
        :return: la liste des Demandes
        """
        return self.demandes


    def getTournees(self) -> list:
        """
        :return: la liste des Tournees
        """
        return self.tournees


    def getNbProducteurs(self) -> "int" :
        """
        :return: le nombre de producteurs créés
        """
        return len(self.producteurs)


    def getNbClients(self) -> "int" :
        """
        :return: le nombre de clients créés
        """
        return len(self.clients)


    def __creerProducteurs(self, fichier : list):
        """
        Méthode privée qui crée les producteurs associés au fichier (lignes 1 à nbProducteurs)
        :return: void car les attributs de classe sont directement modifiés
        """

        if fichier:
            nbProducteurs = int(fichier[0][0])
            # Les partenaires sont une liste de Prodcteurs.
            # Ceux-ci ne sont pas encore créés, on va donc stocker leurs numéros dans une liste temporaire
            partners_tempo = []

            # On parcourt le fichier de la première ligne au nombre de producteurs + 1

            for i in range(1, nbProducteurs + 1):
                # On récupère la ligne courante
                producteur = fichier[i]
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


    def __creerClients(self, fichier : list):
        """
        Méthode privée qui crée les clients associés au fichier (lignes nbProducteurs+1 à la fin)
        :return: void car les attributs de classe sont directement modifiés
        """

        if fichier:
            debutClients = int(fichier[0][0]) + 1

            # On parcourt le fichier de debutClients à la fin du fichier
            for i in range(debutClients, len(fichier)):
                client_en_cours = fichier[i]
                # On crée une variable indice comme pointeur que l'on va incrémenter
                # au fur et à mesure de l'avancée dans la ligne.
                indice = 0

                latitude = float(client_en_cours[indice])
                indice += 1
                longitude = float(client_en_cours[indice])
                indice += 1

                nbDispos = int(client_en_cours[indice])
                indice += 1
                dispos = []

                for jour in range(indice, nbDispos + indice):
                    dispos.append( DemiJour(int (client_en_cours[jour]) ) )

                indice += nbDispos

                client = Client(latitude, longitude, dispos)
                self.clients.append(client)

                for j in range(len(self.producteurs)):
                    masse = float(client_en_cours[indice + j])
                    if masse > 0:
                        producteur = self.producteurs[j]
                        self.demandes.append(Demande(client, producteur, masse))


    def __creerTache(self, ligne):
        """
        Parcours la ligne et récupère les informations nécessaires à la création d'une tâche
        :param ligne: liste
        :return: Une Tache
        """

        nbProducteurs = self.getNbProducteurs()
        type = ligne[0]
        charge = float(ligne[1])
        if type == 'P':
            lieu = self.producteurs[int(ligne[2])]
            # Numero premier client commence à nbProducteurs
            # Indice premier client = numClient - nbProducteurs
            info_requete = self.clients[int(ligne[3])-nbProducteurs]
        else:
            lieu = self.clients[int(ligne[2]) - nbProducteurs]
            info_requete = self.producteurs[int(ligne[3])]
        horaire = ligne[4]

        return Tache(type, charge, lieu, info_requete, horaire)


    def __creerTournees(self, fichier):
        """
        Méthode privée qui crée les tournées associées au fichier
        :param fichier:
        :return: void, car les attributs de classe sont directement modifiés
        """

        if fichier:
            # Pour chaque tournée du fichier, on conserve son numéro
            for i, tournee in enumerate(fichier):
                producteur = self.producteurs[int(tournee[0][0])]
                demiJour = DemiJour(int(tournee[0][1]))
                liste_taches = []

                # ligne 1 = liste des nœuds visités = pas utile

                """
                type = tournee[2][0]
                charge = float(tournee[2][1])
                if type == 'P':
                    lieu = self.producteurs[int(tournee[2][2])]
                    info_requete = self.clients[int(tournee[2][3])]
                else:
                    lieu = self.clients[int(tournee[2][2])]
                    info_requete = self.producteurs[int(tournee[2][3])]
    
                horaire = tournee[2][4]
                """
                for j in range (2, len(tournee)):
                    tache = self.__creerTache(tournee[j])
                    liste_taches.append(tache)

                self.tournees.append(Tournee(demiJour, producteur, liste_taches))