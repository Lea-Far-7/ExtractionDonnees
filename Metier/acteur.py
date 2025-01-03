import abc # pour classe abstraite

from Metier.demiJour import DemiJour


class Acteur(abc.ABC):

    """
    Classe abstraite représentant un acteur.

    Elle peut servir à représenter un **Producteur** ou un **Client**.

    L'identifiant d'un Acteur dépend de son ordre d'instanciation.

    L'attribut de classe **nb** permet de récupérer le nombre d'instances créées.
    """

    nb = 0 # nombre d'instances créées d'Acteur
    instances = [] # instances créées d'Acteur

    def __init__(self, latitude:float, longitude:float, dispos=None):
        """
        Initialise l'acteur.
        :param float latitude: Latitude en degrés de l'acteur.
        :param float longitude: Longitude en degrés de l'acteur.
        :param list[DemiJour] dispos: Liste des **DemiJour** où l'acteur est disponible.
        """
        self.id = Acteur.nb
        self.latitude = latitude
        self.longitude = longitude
        self.dispos = dispos if dispos is not None else []
        self.infosTournees = []     # contient les chaines de données sur les tournées qui impliquent l'acteur
        Acteur.instances.append(self)
        Acteur.nb += 1

    def __del__(self):
        """
        Détruit l'acteur.
        """
        Acteur.nb -= 1

    def addDispo(self, dispo:DemiJour):
        """
        Ajouter un **DemiJour** à la liste des disponibilités.
        :param list dispo: **DemiJour** à ajouter.
        """
        self.dispos.append(dispo)

    def removeDispo(self, dispo:DemiJour):
        """
        Retirer un **DemiJour** à la liste des disponibilités.
        :param list dispo: **DemiJour** à retirer.
        """
        self.dispos.remove(dispo)

    def getInfosTournees(self):
        result = ""
        for info in self.infosTournees:
            result += info + "\n"
        return result[:-1]

    @abc.abstractmethod
    def __str__(self)->str:
        pass

    @abc.abstractmethod
    def __repr__(self)->str:
        pass

    @classmethod
    def deleteAll(cls):
        cls.instances.clear()
        cls.nb = 0