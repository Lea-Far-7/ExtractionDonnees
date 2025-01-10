from PIL import ImageTk, Image
from Interface.AfficherActeur import AfficherActeur
from Interface.colors import color_palette, colors_nb
from Metier.acteur import Acteur
from Metier.client import Client
from Metier.tache import Tache

class MarkerActeur:

    image_client = None

    @classmethod
    def charger_image_client(cls):
        if cls.image_client is None:
            cls.image_client = ImageTk.PhotoImage(Image.open("..\Images\\client.png").resize((20, 20)))

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
            # Crée un marker sur la carte basé sur l'identifiant du client
            MarkerActeur.charger_image_client()
            self.marker = map.set_marker(self.acteur.latitude, self.acteur.longitude, icon=MarkerActeur.image_client, command=self.affichage)
        else:
            # Crée un marker sur la carte basé sur l'identifiant du producteur
            self.marker = map.set_marker(self.acteur.latitude, self.acteur.longitude, marker_color_outside="#000000",
                                         marker_color_circle=self.color, command=self.affichage)

        self.marker_hidden = False

    def affichage(self, event):
        # Cache toutes les bulles d'information de tous les affichages
        AfficherActeur.hide()
        # Affiche le marqueur sur lequel on a cliqué
        self.popup.afficher()

    def hide(self):
        AfficherActeur.hide()


    # Pour faire disparaître le marqueur, on n'a rien trouvé de mieux pour l'instant que de l'envoyer à l'autre bout du monde
    # (-89;-179) se situe en Antarctique sur le bord de carte du logiciel donc impossible à voir
    def hide_marker(self):
        if not self.marker_hidden:
            self.marker.set_position(-89, -179)
            self.marker_hidden = True

    def show_marker(self):
        if self.marker_hidden:
            self.marker.set_position(self.acteur.latitude, self.acteur.longitude)
            self.marker_hidden = False
