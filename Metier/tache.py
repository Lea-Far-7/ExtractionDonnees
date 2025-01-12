from Metier.acteur import Acteur


class Tache:

    nb = 0 # nombre d'instances créées de Tache
    instances = []  # instances créées de Tache
    types = {'P':"Pick-Up", 'D':"Drop-Off"}

    def __init__(self, t:chr, charge:float, lieu:Acteur, infoRequete:Acteur, horaire:str):
        self.idTache = Tache.nb
        self.type = t
        self.charge = charge
        self.lieu = lieu
        self.infoRequete = infoRequete
        self.horaire = horaire
        Tache.instances.append(self)
        Tache.nb += 1

    def __del__(self):
        """
        Détruit la tâche.
        """
        Tache.nb -= 1

    def getType(self)->str:
        return Tache.types[self.type]

    def __str__(self)->str:
        result = "Tâche " + str(self.idTache) + "\n" + self.getType() + " " + str(self.charge)
        if self.type == "P":
            result += " chez Producteur " + str(self.lieu.id) + " pour Client " + str(self.infoRequete.id)
        else:
            result += " chez Client " + str(self.lieu.id) + " de Producteur " + str(self.infoRequete.id)
        result += " à " + self.horaire
        return result

    @classmethod
    def deleteAll(cls):
        cls.instances.clear()
        cls.nb = 0