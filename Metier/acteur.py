import abc # pour classe abstraite
from demiJour import DemiJour


class Acteur(abc.ABC):

    nb = 0 # nombre d'instances créées d'Acteur

    def __init__(self, latitude:float, longitude:float, dispos=[]):
        self.id = Acteur.nb
        self.latitude = latitude
        self.longitude = longitude
        self.dispos = dispos
        Acteur.nb += 1

    def addDispo(self, dispo:DemiJour):
        self.dispos.append(dispo)

    def removeDispo(self, dispo:DemiJour):
        self.dispos.remove(dispo)

    @abc.abstractmethod
    def __str__(self)->str:
        pass
