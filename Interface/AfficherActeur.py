import customtkinter

from Metier.ObserverActeur import ObserverActeur
from Metier.acteur import Acteur

class AfficherActeur(ObserverActeur):
    """
    Cette classe permet d'afficher les informations des Acteurs selon les Marqueurs passés en paramètre
    """
    instances = []

    def __init__(self, masterwindow, marker, acteur : Acteur):
        """
        L'initialisation permet de rentrer les données passées en paramètres.
        :param masterwindow: Fenêtre principale.
        :param marker: Objet MarkerActeur contenant le marqueur placé sur la carte.
        :param acteur: Objet Acteur contenant les informations sur l'acteur concerné.
        """
        self.__class__.instances.append(self)
        self.masterwindow = masterwindow
        self.marker = marker
        self.acteur = acteur

        self.acteur.attachObserver(self)

        self.window = customtkinter.CTkToplevel()
        self.window.withdraw()
        self.window.overrideredirect(True)

        self.label = customtkinter.CTkLabel(self.window, text=str(acteur), fg_color="transparent")
        self.label.grid(row=0, column=0, columnspan=1, padx=20, pady=10)


    @classmethod
    def hide(cls):
        """
        Permet de cacher les informations affichées après un clic sur le trajet.
        :param cls: La classe concernée.
        """
        for i in cls.instances:
            i.window.withdraw()


    # Garde la popup en bas à droite de l'écran
    def update_popup_position(self, event=None):
        """
        Permet de garder l'affichage en bas à droite de la fenêtre.
        :param event: L'évènement concernant l'affichage, non-utilisé ici.
        """
        if self.window.state() != 'withdrawn':
            self.window.geometry(
                "+%d+%d" % (self.masterwindow.winfo_rootx() + self.masterwindow.winfo_width() - self.window.winfo_width(),
                            self.masterwindow.winfo_rooty() + self.masterwindow.winfo_height() - self.window.winfo_height()))
            self.window.lift()


    def update(self):
        """
        Appel effectué à chaque fois qu'infoTournees de l'acteur change, met à jour les informations.
        :return: void
        """
        newtext = str(self.acteur)
        infosTournees = self.acteur.getInfosTournees()
        if infosTournees != "":
            newtext += "\n\n" + infosTournees
        self.label.configure(text = newtext)
        self.label.update()


    def afficher(self):
        """
        Permet l'affichage de la popup d'information en bas à droite.
        :return: void
        """
        self.window.deiconify()
        # Force la mise à jour de l'interface utilisateur
        self.masterwindow.update_idletasks()
        self.update_popup_position()