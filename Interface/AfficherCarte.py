from Interface.MarkerActeur import MarkerActeur

class AfficherCarte:

    def __init__(self, interface):
        self.interface = interface

    def markers_producteurs(self, infos_producteur):
        # Parcourt les producteurs créés et crée les marqueurs associés
        for prod in infos_producteur:
            self.interface.mark_list[prod.id] = (MarkerActeur(self.interface.map_widget, prod, self.interface))

    def markers_clients(self, infos_clients):
        # Parcourt les clients créés et crée les marqueurs associés
        for cl in infos_clients:
            self.interface.mark_list[cl.id] = (MarkerActeur(self.interface.map_widget, cl, self.interface))

    def path_taches(self, liste_de_listes_de_tournees):
        lieu2 = (0, 0)
        for liste_tournees in liste_de_listes_de_tournees:
            for tournee in liste_tournees:
                color = self.interface.mark_list[tournee.producteur.id].color
                temp = 0
                for tache in tournee.taches:
                    # print(tache)
                    if temp == 0:
                        lieu2 = self.interface.mark_list[tache.lieu.id].marker.position
                        self.interface.path_list[tache] = self.interface.map_widget.set_path(
                            [self.interface.mark_list[tournee.producteur.id].marker.position, lieu2], width=4,
                            command="", color=color)
                        temp = 1
                    else:
                        nouv_lieu = self.interface.mark_list[tache.lieu.id].marker.position
                        self.interface.path_list[tache] = self.interface.map_widget.set_path(
                            [lieu2, nouv_lieu], width=4, command="", color=color)
                        lieu2 = nouv_lieu