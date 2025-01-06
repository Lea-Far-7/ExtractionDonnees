from Interface.AfficherActeur import AfficherActeur
from Metier.tache import Tache


class PathTrajet:
    def __init__(self, map, tache:Tache, masterwindow):
        self.tache = tache

        # On récupère la fenêtre principale
        self.masterwindow = masterwindow

        # On instancie l'objet qui permettra d'afficher les données
        self.popup = None

        #self.trajet = map.set_path([(self.tache.lieu.latitude,self.tache.lieu.longitude), (self.tache.infoRequete.latitude,self.tache.infoRequete.longitude)],width=5,command="")

    def affichage(self, event):
        # Cache toutes les bulles d'information de tous les affichages
        AfficherActeur.hide()
        # Affiche le marqueur sur lequel on a cliqué
        self.popup.afficher()

    def hide(self):
        AfficherActeur.hide()