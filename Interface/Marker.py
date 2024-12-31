import os

import customtkinter
from PIL import ImageTk, Image
from tkintermapview import map_widget

from Interface.PopupAffichage import PopupAffichage
from Interface.colors import color_palette, colors_nb
from Metier.acteur import Acteur
from Metier.producteur import Producteur
from Metier.tache import Tache


class Marker():
    def __init__(self, map, acteur:Acteur, masterwindow):
        self.acteur = acteur
        self.marker = map.set_marker(self.acteur.latitude, self.acteur.longitude, marker_color_outside="#000000", marker_color_circle= color_palette[acteur.id % colors_nb], command=self.affichage)

        self.masterwindow = masterwindow
        self.taches = None

        self.popup = PopupAffichage(self.masterwindow, self)

    def ajoutTaches(self, tache:Tache):
        self.taches.append(tache)

    def affichage(self, event):
        PopupAffichage.hide()
        self.popup.afficher()