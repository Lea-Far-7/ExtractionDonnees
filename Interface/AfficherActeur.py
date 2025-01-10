import customtkinter

from Metier.ObserverActeur import ObserverActeur
from Metier.acteur import Acteur

class AfficherActeur(ObserverActeur):

    instances = []

    def __init__(self, masterwindow, marker, acteur : Acteur):
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
        for i in cls.instances:
            i.window.withdraw()


    # Garde la popup en bas à droite de l'écran
    def update_popup_position(self, event=None):
        if self.window.state() != 'withdrawn':
            self.window.geometry(
                "+%d+%d" % (self.masterwindow.winfo_rootx() + self.masterwindow.winfo_width() - self.window.winfo_width(),
                            self.masterwindow.winfo_rooty() + self.masterwindow.winfo_height() - self.window.winfo_height()))
            self.window.lift()


    # Appel effectué à chaque fois qu'infoTournees de l'acteur change
    def update(self):
        newtext = str(self.acteur)
        infosTournees = self.acteur.getInfosTournees()
        if infosTournees != "":
            newtext += "\n\n" + infosTournees
        self.label.configure(text = newtext)
        self.label.update()


    def afficher(self):
        self.window.deiconify()

        # Force la mise à jour de l'interface utilisateur
        self.masterwindow.update_idletasks()

        # Ajoute un délai de 100 ms pour éviter le décalage entre le popup et la fenêtre principale
        self.update_popup_position() # Mettre un délai window.after()