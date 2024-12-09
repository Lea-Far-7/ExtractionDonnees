import os
import tkinter
import customtkinter
from Interface.PopUp import PopUp
from Modules.CreerClasses import CreerClasses


class PopupFiltre:
    """Pop-up pour la gestion des filtres"""

    def __init__(self, interface):

        # Initialise la popup
        self.popup = PopUp(interface)

        # Création de la Frame pour les Producteurs
        frame_prod = customtkinter.CTkScrollableFrame(self.popup.window, label_text="Producteurs")
        frame_prod.grid(row=0, column=0, padx=(10, 10), pady=(20, 0), sticky="nsew")

        # Création de la Frame pour les Clients
        frame_cl = customtkinter.CTkScrollableFrame(self.popup.window, label_text="Clients")
        frame_cl.grid(row=0, column=1, padx=(10, 10), pady=(20, 0), sticky="nsew")

        # Création de la Frame pour les DemiJours
        frame_dj = customtkinter.CTkScrollableFrame(self.popup.window, label_text="Date")
        frame_dj.grid(row=0, column=2, padx=(10, 10), pady=(20, 0), sticky="nsew")


        # Récupération des données s'il y en a et ajouts dans les Frame
        if interface.donnees:

            i = 0
            for prod in interface.donnees.getProducteurs():
                switch = customtkinter.CTkSwitch(master=frame_prod, progress_color="#1d7c69", text=repr(prod))
                switch.grid(row=i, column=0, padx=10, pady=(0, 20))
                i+=1

            i = 0
            for cl in interface.donnees.getClients():
                switch = customtkinter.CTkSwitch(master=frame_cl, progress_color="#1d7c69", text=repr(cl))
                switch.grid(row=i, column=0, padx=10, pady=(0, 20))
                i += 1

            #i = 0
            #for dj in data.getDemiJour():
            #    switch = customtkinter.CTkSwitch(master=frame_dj, progress_color="#1d7c69", text=repr(dj))
            #    switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            #    i += 1


        validButton = customtkinter.CTkButton(self.popup.window, fg_color="#1d7c69", hover_color="#275855",
                                                command=interface.valider, text="Valider")
        validButton.grid(row=9, column=0, columnspan=10, padx=20, pady=10)

        # Replace la pop-up au centre de la fenêtre principale
        self.popup.window.geometry("+%d+%d" % (
        (self.popup.masterwindow.winfo_rootx() + self.popup.masterwindow.winfo_width() / 2) - (
                    self.popup.window.winfo_width() * 1.25),
        (self.popup.masterwindow.winfo_rooty() + self.popup.masterwindow.winfo_height() / 2) - (
                    self.popup.window.winfo_height() * 1.25)))
        interface.wait_window(self.popup.window)