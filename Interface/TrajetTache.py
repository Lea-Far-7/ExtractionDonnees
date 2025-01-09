from Interface.AfficherTrajet import AfficherTrajet
from Metier import tournee
from Metier.tache import Tache
from Metier.tournee import Tournee


class TrajetTache:
    def __init__(self, map, tache:Tache, tournee:Tournee, color, lieu2, nouv_lieu, masterwindow):
        self.tache = tache
        self.tournee = tournee

        # On récupère la fenêtre principale
        self.masterwindow = masterwindow

        # On instancie l'objet qui permettra d'afficher les données
        self.popup = AfficherTrajet(self.masterwindow, self, self.tache)

        if nouv_lieu == None:
            self.trajet = self.masterwindow.map_widget.set_path(
                [self.masterwindow.mark_list[tournee.producteur.id].marker.position, lieu2], width=4,
                command=self.affichage, color=color)
        else :
            self.trajet = self.masterwindow.map_widget.set_path(
                [lieu2, nouv_lieu], width=4, command=self.affichage, color=color)


    def affichage(self, event):
        # Cache toutes les bulles d'information de tous les affichages
        AfficherTrajet.hide()
        # Affiche le marqueur sur lequel on a cliqué
        self.popup.afficher()

    def hide(self):
        AfficherTrajet.hide()