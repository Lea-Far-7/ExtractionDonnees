from Interface.MarkerActeur import MarkerActeur
from Interface.TrajetTache import TrajetTache
from Modules.distance import distance


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
        # Parcourt les tournées et leurs tâches pour créer un trajet correspondant à chaque tâche
        for liste_tournees in liste_de_listes_de_tournees:
            for tournee in liste_tournees:
                color = self.interface.mark_list[tournee.producteur.id].color
                temp = 0
                temp2 = temp
                for tache in tournee.taches:
                    list_dist, _, _ = tournee.distance()
                    list_duree, _, _ = tournee.duree()
                    list_chargement, _,_  = tournee.chargement()
                    if temp == 0:
                        lieu1 = self.interface.mark_list[tournee.producteur.id].marker.position
                        lieu2 = self.interface.mark_list[tache.lieu.id].marker.position
                        self.interface.path_list[tache] = TrajetTache(self.interface.map_widget, tache, tournee, color, lieu2, lieu1, list_dist[temp], list_duree[temp], list_chargement[temp], self.interface)
                        temp = 1
                    else:
                        # Temp2 sert à retarder le compte d'une itération pour garder la valeur d'avant pickup ou dropoff et ainsi afficher la bonne valeur sur la popup
                        nouv_lieu = self.interface.mark_list[tache.lieu.id].marker.position
                        self.interface.path_list[tache] = TrajetTache(self.interface.map_widget, tache, tournee, color, lieu2, nouv_lieu, list_dist[temp], list_duree[temp], list_chargement[temp2], self.interface)
                        lieu2 = nouv_lieu
                        temp += 1
                        temp2 += 1