import os

import customtkinter
from PIL import ImageTk, Image
from tkintermapview import map_widget

from Interface.PopupAffichage import PopupAffichage
from Interface.colors import color_palette, colors_nb
from Metier.acteur import Acteur
from Metier.client import Client
from Metier.producteur import Producteur
from Metier.tache import Tache


class Marker():
    def __init__(self, map, acteur:Acteur, masterwindow):
        self.acteur = acteur

        if acteur.__class__ is Producteur :
            self.marker = map.set_marker(self.acteur.latitude, self.acteur.longitude, marker_color_outside="#000000", marker_color_circle= color_palette[acteur.id % colors_nb], command=self.affichage)
            self.masterwindow = masterwindow
            self.taches = None

            self.popup = PopupAffichage(self.masterwindow, self)
        else :
            # Charge les images pour les icônes des producteurs et clients
            self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
            self.image_client = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "../Images", "client.png")).resize((35, 35)))
            self.marker = map.set_marker(self.acteur.latitude, self.acteur.longitude, icon = self.image_client,
                                         command=self.affichage)
            #TODO : Continuer pour afficher les informations correspondantes

    def ajoutTaches(self, tache:Tache):
        self.taches.append(tache)

    def affichage(self, event):
        PopupAffichage.hide()
        self.popup.afficher()