from PIL import ImageTk, Image
from Interface.AfficherActeur import AfficherActeur
from Interface.colors import color_palette, colors_nb
from Metier.acteur import Acteur
from Metier.client import Client
from Metier.tache import Tache

class MarkerActeur:
    def __init__(self, map, acteur:Acteur, masterwindow):
        self.acteur = acteur
        self.taches = None

        # On récupère la fenêtre principale
        self.masterwindow = masterwindow

        # On instancie l'objet qui permettra d'afficher les données
        self.popup = AfficherActeur(self.masterwindow, self, self.acteur)

        self.color = color_palette[acteur.id % colors_nb]

        # Charge l'image pour l'icône des clients
        if isinstance(acteur, Client):
            image_client = ImageTk.PhotoImage(Image.open("..\Images\\client.png").resize((35, 35)))
            # Crée un marker sur la carte basé sur l'identifiant du client
            self.marker = map.set_marker(self.acteur.latitude, self.acteur.longitude, icon=image_client, command=self.affichage)
        else:
            # Crée un marker sur la carte basé sur l'identifiant du producteur
            self.marker = map.set_marker(self.acteur.latitude, self.acteur.longitude, marker_color_outside="#000000",
                                         marker_color_circle=self.color, command=self.affichage)


    # Ajout de taches à l'objet pour les afficher par la suite
    def ajoutTaches(self, tache:Tache):
        self.taches.append(tache)

    def affichage(self, event):
        # Cache toutes les bulles d'information de tous les affichages
        AfficherActeur.hide()
        # Affiche le marqueur sur lequel on a cliqué
        self.popup.afficher()

    def hide(self):
        AfficherActeur.hide()