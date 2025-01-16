import customtkinter

# Un fichier de données, plusieurs fichiers de solutions. Peut-être importer un projet au lieu de Données et Solutions différents

class PopUp:
    """
    Cette classe est une base utilisée pour faire les popups d'import et de filtres.
    """
    def __init__(self, masterwindow):
        """
        Constructeur de la classe PopUp, créé une popup sans topbar et avec un bouton de fermeture de popup.
        :param masterwindow: Fenêtre principale.
        """
        super().__init__()

        # Récupération de l'interface mère
        self.masterwindow = masterwindow

        # Création d'une nouvelle fenêtre
        self.window = customtkinter.CTkToplevel()

        #Focus sur cette nouvelle fenêtre (cela désactive la fenêtre principale)
        self.window.grab_set()

        # Suppression de la topbar (Titre, Minimiser, Maximiser, Fermer)
        self.window.overrideredirect(True)

        def destroyWindow():
            self.window.destroy()


        self.sidebar_button_1 = customtkinter.CTkButton(self.window, fg_color="#1d7c69", hover_color="#275855", command=destroyWindow, text = "Fermer")
        self.sidebar_button_1.grid(row=10, column=0, columnspan=10, padx=20, pady=10)

        # Placement de la fenêtre à des coordonnées relatives à la fenêtre principale
        if self.masterwindow is not None:
            self.window.geometry("+%d+%d" % (self.masterwindow.winfo_rootx()+self.masterwindow.winfo_width()/2, self.masterwindow.winfo_rooty()+self.masterwindow.winfo_height()/2))