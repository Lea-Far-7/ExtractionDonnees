from acteur import Acteur


class Client(Acteur):

    nb = 0 # nombre d'instances de Client

    def __init__(self, latitude:float, longitude:float, dispos=[]):
        super().__init__(latitude,longitude,dispos)
        Client.nb += 1

    def __str__(self)->str:
        result = "Client " + str(self.id) + " :"
        result += "\n\tCoordonnées : (" + str(self.latitude) + " ; " + str(self.longitude) + ")"
        result += "\n\tDispos : "
        for dispo in self.dispos:
            result += "\n\t\t" + str(dispo)
        return result
