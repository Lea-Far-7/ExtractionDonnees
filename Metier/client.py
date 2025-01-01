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
        result += "\nCoordonnées : (" + str(round(self.latitude,6)) + " ; " + str(round(self.latitude,6)) + ")"
        result += "\nDispos : "
        for dispo in self.dispos:
            result += repr(dispo)+", "
        return result[:-2]


    def __repr__(self)->str:
        """Affichage simple"""
        return "Client " + str(self.id)
