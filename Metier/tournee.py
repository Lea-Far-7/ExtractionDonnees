from Metier.acteur import Acteur
from Metier.producteur import Producteur
from Metier.demiJour import DemiJour
from Metier.tache import Tache
from Modules.distance import distance


class Tournee:

    nb = 0 # nombre d'instances créées de Tournee

    def __init__(self, demiJour:DemiJour, producteur:Producteur, taches=[]):
        self.idTournee = Tournee.nb
        self.demiJour = demiJour
        self.producteur = producteur
        self.taches = taches
        Tournee.nb += 1

    def addTache(self, t:chr, charge:float, lieu:Acteur, infoRequete:Acteur, horaire:str):
        tache = Tache(t,charge,lieu,infoRequete,horaire)
        self.taches.append(tache)
        return tache

    def removeTache(self, tache:Tache):
        self.taches.remove(tache)
        del(tache)

    def distanceTot(self)->float:
        if len(self.taches) < 2:
            return 0
        d = 0
        p0 = self.taches[0].lieu # point départ
        for tache in self.taches[1:]:
            p1 = tache.lieu # point suivant
            if p0 != p1:
                d += distance([p0.latitude,p0.longitude],[p1.latitude,p1.longitude])
            p0 = p1 # décalage pour le prochain point
        return d

    def chargementTot(self)->float:
        chargement = 0
        for tache in self.taches:
            if tache.type == 'P':
                chargement += tache.charge
        return chargement

    def chargementMax(self)->float:
        chargement = 0
        chargement_max = 0
        for tache in self.taches:
            if tache.type == 'P':
                chargement += tache.charge
                if chargement > chargement_max:
                    chargement_max = chargement
            else:
                chargement -= tache.charge
        return chargement_max

    def duree(self)->int:
        debut = self.taches[0].horaire
        fin = self.taches[-1].horaire
        [debutH, debutM] = debut.split(':')
        [finH, finM] = fin.split(':')
        return (int(finH)-int(debutH))*60 + (int(finM)-int(debutM))

    def __str__(self)->str:
        result = ("Tournée " + str(self.idTournee) + " : "
                + "\n\t" + str(self.demiJour)
                + "\n\tProducteur " + str(self.producteur.id)
                + "\n\tTaches : ")
        for tache in self.taches:
            result += "\n\t\t" + str(tache)

        return result
