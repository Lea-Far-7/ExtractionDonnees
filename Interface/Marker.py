import os

import customtkinter
from PIL import ImageTk, Image
from tkintermapview import map_widget

from Interface.PopupAffichage import PopupAffichage
from Metier.acteur import Acteur
from Metier.producteur import Producteur
from Metier.tache import Tache


class Marker():
    def __init__(self, map, acteur:Acteur, masterwindow):
        # Importe
        self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.image_client = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "../Images", "client.png")).resize((35, 35)))
        self.image_producteur = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "../Images", "producteur.png")).resize((35, 35)))

        self.acteur = acteur
        self.marker = map.set_marker(self.acteur.latitude, self.acteur.longitude, icon=self.image_producteur, command=self.affichage)

        self.masterwindow = masterwindow
        self.taches = None

        self.popup = PopupAffichage(self.masterwindow, self)

    def ajoutTaches(self, tache:Tache):
        self.taches.append(tache)

    def affichage(self, event):
        PopupAffichage.hide()
        self.popup.afficher()