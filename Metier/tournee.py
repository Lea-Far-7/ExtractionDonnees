from decimal import getcontext, Decimal

from Metier.acteur import Acteur
from Metier.producteur import Producteur
from Metier.demiJour import DemiJour
from Metier.tache import Tache
from Modules.distance import distance

class Tournee:

    nb = 0  # nombre d'instances créées de Tournee
    instances = []  # instances créées de Tournee

    def __init__(self, demiJour:DemiJour, producteur:Producteur, taches=[]):
        self.idTournee = Tournee.nb
        self.demiJour = demiJour
        self.producteur = producteur
        self.taches = taches
        Tournee.instances.append(self)
        Tournee.nb += 1

    def __del__(self):
        """
        Détruit la tournée.
        """
        Tournee.nb -= 1

    def addTache(self, t:chr, charge:float, lieu:Acteur, infoRequete:Acteur, horaire:str):
        tache = Tache(t,charge,lieu,infoRequete,horaire)
        self.taches.append(tache)
        return tache

    def removeTache(self, tache:Tache):
        self.taches.remove(tache)
        del(tache)

    def distance(self)->tuple[list[float], float, float]:
        """
        Calcule les distances parcourues pour effectuer chaque tâche, le maximum et le total.
        :return:
            - Liste des distances parcourues en km.
            - Distance maximale parcourue pour une tâche.
            - Distance totale parcourue pour la tournée.
        """
        if not self.taches:
            return [], 0.0, 0.0
        distances = []
        p0 = self.producteur # point départ
        for tache in self.taches:
            p1 = tache.lieu # point suivant
            d = distance([p0.latitude,p0.longitude],[p1.latitude,p1.longitude])
            distances.append(d)
            p0 = p1 # décalage pour le prochain point
        return distances, max(distances), sum(distances)

    def chargement(self)->tuple[list[float], float, float]:
        """
        Calcule les chargements transportés entre chaque tâche, le maximum et le total.
        :return:
            - Liste des chargements transportés entre les tâches en kg.
            - Chargement maximal transporté entre deux tâches.
            - Chargement total transporté durant la tournée.
        """

        getcontext().prec = 28

        chargements = []
        charge_max = Decimal('0')
        charge_totale = Decimal('0')
        chargeCumulee = Decimal('0')

        for tache in self.taches:
            c = Decimal(str(tache.charge))

            if tache.type == 'P':
                chargeCumulee += c
                charge_max = max(charge_max, chargeCumulee)
                charge_totale += c
            else:
                chargeCumulee -= c
            chargements.append(float(chargeCumulee))

        print("Tournee ", self.idTournee)
        if chargeCumulee != 0:
            print ("Commande non livrée, reste : ", chargeCumulee)
        else:
            print("Reste 0 : toutes les commandes ont été livrées")
        if charge_max >= self.producteur.capacity:
            print("Charge maximale : ", charge_max, " kg")
            print("Supérieur à la capacité du camion : ", self.producteur.capacity, " kg")

        return chargements, float(charge_max), float(charge_totale)

    def duree(self)->tuple[list[int], int, int]:
        """
        Calcule les durées entre chaque tâche, le maximum et le total.
        :return:
            - Liste des durées entre les tâches en minutes.
            - Durée maximale entre deux tâches.
            - Durée totale pour la tournée.
        """
        if not self.taches:
            return [], 0, 0
        durees = []
        t0 = self.taches[0].horaire
        for tache in self.taches:
            t1 = tache.horaire
            [t0h, t0m] = t0.split(':')
            [t1h, t1m] = t1.split(':')
            t = (int(t1h)-int(t0h))*60 + (int(t1m)-int(t0m))
            durees.append(t)
            t0 = t1
        return durees, max(durees), sum(durees)

    def __str__(self)->str:
        result = ("Tournée " + str(self.idTournee) + " : "
                + "\n\t" + str(self.demiJour)
                + "\n\tProducteur " + str(self.producteur.id)
                + "\n\tTaches : ")
        for tache in self.taches:
            result += "\n\t\t" + str(tache)

        return result

    @classmethod
    def deleteAll(cls):
        cls.instances.clear()
        cls.nb = 0

    @classmethod
    def getNbTourneesProd(cls)->dict:
        """
        Calcule le nombre de tournées effectuées pour chaque producteur.
        Si un producteur est absent du dictionnaire renvoyé, aucune tournée n'est effectuée par lui.
        :return: Dictionnaire avec pour clés des Producteurs et pour valeurs les nombres de tournées effectuées.
        """
        result = {}
        for tournee in cls.instances:
            if tournee.producteur in result:
                result[tournee.producteur] += 1
            else:
                result[tournee.producteur] = 1
        return result
