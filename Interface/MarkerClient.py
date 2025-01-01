import os

from PIL import ImageTk, Image
from Interface.AffichageClient import AffichageClient
from Interface.AffichageProducteur import AffichageProducteur
from Metier.acteur import Acteur
from Metier.client import Client
from Metier.tache import Tache

class MarkerClient:
    def __init__(self, map, client:Client, masterwindow):
        self.client = client

        # Ici on récupère la fenêtre principale
        self.masterwindow = masterwindow

        self.taches = None

        # Ici on instancie l'objet qui permettra d'afficher les données
        self.popup = AffichageClient(self.masterwindow, self)

        # Charge l'image pour l'icône des clients
        self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.image_client = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "../Images", "client.png")).resize((35, 35)))

        # Créé un marker sur la carte basé sur l'identifiant du client
        self.marker = map.set_marker(self.client.latitude, self.client.longitude, icon = self.image_client,
                                         command=self.affichage)

    # Ajout de taches à l'objet pour les afficher par la suite
    def ajoutTaches(self, tache:Tache):
        self.taches.append(tache)

    def affichage(self, event):
        # Cache toutes les bulles d'information de tous les affichages
        AffichageClient.hide(AffichageProducteur)
        # Affiche le marqueur sur lequel on a cliqué
        self.popup.afficher()