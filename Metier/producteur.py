from acteur import Acteur


class Producteur(Acteur):

    nb = 0 # nombre d'instances de Producteur

    def __init__(self, latitude:float, longitude:float, capacity:float, dispos=[], partners=[]):
        super().__init__(latitude,longitude,dispos)
        self.capacity = capacity
        self.partners = partners
        Producteur.nb += 1

    def addPartner(self, partner:"Producteur"):
        self.partners.append(partner)

    def removePartner(self, partner:"Producteur"):
        self.partners.remove(partner)

    def __str__(self)->str:
        result = "Producteur " + str(self.id) + " :"
        result += "\n\tCoordonnées : (" + str(self.latitude) + " ; " + str(self.longitude) + ")"
        result += "\n\tCapacité : " + str(self.capacity)
        result += "\n\tDispos : "
        for dispo in self.dispos:
            result += "\n\t\t" + str(dispo)
        result += "\n\tPartenaires : "
        for partner in self.partners:
            result += "\n\t\tProducteur " + str(partner.id)
        return result
