import os

from PIL import ImageTk, Image
from Interface.AffichageClient import AffichageClient
from Interface.AffichageProducteur import AffichageProducteur
from Metier.acteur import Acteur
from Metier.tache import Tache

class MarkerClient:
    def __init__(self, map, acteur:Acteur, masterwindow):
        self.acteur = acteur
        self.masterwindow = masterwindow
        self.taches = None
        self.popup = AffichageClient(self.masterwindow, self)

        # Charge les images pour les icônes des producteurs et clients
        self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.image_client = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "../Images", "client.png")).resize((35, 35)))
        self.marker = map.set_marker(self.acteur.latitude, self.acteur.longitude, icon = self.image_client,
                                         command=self.affichage)
        #TODO : Continuer pour afficher les informations correspondantes

    def ajoutTaches(self, tache:Tache):
        self.taches.append(tache)

    def affichage(self, event):
        AffichageClient.hide(AffichageProducteur)
        self.popup.afficher()