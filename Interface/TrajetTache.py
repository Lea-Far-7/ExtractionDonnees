from Interface.AfficherTrajet import AfficherTrajet
from Metier.tache import Tache


class MarkerActeur:
    def __init__(self, map, tache:Tache, masterwindow):
        self.tache = tache

        # On récupère la fenêtre principale
        self.masterwindow = masterwindow

        # On instancie l'objet qui permettra d'afficher les données
        self.popup = AfficherTrajet(self.masterwindow, self, self.tache)

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

        self.marker_hide = False


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