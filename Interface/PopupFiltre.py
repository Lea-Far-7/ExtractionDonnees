import customtkinter
from Interface.PopUp import PopUp
from Modules.ListeDemiJours import ListeDemiJours
from Modules.extractRange import extractRange
from Modules.filtres import filtreTournees


class PopupFiltre:
    """Pop-up pour la gestion des filtres"""

    def __init__(self, interface):

        self.interface = interface
        self.switch_prod = {}
        self.switch_cl = {}
        self.switch_dj = {}

        # Initialise la popup
        self.popup = PopUp(interface)

        # Création de la Frame pour les Producteurs
        frame_prod = customtkinter.CTkScrollableFrame(self.popup.window, label_text="Producteurs")
        frame_prod.grid(row=0, column=0, padx=10, pady=20, sticky="nsew")

        # Création de la Frame pour les Clients
        frame_cl = customtkinter.CTkScrollableFrame(self.popup.window, label_text="Clients")
        frame_cl.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")

        # Création de la Frame pour les DemiJours
        frame_dj = customtkinter.CTkScrollableFrame(self.popup.window, label_text="Date")
        frame_dj.grid(row=0, column=2, padx=10, pady=20, sticky="nsew")


        # Champ textuel de filtrage pour les Producteurs
        self.entry_prod = customtkinter.CTkEntry(self.popup.window, placeholder_text="par exemple : 1-5, 8, 11-13")
        self.entry_prod.grid(row=1, column=0, padx=20, pady=(0,10), sticky="nsew")

        # Champ textuel de filtrage pour les Producteurs
        self.entry_cl = customtkinter.CTkEntry(self.popup.window, placeholder_text="par exemple : 1-5, 8, 11-13")
        self.entry_cl.grid(row=1, column=1, padx=20, pady=(0,10), sticky="nsew")


        # Récupération des données s'il y en a et ajouts dans les Frame
        if interface.donnees:

            i = 0
            for prod in interface.donnees.getProducteurs():
                switch = customtkinter.CTkSwitch(master=frame_prod, progress_color="#1d7c69", text=repr(prod))
                switch.grid(row=i, column=0, padx=10, pady=(0, 20))
                self.switch_prod[prod.id] = switch
                i+=1

            i = 0
            for cl in interface.donnees.getClients():
                switch = customtkinter.CTkSwitch(master=frame_cl, progress_color="#1d7c69", text=repr(cl))
                switch.grid(row=i, column=0, padx=10, pady=(0, 20))
                self.switch_cl[cl.id] = switch
                i += 1

            i = 0
            for dj in ListeDemiJours.getlisteDJ():
                switch = customtkinter.CTkSwitch(master=frame_dj, progress_color="#1d7c69", text=repr(dj))
                switch.grid(row=i, column=1, padx=10, pady=(0, 20), sticky="w")
                self.switch_dj[dj.num] = switch
                i += 1


        validButton = customtkinter.CTkButton(self.popup.window, fg_color="#1d7c69", hover_color="#275855",
                                                command=self.validate, text="Valider")
        validButton.grid(row=3, column=0, columnspan=3, padx=20, pady=10)

        # Replace la pop-up au centre de la fenêtre principale
        self.popup.window.geometry("+%d+%d" % (
        (self.popup.masterwindow.winfo_rootx() + self.popup.masterwindow.winfo_width() / 2) - (
                    self.popup.window.winfo_width() * 1.25),
        (self.popup.masterwindow.winfo_rooty() + self.popup.masterwindow.winfo_height() / 2) - (
                    self.popup.window.winfo_height() * 1.25)))
        interface.wait_window(self.popup.window)



    def validate(self):

        producteurs_id = []
        clients_id = []
        demi_jours_num = []

        filtrage_text_prod = self.entry_prod.get()
        filtrage_text_cl = self.entry_cl.get()

        # Récupération des producteurs à filtrer
        if filtrage_text_prod != "":
            # Sélection par le champ textuel dédié
            producteurs_id = extractRange(filtrage_text_prod)
            # Mise à jour des switch en fonction des plages sélectionnées
            for key, switch in self.switch_prod.items():
                if key in producteurs_id:
                    switch.select()
                else:
                    switch.deselect()
        else:
            # Sélection par les switch
            for key, switch in self.switch_prod.items():
                if switch.get():
                    producteurs_id.append(key)

        # Récupération des clients à filtrer
        if filtrage_text_cl != "":
            # Sélection par le champ textuel dédié
            clients_id = extractRange(filtrage_text_cl)
            # Mise à jour des switch en fonction des plages sélectionnées
            for key, switch in self.switch_cl.items():
                if key in clients_id:
                    switch.select()
                else:
                    switch.deselect()
        else:
            # Sélection par les switch
            for key, switch in self.switch_prod.items():
                if switch.get():
                    clients_id.append(key)

        # Récupération des demi-jours à filtrer : sélection par les switch
        for key, switch in self.switch_dj.items():
            if switch.get():
                demi_jours_num.append(key)

        # Filtrage des tournées
        # tourneesF = filtreTournees(..., producteurs_id, clients_id, demi_jours_num)

        #TODO: Implémenter la sélection des tournées, des producteurs et des clients à faire apparaitre