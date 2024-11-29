from Metier.acteur import Acteur


class Client(Acteur):

    """
    Classe représentant un client.

    L'attribut de classe **nb** permet de récupérer le nombre d'instances créées.
    """

    nb = 0 # nombre d'instances de Client

    def __init__(self, latitude:float, longitude:float, dispos=None):
        """
        Initialise le client.
        :param float latitude: Latitude en degrés du client.
        :param float longitude: Longitude en degrés du client.
        :param list[DemiJour] dispos: Liste des **DemiJour** où le client est disponible.
        """
        super().__init__(latitude,longitude,dispos)
        Client.nb += 1

    def __str__(self)->str:
        """
        Affiche les informations sur le client.
        """
        result = "Client " + str(self.id) + " :"
        result += "\n\tCoordonnées : (" + str(self.latitude) + " ; " + str(self.longitude) + ")"
        result += "\n\tDispos : "
        for dispo in self.dispos:
            result += "\n\t\t" + str(dispo)
        return result
