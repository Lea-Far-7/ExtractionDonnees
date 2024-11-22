from acteur import Acteur


class Tache:

    nb = 0 # nombre d'instances créées de Tache
    types = {'P':"Pick-Up", 'D':"Drop-Off"}

    def __init__(self, t:chr, charge:float, lieu:Acteur, infoRequete:Acteur, horaire:str):
        self.idTache = Tache.nb
        self.type = t
        self.charge = charge
        self.lieu = lieu
        self.infoRequete = infoRequete
        self.horaire = horaire
        Tache.nb += 1

    def getType(self)->str:
        return Tache.types[self.type]

    def __str__(self)->str:
        return ("Tache " + str(self.idTache) + " : " + self.getType() + " " + str(self.charge)
                + " chez Acteur " + str(self.lieu.id) + " pour Acteur " + str(self.infoRequete.id)
                + " à " + self.horaire)
