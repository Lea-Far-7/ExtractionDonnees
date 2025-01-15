from Metier.acteur import Acteur

class Tache:

    nb = 0 # nombre d'instances créées de Tache
    instances = []  # instances créées de Tache
    types = {'P':"Pick-Up", 'D':"Drop-Off"}

    def __init__(self, t:chr, charge:float, lieu:Acteur, infoRequete:Acteur, horaire:str):
        """
        Initialise la Tache.
        :param chr t: Type de tâche, 'P' pour Pick-Up, 'D' pour Drop-Off.
        :param charge: Charge récupérée ou déposée durant la tâche.
        :param lieu: Acteur chez lequel se déroule la tâche.
        :param infoRequete: Autre Acteur qui est lié à la demande assurée par cette tâche.
        :param horaire: Heure au format HH:MM de la tâche.
        """
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
        """
        Renvoie le nom complet du type de la tâche.
        """
        return Tache.types[self.type]

    def __str__(self)->str:
        """
        Affiche les informations sur la tâche.
        """
        result = "Tâche " + str(self.idTache) + "\n" + self.getType() + " " + str(self.charge)
        if self.type == "P":
            result += " chez Producteur " + str(self.lieu.id) + " pour Client " + str(self.infoRequete.id)
        else:
            result += " chez Client " + str(self.lieu.id) + " de Producteur " + str(self.infoRequete.id)
        result += " à " + self.horaire
        return result

    @classmethod
    def deleteAll(cls):
        """
        Efface toutes les instances de Tache.
        """
        cls.instances.clear()
        cls.nb = 0