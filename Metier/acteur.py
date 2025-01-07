import abc # pour classe abstraite

from Metier.ObserverActeur import ObserverActeur
from Metier.demiJour import DemiJour


class Acteur(abc.ABC):

    """
    Classe abstraite représentant un acteur.

    Elle peut servir à représenter un **Producteur** ou un **Client**.

    L'identifiant d'un Acteur dépend de son ordre d'instanciation.

    L'attribut de classe **nb** permet de récupérer le nombre d'instances créées.
    """

    nb = 0 # nombre d'instances créées d'Acteur
    instances = {} # instances créées d'Acteur

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
        self.infosTournees = [[],[]]     # contient les chaines de données sur les tournées qui impliquent l'acteur
                                        # 1è sous-liste : conduite de tournée, 2è sous-liste : passage de tournée
        self.observers = [] # liste des objets qui doivent réagir à la modification de infosTournees (MarkerActeur)
        Acteur.instances[Acteur.nb] = self
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

    def getInfosTournees(self)->str:
        result = ""
        for part in self.infosTournees:
            for info in part:
                result += info + "\n"
        return result[:-1]

    def attachObserver(self, observer:ObserverActeur):
        if observer not in self.observers:
            self.observers.append(observer)

    def detachObserver(self, observer:ObserverActeur):
        if observer in self.observers:
            self.observers.remove(observer)

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

    @classmethod
    def updateInfosTournees(cls, listSolutions:list):   # listSolutions = liste de liste de tournées
        for instance in cls.instances.values():
            instance.infosTournees = [[],[]]    #initialisation
        for listTournees in listSolutions:
            for tournee in listTournees:
                cls.instances[tournee.producteur.id].infosTournees[0].append("Conduite de la tournée "+str(tournee.idTournee))
                for tache in tournee.taches:
                    info = (tache.getType() + " " + str(tache.charge) + " " + {"P": "pour", "D": "de"}[
                        tache.type] + " " + repr(tache.infoRequete) + " " + repr(tournee.demiJour) + " " + tache.horaire +
                        " par " + repr(tournee.producteur))
                    cls.instances[tache.lieu.id].infosTournees[1].append(info)
        for instance in cls.instances.values():
            for observer in instance.observers:
                observer.update()
            # Tests
            # print("\n-- InfosTournees "+repr(instance)+" --")
            # print(instance.getInfosTournees())