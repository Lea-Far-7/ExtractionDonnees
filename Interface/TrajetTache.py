from Interface.AfficherActeur import AfficherActeur
from Interface.AfficherTrajet import AfficherTrajet
from Metier.tache import Tache
from Metier.tournee import Tournee


class TrajetTache:
    """
    Classe côté Métier des chemins (trajets) gérant les données des tournées et tâches
    """
    def __init__(self, map, tache:Tache, tournee:Tournee, color, lieu2, lieu1, distance, duree, chargement, masterwindow):
        """
        Constructeur de la classe TrajetTache, créé un trajet sur la carte
        à partir des informations de la tournée et des autres paramètres.
        :param map: La carte contenue dans la fenêtre principale.
        :param tache: La tâche actuelle.
        :param tournee: La tournée dans laquelle se trouve la tâche actuelle.
        :param color: La couleur du marqueur de départ du trajet.
        :param lieu2: Le lieu de départ du trajet.
        :param lieu1: Le lieu d'arrivée du trajet.
        :param distance: La distance du trajet.
        :param duree: La duree du trajet.
        :param chargement: Le chargement géré par le trajet.
        :param masterwindow: La fenêtre principale.
        """
        self.tache = tache
        self.tournee = tournee

        self.lieu2 = lieu2 # Départ
        self.lieu1 = lieu1 # Arrivée

        self.distance = distance
        self.duree = duree
        self.chargement = chargement
        self.trajet_hidden = False


        # On récupère la fenêtre principale
        self.masterwindow = masterwindow

        # On instancie l'objet qui permettra d'afficher les données
        self.popup = AfficherTrajet(self.masterwindow, self, self.tache)

        # Créé un trait d'un point A à un point B
        self.trajet = self.masterwindow.map_widget.set_path([lieu2, lieu1], width=4, command=self.affichage, color=color)

    def affichage(self, event):
        """
        Cache toutes les bulles d'information de tous les affichages et
        permet l'affichage de la popup d'information en bas à droite.
        """
        AfficherTrajet.hide()
        AfficherActeur.hide()
        # Affiche le marqueur sur lequel on a cliqué
        self.popup.afficher()

    def hide(self):
        """
        Permet de cacher les informations affichées après un clic sur le trajet.
        """
        AfficherTrajet.hide()

    # Comme pour les marqueurs d'acteurs, on envoie les trajets à l'autre bout du monde
    def hide_trajet(self):
        """
        Fait disparaître temporairement le trajet pour pouvoir le re-afficher plus tard
        """
        if not self.trajet_hidden:
            self.trajet.set_position_list([(-89, -179),(-89, -179)])
            self.trajet_hidden = True

    def show_trajet(self):
        """
        Remet le trajet à son emplacement originel.
        :return: void
        """
        if self.trajet_hidden:
            self.trajet.set_position_list([self.lieu1,self.lieu2])
            self.trajet_hidden = False