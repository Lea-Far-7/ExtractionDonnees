
class DemiJour:

    defaultLabels = ["Lundi matin", "Lundi après-midi", "Mardi matin", "Mardi après-midi",
        "Mercredi matin", "Mercredi après-midi", "Jeudi matin", "Jeudi après-midi",
        "Vendredi matin", "Vendredi après-midi"]

    def __init__(self, num, label=None):
        self.num = num
        if label:
            self.label = label
        else:
            self.label = DemiJour.defaultLabels[num % 10]

    def __str__(self)->str:
        return "Demi-jour "+ str(self.num) + " : " + self.label
