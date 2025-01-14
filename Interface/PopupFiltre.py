import customtkinter

from Interface.Createur import Createur
from Interface.PopUp import PopUp
from Metier.acteur import Acteur
from Modules.ListeDemiJours import ListeDemiJours
from Modules.extractRange import extractRange
from Modules.filtres import filtreTournees, filtreActeurs


class PopupFiltre:
    """Pop-up pour la gestion des filtres"""

    def __init__(self, interface, createur : Createur):

        self.interface = interface
        self.createur = createur
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
        if self.createur.projet:

            producteurs, clients = self.createur.getActeurs(self.interface.donnees, self.createur.projet)
            i = 0
            for prod in producteurs:
                switch = customtkinter.CTkSwitch(master=frame_prod, progress_color="#1d7c69", text=repr(prod))
                switch.grid(row=i, column=0, padx=10, pady=(0, 20))
                self.switch_prod[prod.id] = switch
                i+=1

            i = 0
            for cl in clients:
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

        # Création du menu déroulant pour choisir un fichier de tournées (solution) en particulier
        self.menu_solutions = customtkinter.CTkOptionMenu(self.popup.window, values=["tous les fichiers solution"]+self.interface.solutions_selectionnees,
            fg_color="#1d7c69", button_color="#1d7c69", button_hover_color="#275855")
        self.menu_solutions.grid(row=1, column=2, padx=10)

        validButton = customtkinter.CTkButton(self.popup.window, fg_color="#1d7c69", hover_color="#275855",
                                                command=self.__validate, text="Valider")
        validButton.grid(row=3, column=0, columnspan=3, padx=20, pady=10)

        # Replace la pop-up au centre de la fenêtre principale
        self.popup.window.geometry("+%d+%d" % (
        (self.popup.masterwindow.winfo_rootx() + self.popup.masterwindow.winfo_width() / 2) - (
                    self.popup.window.winfo_width() * 1.25),
        (self.popup.masterwindow.winfo_rooty() + self.popup.masterwindow.winfo_height() / 2) - (
                    self.popup.window.winfo_height() * 1.25)))
        interface.wait_window(self.popup.window)



    def __validate(self):

        producteurs_id = []
        clients_id = []
        demi_jours_num = []

        filtrage_text_prod = self.entry_prod.get()
        filtrage_text_cl = self.entry_cl.get()
        filtrage_solution = self.menu_solutions.get()

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
            for key, switch in self.switch_cl.items():
                if switch.get():
                    clients_id.append(key)

        # Récupération des demi-jours à filtrer : sélection par les switch
        for key, switch in self.switch_dj.items():
            if switch.get():
                demi_jours_num.append(key)


        # Récupération des tournées
        tournees = []
        tournees_pre_filtrees = [] # contient les tournées d'un seul ou tous les fichiers solutions
        for nom_fichier in self.interface.solutions_selectionnees:
            fichier = self.interface.solutions[nom_fichier]
            list_tournees = self.createur.getTournees(fichier, nom_fichier)
            tournees.extend(list_tournees)
            if filtrage_solution == nom_fichier:
                tournees_pre_filtrees.extend(list_tournees)


        # Filtrage des tournées
        if filtrage_solution == "tous les fichiers solution":
            tournees_filtrees = filtreTournees(tournees, producteurs_id, clients_id, demi_jours_num)
        else:
            tournees_filtrees = filtreTournees(tournees_pre_filtrees, producteurs_id, clients_id, demi_jours_num)

        # Filtrage des acteurs
        acteurs_select = producteurs_id+clients_id
        acteurs_filtres = filtreActeurs(tournees_filtrees, acteurs_select)


        # Mise à jour des conditions d'affichage dans le tableau
        self.interface.afficheurTableau.acteurs_id_filtres = acteurs_select
        self.interface.afficheurTableau.tournees_filtrees = tournees_filtrees


        # Mise à jour de l'affichage des acteurs sur la carte
        for id, acteur_marker in self.interface.mark_list.items():
            if id in acteurs_filtres:
                # montrer
                acteur_marker.show_marker()
            else:
                # cacher
                acteur_marker.hide_marker()


        # Mise à jour de l'affichage des trajets sur la carte
        for tournee in tournees:
            if tournee in tournees_filtrees:
                # montrer tous les trajets (tâches) de la tournée
                # mais avant on vérifie si le 1er trajet n'est pas déjà montré pour éviter de parcourir inutilement
                if self.interface.path_list[tournee.taches[0]].trajet_hidden:
                    for tache in tournee.taches:
                        self.interface.path_list[tache].show_trajet()
            else:
                # cacher tous les trajets (tâches) de la tournée
                # mais avant on vérifie si le 1er trajet n'est pas déjà caché pour éviter de parcourir inutilement
                if not self.interface.path_list[tournee.taches[0]].trajet_hidden:
                    for tache in tournee.taches:
                        self.interface.path_list[tache].hide_trajet()


        # Mise à jour des infosTournees des acteurs
        Acteur.updateInfosTournees([tournees_filtrees])

        #tests
        print("Tournées filtrées :", tournees_filtrees)
        print("ID Acteurs filtrés :", acteurs_filtres)