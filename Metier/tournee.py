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
        self.__infosTournee_injection()

    def __infosTournee_injection(self):
        for tache in self.taches:
            info = tache.getType() + " " + str(tache.charge) + " " + {"P":"pour","D":"de"}[tache.type] + " " + repr(tache.infoRequete)
            info += " " + repr(self.demiJour) + " " + tache.horaire
            tache.lieu.infosTournees.append(info)

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

    def distance(self)->tuple[list,float,float]:
        """
        Calcule les distances parcourues pour effectuer chaque tâche, le maximum et le total.
        :return:
            - Liste des distances parcourues en km.
            - Distance maximale parcourue pour une tâche.
            - Distance totale parcourue pour la tournée.
        """
        distances = []
        dmax = 0
        dtot = 0
        p0 = self.producteur # point départ
        for tache in self.taches:
            p1 = tache.lieu # point suivant
            d = distance([p0.latitude,p0.longitude],[p1.latitude,p1.longitude])
            distances.append(d)
            if d > dmax:
                dmax = d
            dtot += d
            p0 = p1 # décalage pour le prochain point
        return distances, dmax, dtot

    def chargement(self)->tuple[list,float,float]:
        """
        Calcule les chargements transportés entre chaque tâche, le maximum et le total.
        :return:
            - Liste des chargements transportés entre les tâches en kg.
            - Chargement maximal transporté entre deux tâches.
            - Chargement total transporté durant la tournée.
        """
        chargements = []
        cmax = 0
        ctot = 0
        c = 0
        for tache in self.taches:
            if tache.type == 'P':
                c += tache.charge
                if c > cmax:
                    cmax = c
            else:
                c -= tache.charge
            chargements.append(c)
            ctot += c
        return chargements, cmax, ctot

    def duree(self)->tuple[list,float,float]:
        """
        Calcule les durées entre chaque tâche, le maximum et le total.
        :return:
            - Liste des durées entre les tâches en minutes.
            - Durée maximale entre deux tâches.
            - Durée totale pour la tournée.
        """
        durees = []
        dmax = 0
        dtot = 0
        t0 = self.taches[0].horaire
        for tache in self.taches:
            t1 = tache.horaire
            [t0h, t0m] = t0.split(':')
            [t1h, t1m] = t1.split(':')
            t = (int(t1h)-int(t0h))*60 + (int(t1m)-int(t0m))
            durees.append(t)
            if t > dmax:
                dmax = t
            dtot += t
            t0 = t1
        return durees, dmax, dtot

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
