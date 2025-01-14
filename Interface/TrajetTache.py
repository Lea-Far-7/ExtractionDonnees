from Interface.AfficherActeur import AfficherActeur
from Interface.AfficherTrajet import AfficherTrajet
from Metier.tache import Tache
from Metier.tournee import Tournee


class TrajetTache:
    def __init__(self, map, tache:Tache, tournee:Tournee, color, lieu2, lieu1, distance, duree, chargement, masterwindow):
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
        # Cache toutes les bulles d'information de tous les affichages
        AfficherTrajet.hide()
        AfficherActeur.hide()
        # Affiche le marqueur sur lequel on a cliqué
        self.popup.afficher()

    def hide(self):
        AfficherTrajet.hide()

    # Comme pour les marqueurs d'acteurs, on envoie les trajets à l'autre bout du monde
    def hide_trajet(self):
        if not self.trajet_hidden:
            self.trajet.set_position_list([(-89, -179),(-89, -179)])
            self.trajet_hidden = True

    def show_trajet(self):
        if self.trajet_hidden:
            self.trajet.set_position_list([self.lieu1,self.lieu2])
            self.trajet_hidden = False