from Interface.AffichageClient import AffichageClient
from Interface.AffichageProducteur import AffichageProducteur
from Interface.colors import color_palette, colors_nb
from Metier.producteur import Producteur
from Metier.tache import Tache

class MarkerProducteur():
    def __init__(self, map, prod:Producteur, masterwindow):
        self.prod = prod

        # Créé un marker sur la carte basé sur l'identifiant du producteur
        self.marker = map.set_marker(self.prod.latitude, self.prod.longitude, marker_color_outside="#000000", marker_color_circle= color_palette[prod.id % colors_nb], command=self.affichage)

        # Ici on récupère la fenêtre principale
        self.masterwindow = masterwindow

        self.taches = None

        # Ici on instancie l'objet qui permettra d'afficher les données
        self.popup = AffichageProducteur(self.masterwindow, self)

    # Ajout de taches à l'objet pour les afficher par la suite
    def ajoutTaches(self, tache:Tache):
        self.taches.append(tache)

    def affichage(self, event):
        # Cache toutes les bulles d'information de tous les affichages
        AffichageProducteur.hide(AffichageClient)
        # Affiche le marqueur sur lequel on a cliqué
        self.popup.afficher()

    def hide(self):
        AffichageProducteur.hide(AffichageClient)