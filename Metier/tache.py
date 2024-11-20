from acteur import Acteur


class Tache:

    nb = 0 # nombre d'instances créées de Tache

    def __init__(self, t:chr, charge:float, lieu:Acteur, infoRequete:Acteur, horaire:str):
        self.idTache = Tache.nb
        self.type = t
        self.charge = charge
        self.lieu = lieu
        self.infoRequete = infoRequete
        self.horaire = horaire
        Tache.nb += 1
