from Metier.acteur import Acteur
from Metier.demiJour import DemiJour


class Producteur(Acteur):

    """
    Classe représentant un producteur.

    L'attribut de classe **nb** permet de récupérer le nombre d'instances créées.
    """

    nb = 0 # nombre d'instances de Producteur

    def __init__(self, latitude:float, longitude:float, capacity:float, dispos=None, partners=None):
        """
        Initialise le producteur.
        :param float latitude: Latitude en degrés du producteur.
        :param float longitude: Longitude en degrés du producteur.
        :param float capacity: Capacité en kg du camion du producteur.
        :param list[DemiJour] dispos: Liste des **DemiJour** où le producteur est disponible. Par défaut, une liste vide.
        :param list[Producteur] partners: Liste des **Producteur** partenaires. Par défaut, une liste vide.
        """
        super().__init__(latitude,longitude,dispos)
        self.capacity = capacity
        self.partners = partners if partners is not None else []
        Producteur.nb += 1

    def addPartner(self, partner:"Producteur"):
        """
        Ajouter un **Producteur** à la liste des partenaires.
        :param Producteur partner: **Producteur** à ajouter.
        """
        self.partners.append(partner)

    def removePartner(self, partner:"Producteur"):
        """
        Retirer un **Producteur** à la liste des partenaires.
        :param Producteur partner: **Producteur** à retirer.
        """
        self.partners.remove(partner)

    def __str__(self)->str:
        """
        Affiche les informations sur le producteur.
        """
        result = "Producteur " + str(self.id) + " :"
        result += "\n\tCoordonnées : (" + str(self.latitude) + " ; " + str(self.longitude) + ")"
        result += "\n\tCapacité : " + str(self.capacity) + "kg"
        result += "\n\tDispos : "
        for dispo in self.dispos:
            result += "\n\t\t" + str(dispo)
        result += "\n\tPartenaires : "
        for partner in self.partners:
            result += "\n\t\tProducteur " + str(partner.id)
        return result

    def __repr__(self)->str:
        """Affichage simple"""
        return "Producteur " + str(self.id)
