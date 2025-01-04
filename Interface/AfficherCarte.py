from Interface.MarkerActeur import MarkerActeur

class AfficherCarte:

    def __init__(self, interface):
        self.interface = interface

    def markers_producteurs(self, infos_producteur):
        # Parcourt les producteurs créés et crée les marqueurs associés
        for prod in infos_producteur:
            self.interface.mark_list.append(MarkerActeur(self.interface.map_widget, prod, self.interface))

    def markers_clients(self, infos_clients):
        # Parcourt les clients créés et crée les marqueurs associés
        for cl in infos_clients:
            self.interface.mark_list.append(MarkerActeur(self.interface.map_widget, cl, self.interface))