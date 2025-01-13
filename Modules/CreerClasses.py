from Interface.MessageErreurSolution import MessageErreurSolution
from Modules.Convertisseur import Convertisseur

from Metier.acteur import Acteur
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
        self.__convertisseur = Convertisseur()

        # Pour vérifier que toutes les commandes de la tournée sont livrées
        self.chargeCumulee = self.__convertisseur.float_to_decimal(0)
        # On conserve les tâches pick-up dans un dictionnaire pour s'assurer que
        # toutes les commandes à délivrer ont été récupérées
        self.taches_P = {}
        # Si l'utilisateur dit qu'il veut continuer à charger le fichier solution malgré la présence d'au moins une erreur
        # Alors, pour les performances, on n'effectue plus de vérification et on génère les tournées jusqu'à la fin.
        self.afficherErreur = True
        # {erreur : compteur de l'erreur}
        self.erreurs = {"charge" : 0, "drop_pick" : 0, "acteurs" : 0, "demi_jour" : 0}
        self.nb_total_erreurs = 0
        self.message_erreur = MessageErreurSolution()



    def load_donnees(self, fichier : list):
        """
        Création des instances de Producteur et Client avec les méthodes privées
        `__creerProducteurs` et `__creerClients`
        Booléen self.donnees_loaded garantit l'unique instanciation des producteurs et des clients
        :param fichier:
        :return: void
        """
        if not self.donnees_loaded:
            Acteur.deleteAll()
            Client.nb = 0
            Producteur.nb = 0
            Demande.deleteAll()
            self.__creerProducteurs(fichier)
            self.__creerClients(fichier)
            self.donnees_loaded = True


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


    def getTournees(self, fichier : list, nom_fichier:str) -> list:
        """
        Pas d'unique instanciation comme pour le fichier de données,
        car plusieurs fichiers solution sont sélectionnables pour un projet
        :param fichier: list
        :return: la liste des Tournees du fichier donné.
        """
        Tournee.deleteAll()
        self.tournees = []
        self.__creerTournees(fichier, nom_fichier)
        if not self.afficherErreur:
            self.message_erreur.afficher_information_nb_erreurs(nom_fichier, self.nb_total_erreurs)
        self.chargeCumulee = self.__convertisseur.float_to_decimal(0)
        self.afficherErreur = True
        self.erreurs = {"charge": 0, "drop_pick": 0, "acteurs": 0, "demi_jour": 0}
        self.nb_total_erreurs = 0
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


    def __creerTache(self, ligne : list):
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

            # Pour les vérifications de conformité
            self.chargeCumulee += self.__convertisseur.float_to_decimal(charge)
            self.taches_P[(info_requete, lieu)] = (lieu, info_requete)

        else:
            acteurs = []
            acteurs.extend(self.producteurs)
            acteurs.extend(self.clients)
            lieu = acteurs[int(ligne[2])]
            info_requete = self.producteurs[int(ligne[3])]

            self.chargeCumulee -= self.__convertisseur.float_to_decimal(charge)
            if (lieu, info_requete) not in self.taches_P:
                self.erreurs["drop_pick"] += 1
                self.nb_total_erreurs += 1

        horaire = ligne[4]

        if lieu not in Acteur.instances.values() or info_requete not in Acteur.instances.values():
            self.erreurs["acteurs"] += 1
            self.nb_total_erreurs += 1

        return Tache(type, charge, lieu, info_requete, horaire)


    def __creerTournees(self, fichier : list, nom_fichier : str):
        """
        Méthode privée qui crée les tournées associées au fichier
        :param fichier : liste de lignes
        :return: void, car les attributs de classe sont directement modifiés
        """

        if fichier:
            # Pour chaque tournée du fichier, on conserve son numéro
            for tournee in fichier:

                producteur = self.producteurs[int(tournee[0][0])]
                numDemiJour = int(tournee[0][1])
                demiJour = DemiJour(numDemiJour)

                # On vérifie que le producteur est disponible pour la tournée
                self.__comparer_dispos(numDemiJour, producteur.dispos)
                # On vérifie que les acteurs sont disponibles pour la tournée
                for t in tournee[1]:
                    acteur = (Acteur.instances[int(t)])
                    self.__comparer_dispos(numDemiJour, acteur.dispos)

                liste_taches = []
                for j in range (2, len(tournee)):
                    tache = self.__creerTache(tournee[j])
                    liste_taches.append(tache)

                # On vérifie que toutes les commandes ont été livrées
                if self.chargeCumulee != 0:
                    self.erreurs["charge"] += 1
                    self.nb_total_erreurs += 1

                self.tournees.append(Tournee(demiJour, producteur, liste_taches))

                if self.nb_total_erreurs > 0 and self.afficherErreur :
                    # Demande à l'utilisateur s'il souhaite continuer le chargement du fichier en dépit des erreurs
                    continuer = self.message_erreur.afficher_question_erreur(nom_fichier, self.erreurs)
                    if not continuer:
                        Tournee.deleteAll()
                        self.tournees = []
                        self.message_erreur.afficher_annulation()
                        break
                    else:
                        self.afficherErreur = False



    def __comparer_dispos(self, jour:int, listeDispos:list):
        liste_jours = []
        for d in listeDispos:
            liste_jours.append(d.num)
        if jour not in liste_jours:
            self.erreurs["demi_jour"] += 1
            self.nb_total_erreurs += 1