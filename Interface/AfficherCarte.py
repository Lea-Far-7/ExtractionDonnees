from Interface.MarkerActeur import MarkerActeur
from Interface.TrajetTache import TrajetTache

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

        # lieu2 est le lieu de départ d'un trajet
        lieu2 = (0, 0)

        # Parcourt la liste des listes de tournées, cette variable contient la liste des tournées de chaque fichier.
        # Chaque fichier est une liste et celle-ci contient la liste des tournées
        for liste_tournees in liste_de_listes_de_tournees:
            # Parcourt les tournées de la liste de tournées
            for tournee in liste_tournees:
                # Défini la couleur du trajet en fonction de la couleur du marker du producteur de départ
                color = self.interface.mark_list[tournee.producteur.id].color

                # Variables compteurs
                temp = 0
                temp2 = temp

                # Parcourt la liste des taches contenues dans une tournée
                for tache in tournee.taches:

                    # Récupère la liste des distances, durées et chargements des trajets pour les associer aux trajets correspondants
                    list_dist, _, _ = tournee.distance()
                    list_duree, _, _ = tournee.duree()
                    list_chargement, _,_  = tournee.chargement()

                    # Première itération différente des autres étant donné qu'elle n'a pas de lieu de destination à proprement parler
                    if temp == 0:
                        lieu1 = self.interface.mark_list[tournee.producteur.id].marker.position
                        lieu2 = self.interface.mark_list[tache.lieu.id].marker.position

                        # Création du trajet
                        self.interface.path_list[tache] = TrajetTache(self.interface.map_widget, tache, tournee, color, lieu2, lieu1, list_dist[temp], list_duree[temp], list_chargement[temp], self.interface)
                        temp = 1

                    # Les autres itérations prennent les dernières coordonnées de la tâche précédente, puis se dirigent vers le marker de destination de la tâche
                    else:
                        # Temp2 sert à retarder le compte d'une itération pour garder la valeur d'avant pickup ou drop-off et ainsi afficher la bonne valeur sur la popup
                        nouv_lieu = self.interface.mark_list[tache.lieu.id].marker.position

                        # Création du trajet
                        self.interface.path_list[tache] = TrajetTache(self.interface.map_widget, tache, tournee, color, lieu2, nouv_lieu, list_dist[temp], list_duree[temp], list_chargement[temp2], self.interface)
                        lieu2 = nouv_lieu
                        temp += 1
                        temp2 += 1