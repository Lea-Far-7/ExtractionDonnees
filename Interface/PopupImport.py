import os
import tkinter
import customtkinter
from Interface.PopUp import PopUp
from Modules.FileManager import FileManager


# Création d'une pop-up et inclusion d'éléments pour l'importation de fichiers
class PopupImport():
    def __init__(self, interface): # Ajouter createur en parametre / attribut

        #Initialise la popup
        self.popup = PopUp(interface)


        # Création de la Frame contenant les RadioButtons
        scrollable_frame = customtkinter.CTkScrollableFrame(self.popup.window, label_text="Projets")
        scrollable_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        radio_var = tkinter.IntVar(value=0)


        # Récupère le chemin des fichiers de données et de solutions associées
        liste_dossiers_projets = FileManager().lister_dossiers(os.path.join(interface.current_path, "../Projets"))

        # Génère la Frame qui va contenir les Switchs
        frame_solutions = customtkinter.CTkScrollableFrame(self.popup.window, label_text="Fichiers Solution Associés")
        frame_solutions.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # Créé la liste des projets
        liste_projets = {}
        i = 0
        for projet in liste_dossiers_projets:
            liste_projets[projet] = customtkinter.CTkRadioButton(master=scrollable_frame, fg_color="#1d7c69", hover_color="#275855", variable=radio_var, value=i+1, text=f"{projet}", command=lambda p=projet: interface.assignProjet(p,frame_solutions))
            liste_projets[projet].grid(row=i, column=0, padx=10, pady=(0, 20))
            i = i + 1

        boutonValider = customtkinter.CTkButton(self.popup.window, fg_color="#1d7c69", hover_color="#275855", command=interface.valider, text="Valider")
        boutonValider.grid(row=9, column=0, columnspan=10, padx=20, pady=10)


        #Replace la pop-up au centre de la fenêtre principale
        self.popup.window.geometry("+%d+%d" % ((self.popup.masterwindow.winfo_rootx() + self.popup.masterwindow.winfo_width() / 2)-(self.popup.window.winfo_width()*1.5),
                (self.popup.masterwindow.winfo_rooty() + self.popup.masterwindow.winfo_height() / 2)-(self.popup.window.winfo_height()*1.25)))
        interface.wait_window(self.popup.window)