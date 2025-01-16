import customtkinter
from Interface.AfficherActeur import AfficherActeur

class AfficherTrajet():
    """
    Cette classe permet d'afficher les trajets entre un point A et un point B
    à partir de la tâche et du trajet passé en paramètre
    """
    instances = []


    def __init__(self, masterwindow, trajet, tache):
        """
        L'initialisation permet de rentrer les données passées en paramètres.
        :param masterwindow: Fenêtre principale.
        :param trajet: Objet TrajetTache contenant le tracé du trajet ainsi que les informations des tâches.
        :param tache: Objet métier contenant des informations affichées plus loin.
        """
        self.__class__.instances.append(self)

        self.masterwindow = masterwindow
        self.trajet = trajet
        self.tache = tache

        self.window = customtkinter.CTkToplevel()
        self.window.withdraw()
        self.window.overrideredirect(True)

        text = ("Objectif : " + str(tache) + " " + repr(self.trajet.tournee.demiJour) + " par " + repr(self.trajet.tournee.producteur)
                + "\nCharge transportée : "+str(round(self.trajet.chargement,2))+" kg"
                + "\nDistance : "+str(round(self.trajet.distance,2))+" km"
                + "\nDurée : "+str(round(self.trajet.duree,2))+" min")

        self.label = customtkinter.CTkLabel(self.window, text=text, fg_color="transparent")
        self.label.grid(row=0, column=0, columnspan=1, padx=20, pady=10)


    @classmethod
    def hide(cls):
        """
        Permet de cacher les informations affichées après un clic sur le trajet.
        :param cls: La classe concernée.
        """
        for i in cls.instances:
            if hasattr(i, 'window') and i.window.winfo_exists():
                i.window.withdraw()
        AfficherActeur.hide()

    # Garde la popup en bas à droite de l'écran
    def update_popup_position(self, event=None):
        """
        Permet de garder l'affichage en bas à droite de la fenêtre.
        :param event: L'évènement concernant l'affichage, non-utilisé ici.
        """
        if hasattr(self, 'window') and self.window.winfo_exists():#self.window.state() != 'withdrawn':
            self.window.geometry(
                "+%d+%d" % (self.masterwindow.winfo_rootx() + self.masterwindow.winfo_width() - self.window.winfo_width(),
                            self.masterwindow.winfo_rooty() + self.masterwindow.winfo_height() - self.window.winfo_height()))
            self.window.lift()

    def afficher(self):
        """
        Permet l'affichage de la popup d'information en bas à droite.
        """
        self.window.deiconify()
        # Force la mise à jour de l'interface utilisateur
        self.masterwindow.update_idletasks()
        # Ajoute un délai de 100 ms pour éviter le décalage entre le popup et la fenêtre principale
        self.update_popup_position() # Mettre un délai window.after()