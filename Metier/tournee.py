from producteur import Producteur
from demiJour import DemiJour
from tache import Tache


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
