from Metier.producteur import Producteur
from Metier.client import Client

class Demande:

    """
    Classe représentant la commande d'un **Client** à un **Producteur** d'une certaine quantité.

    L'attribut de classe **instances** permet de récupérer la liste des instances créées.
    Et **nb** le nombre d'instances créées.
    """

    nb = 0  # nombre d'instances de Demande
    instances = []  # instances créées de Demande

    def __init__(self, client:Client, producteur:Producteur, masse:float):
        """
        Initialise la demande.
        :param Client client: Client formulant la demande.
        :param Producteur producteur: Producteur répondant à la demande.
        :param float masse: Quantité demandée en kg.
        """
        self.idDemande = Demande.nb
        self.masse = masse
        self.client = client
        self.producteur = producteur
        Demande.instances.append(self)
        Demande.nb += 1

    def __del__(self):
        """
        Détruit la demande.
        """
        Demande.nb -= 1

    def __str__(self)->str:
        """
        Affiche les informations sur la demande.
        """
        return ("Demande "+ str(self.idDemande) + " : " + str(self.masse) + " kg"
                + " de Client " + str(self.client.id)
                + " à Producteur " + str(self.producteur.id))

    @classmethod
    def deleteAll(cls):
        """
        Efface toutes les instances de Demande.
        """
        cls.instances.clear()
        cls.nb = 0

    @classmethod
    def getNbDemandesActeurs(cls)->dict:
        """
        Calcule le nombre de demandes pour chaque acteur (client et producteur).
        Si un acteur est absent du dictionnaire renvoyé, aucune demande n'est liée à lui.
        :return: Dictionnaire avec pour clés des Acteurs et pour valeurs les nombres de demandes qui lui sont liées.
        """
        result = {}
        for demande in cls.instances:
            if demande.producteur in result:
                result[demande.producteur] += 1
            else:
                result[demande.producteur] = 1
            if demande.client in result:
                result[demande.client] += 1
            else:
                result[demande.client] = 1
        return result