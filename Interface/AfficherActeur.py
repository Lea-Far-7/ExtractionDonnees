import customtkinter

from Metier.acteur import Acteur
from Metier.client import Client
from Metier.producteur import Producteur

class AfficherActeur:

    instances = []

    def __init__(self, masterwindow, marker, acteur : Acteur):
        self.__class__.instances.append(self)
        self.masterwindow = masterwindow
        self.marker = marker
        self.acteur = acteur

        self.window = customtkinter.CTkToplevel()
        self.window.withdraw()
        self.window.overrideredirect(True)

        self.ajoutDonnees()


    @classmethod
    def hide(cls):
        for i in cls.instances:
            i.window.withdraw()


    # Garde la popup en bas à droite de l'écran
    def update_popup_position(self, event=None):
        if self.window.state() != 'withdrawn':
            self.window.geometry(
                "+%d+%d" % (self.masterwindow.winfo_rootx() + self.masterwindow.winfo_width() - self.window.winfo_width(),
                            self.masterwindow.winfo_rooty() + self.masterwindow.winfo_height() - self.window.winfo_height()))
            self.window.lift()


    # Permet d'ajouter les données du producteur (et des tâches associées par la suite) dans la popup
    def ajoutDonnees(self):
        if isinstance(self.acteur, Producteur):
            prod = self.acteur
            label = customtkinter.CTkLabel(self.window, text=str(prod), fg_color="transparent")
        elif isinstance(self.acteur, Client):
            client = self.acteur
            label = customtkinter.CTkLabel(self.window, text=str(client), fg_color="transparent")
        else:
            label = customtkinter.CTkLabel(self.window, text="Acteur inconnu", fg_color="transparent")

        label.grid(row=0, column=0, columnspan=1, padx=20, pady=10)

    def afficher(self):
        self.window.deiconify()
        # Force la mise à jour de l'interface utilisateur
        self.masterwindow.update_idletasks()
        # Ajoute un délai de 100 ms pour éviter le décalage entre le popup et la fenêtre principale
        self.update_popup_position() # Mettre un délai window.after()