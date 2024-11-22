from producteur import Producteur
from client import Client


class Demande:

    nb = 0  # nombre d'instances de Demand

    def __init__(self, client:Client, producteur:Producteur, masse:float):
        self.idDemande = Demande.nb
        self.masse = masse
        self.client = client
        self.producteur = producteur
        Demande.nb += 1

    def __str__(self)->str:
        return ("Demande "+ str(self.idDemande) + " : " + str(self.masse)
                + " de Client " + str(self.client.id)
                + " à Producteur " + str(self.client.id))