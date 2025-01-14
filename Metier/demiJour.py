class DemiJour:

    """Classe représentant une demi-journée."""

    defaultLabels = ["Lundi matin", "Lundi après-midi", "Mardi matin", "Mardi après-midi", "Mercredi matin", "Mercredi après-midi",
                     "Jeudi matin", "Jeudi après-midi", "Vendredi matin", "Vendredi après-midi"]

    def __init__(self, num, label=None):
        """
        Initialise la demi-journée.
        :param int num: Numéro associé à la demi-journée.
        :param str label: Etiquette associée à la demi-journée. Si elle n'est pas renseignée, elle prendra une valeur selon le numéro.
        """
        self.num = num
        if label:
            self.label = label
        else:
            self.label = DemiJour.defaultLabels[num % 10]

    def __str__(self)->str:
        """
        Affiche les informations sur la demi-journée.
        """
        return "Demi-jour "+ str(self.num) + " : " + self.label

    def __repr__(self)->str:
        """Affichage simple"""
        return self.label
