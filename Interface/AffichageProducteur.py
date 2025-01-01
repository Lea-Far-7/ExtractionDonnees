import customtkinter

from Metier.producteur import Producteur


class AffichageProducteur:

    instances = []

    def __init__(self, masterwindow, marker):
        self.__class__.instances.append(self)
        self.masterwindow = masterwindow
        self.marker = marker

        self.window = customtkinter.CTkToplevel()
        self.window.withdraw()
        self.window.overrideredirect(True)
        self.ajoutDonnees()

    # Permet de cacher les instances préexistantes pour éviter un amas de popups
    @classmethod
    def hide(cls,cls2):
        for i in cls.instances:
            i.window.withdraw()
        for i in cls2.instances:
            i.window.withdraw()

    # Garde la popup en bas à droite de l'écran
    def update_popup_position(self, event):
        self.window.geometry(
            "+%d+%d" % (self.masterwindow.winfo_rootx() + self.masterwindow.winfo_width() - self.window.winfo_width(),
                        self.masterwindow.winfo_rooty() + self.masterwindow.winfo_height() - self.window.winfo_height()))
        self.window.lift()

    # Permet d'ajouter les données du producteur (et des tâches associées par la suite) dans la popup
    def ajoutDonnees(self):
        # TODO : Continuer pour afficher les informations correspondantes
        prod = self.marker.prod
        partenaires = ""
        for partner in prod.partners:
            partenaires += partner.__repr__() + " "
        label = customtkinter.CTkLabel(self.window, text="Capacité : " + str(prod.capacity) + "\n"
                                        + "Partenaires : " + partenaires + "\n", fg_color="transparent")
        label.grid(row=0, column=0, columnspan=1, padx=20, pady=10)


    def afficher(self):
        self.window.geometry(
            "+%d+%d" % (self.masterwindow.winfo_rootx() + self.masterwindow.winfo_width() - self.window.winfo_width(),
                        self.masterwindow.winfo_rooty() + self.masterwindow.winfo_height() - self.window.winfo_height()))
        self.window.lift()

        # Dès que la fenêtre est modifiée (taille ou position) la popup est replacée au bon endroit
        self.masterwindow.bind('<Configure>', self.update_popup_position)
        self.window.deiconify()