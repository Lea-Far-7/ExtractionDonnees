from PIL import ImageTk, Image
from Interface.AfficherActeur import AfficherActeur
from Interface.AfficherTrajet import AfficherTrajet
from Interface.colors import color_palette, colors_nb
from Metier.acteur import Acteur
from Metier.client import Client

class MarkerActeur:
    """
    Classe côté Métier des marqueurs gérant les données des Acteurs (producteurs et clients)
    """

    image_client = None

    @classmethod
    def charger_image_client(cls):
        """
        Permet de charger l'image représentant les clients sur la carte.
        :return: void
        """
        if cls.image_client is None:
            cls.image_client = ImageTk.PhotoImage(Image.open("Images\\client.png").resize((20, 20)))

    def __init__(self, map, acteur:Acteur, masterwindow):
        """
        Initialise tous les attributs et créé les marqueurs sur la carte en leur associant un affichage conditionnel au clic.
        :param map: Représente la carte.
        :param acteur: Est l'acteur concerné.
        :param masterwindow: Correspond à la fenêtre principale.
        """
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
        """
        Cache toutes les bulles d'information de tous les affichages et
        permet l'affichage de la popup d'information en bas à droite.
        """
        AfficherActeur.hide()
        AfficherTrajet.hide()
        # Affiche le marqueur sur lequel on a cliqué
        self.popup.afficher()

    def hide(self):
        """
        Permet de cacher les informations affichées après un clic sur le marqueur.
        """
        AfficherActeur.hide()

    def hide_marker(self):
        """
        Pour faire disparaître le marqueur, on n'a rien trouvé de mieux pour l'instant que de l'envoyer à l'autre bout du monde
        (-89;-179) se situe en Antarctique sur le bord de carte du logiciel donc impossible à voir.
        :return: void
        """
        if not self.marker_hidden:
            self.marker.set_position(-89, -179)
            self.marker_hidden = True

    def show_marker(self):
        """
        Remet le marqueur à son emplacement originel.
        :return: void
        """
        if self.marker_hidden:
            self.marker.set_position(self.acteur.latitude, self.acteur.longitude)
            self.marker_hidden = False