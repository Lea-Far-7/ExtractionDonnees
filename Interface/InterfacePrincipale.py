from tkinter import *
import tkinter
import os
from  tkinter import ttk
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk
import customtkinter
from Interface.PopUp import PopUp
from Modules.FileManager import FileManager

# Modes: "System", "Dark", "Light"
customtkinter.set_appearance_mode("Dark")

# Thèmes: "blue", "green", "dark-blue"
customtkinter.set_default_color_theme("blue")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Permet de mettre un titre et de définir la taille originale de la fenêtre
        self.title("OLOCAP Viewer")
        self.iconbitmap("../Images/Logo_Olocap_small.ico")
        self.geometry(f"{1100}x{580}")

        # Charge les images pour les icônes des producteurs et clients
        self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.image_client = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "../Images", "client.png")).resize((35, 35)))
        self.image_producteur = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "../Images", "producteur.png")).resize((35, 35)))

        self.popup = None
        # Création d'une pop-up et inclusion d'éléments pour l'importation de fichiers
        def popupImportCreate():

            #Initialise la popup
            self.popup = PopUp(self)



            # Création de la Frame contenant les RadioButtons
            scrollable_frame = customtkinter.CTkScrollableFrame(self.popup.window, label_text="Projets")
            scrollable_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
            radio_var = tkinter.IntVar(value=0)

            """
            # Récupère le chemin des fichiers de données et de solutions associées
            liste_fichiers_donnees = FileManager().lister_fichiers(os.path.join(self.current_path, "../Projets"))
            liste_fichiers_solutions = FileManager().lister_fichiers(os.path.join(self.current_path, "../Projets/Solutions"))
            print(liste_fichiers_donnees)
            print(liste_fichiers_solutions)
            
            # Créé la liste des solutions (à changer pour créer la liste des projets)
            projets = {}
            i = 0
            for projet in liste_fichiers:
                projets[projet] = customtkinter.CTkRadioButton(master=scrollable_frame, fg_color="#1d7c69", hover_color="#275855", variable=radio_var, value=i, text=f"{projet}")
                projets[projet].grid(row=i, column=0, padx=10, pady=(0, 20))
                i = i + 1

            print(projets[liste_fichiers[0]].cget("text"))
            """


            """
            # Génère temporairement toutes les RadioButtons
            for i in range(1,11,1):
                radio = customtkinter.CTkRadioButton(master=scrollable_frame, fg_color="#1d7c69", hover_color="#275855", variable=radio_var, value=i, text=f"Projet {i}")
                radio.grid(row=i, column=0, padx=10, pady=(0, 20))
            """

            # Génère la Frame qui va contenir les Switchs
            scrollable_frame2 = customtkinter.CTkScrollableFrame(self.popup.window, label_text="Fichiers Solution Associés")
            scrollable_frame2.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
            scrollable_frame_choices = []

            # Génère temporairement tous les Switchs
            for i in range(10):
                switch = customtkinter.CTkSwitch(master=scrollable_frame2, progress_color="#1d7c69", text=f"Solution {i+1}")
                switch.grid(row=i, column=0, padx=10, pady=(0, 20))
                scrollable_frame_choices.append(switch)



            #Replace la pop-up au centre de la fenêtre principale
            self.popup.window.geometry("+%d+%d" % ((self.popup.masterwindow.winfo_rootx() + self.popup.masterwindow.winfo_width() / 2)-(self.popup.window.winfo_width()*1.5),
                           (self.popup.masterwindow.winfo_rooty() + self.popup.masterwindow.winfo_height() / 2)-(self.popup.window.winfo_height()*1.25)))
            self.wait_window(self.popup.window)

        # Affiche les données des markers et les caches si deuxième clic
        def showDataMarker(marker):
            if marker.text != "" and marker.text is not None:
                marker.set_text("")
            else :
                marker.set_text("Infos : \nInfos : \nInfos : \nInfos : \nInfos : \nInfos : \nInfos : \n")

        def showDataLine(line):
            if line.name != "" and line.name is not None:
                line.name = ""
            else :
                line.name = "Infos : \nInfos : \nInfos : \nInfos : \nInfos : \nInfos : \nInfos : \n"



        # Mise en arrière définitive de la fenêtre (pour que les pop-ups puissent toujours se situer devant)
        self.attributes('-topmost',False)

        # Permet de configurer la grid,
        # "weight = 1" permet de remplir au maximum l'espace de la grid désigné
        # "weight = 0" permet de réduire au minimum l'espace de la grid désigné

        self.grid_columnconfigure((1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((1, 2), weight=1)

        # Création de la zone contenant les boutons de gestion
        self.sidebar = customtkinter.CTkFrame(self, width=230, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # Crée une Image mise dans un Label pour être affichée et contenue dans la sidebar
        self.my_image = customtkinter.CTkImage(light_image=Image.open("../Images/Logo_Olocap.png"), dark_image=Image.open("../Images/Logo_Olocap.png"), size=(192,58))

        self.image_label = customtkinter.CTkLabel(self.sidebar, image=self.my_image, text=" ")
        self.image_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.couleur_bouton = customtkinter.CTkImage(light_image=Image.open('../Images/Couleur_Boutons.png'), size=(500, 150))

        # Création des boutons dans la sidebar ( soit popupImportCreate, soit importVer2)
        self.importer = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855", command= popupImportCreate , text = "Importer")
        self.importer.grid(row=1, column=0, padx=20, pady=10)

        self.filtre = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855",  command=self.sidebar_button_event, text = "Filtres")
        self.filtre.grid(row=4, column=0, padx=20, pady=10)

        self.export = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855", command=self.sidebar_button_event, text = "Export")
        self.export.grid(row=6, column=0, padx=20, pady=10)

        self.ajout = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855", command=self.sidebar_button_event, text = "Ajout")
        self.ajout.grid(row=7, column=0, padx=20, pady=10)

        self.supprime = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855", command=self.sidebar_button_event, text = "Supprimer")
        self.supprime.grid(row=8, column=0, padx=20, pady=10)

        # Création des boutons de navigation entre la map et le tableau
        self.button_map = customtkinter.CTkButton(self, fg_color="#1d7c69", hover_color="#275855", command=self.select_map, text="Carte")
        self.button_map.grid(row=0, column=2, sticky="e", padx=5, pady=5)

        self.button_tableau = customtkinter.CTkButton(self, fg_color="#1d7c69", hover_color="#275855", command=self.select_tab, text="Tableau")
        self.button_tableau.grid(row=0, column=3, sticky="w", padx=5, pady=5)

        # Création de la map et mise dans une grid (ligne 1 et colonne 1)
        self.map_widget = TkinterMapView()
        self.map_widget.grid(row=1, rowspan=8, column=1, columnspan=4, sticky="nsew")

        # Définition de la position de départ
        self.map_widget.set_position(47.3565655, 0.7035767)

        #Défintion de valeurs de test (deux marqueurs et une ligne les reliant)
        self.pos1 = self.map_widget.set_marker(47.3565655, 0.7035767, icon=self.image_client, command=showDataMarker)
        self.pos2 = self.map_widget.set_marker(47.3561294, 0.6977163, icon=self.image_producteur, command=showDataMarker)

        self.traj1 = self.map_widget.set_path([self.pos2.position, self.pos1.position],color="#1d7c69", command=showDataLine)

        # Création du tableau
        self.tableau = ttk.Treeview()
        self.tableau['columns'] = ["Producteur","Client","Poids Maximal","Demi-Jour travaillé ?","Autre"]

        self.tableau.column("#0",width=0, stretch=NO)
        self.tableau.column("Producteur", width=80, anchor = CENTER)
        self.tableau.column("Client", width=80, anchor = CENTER)
        self.tableau.column("Poids Maximal", width=80, anchor = CENTER)
        self.tableau.column("Demi-Jour travaillé ?", width=80, anchor = CENTER)
        self.tableau.column("Autre", width=80, anchor = CENTER)

        self.tableau.heading("Producteur", text="Producteur")
        self.tableau.heading("Client", text="Client")
        self.tableau.heading("Poids Maximal", text="Poids Maximal")
        self.tableau.heading("Demi-Jour travaillé ?", text="Demi-Jour travaillé ?")
        self.tableau.heading("Autre", text="Autre")

        # Jeu de données temporaires
        self.tableau.insert(parent='',index='end',iid=0,text='',values=('0','Test','101','Test2', 'efguazielgf'))
        for i in range(0,50,1):
            self.tableau.insert(parent='',index='end',iid=i+1,text='',values=(i+1,'Test','101','Test', 'Moore'))
        self.tableau.insert(parent='',index='end',iid=51,text='',values=('51','Test','101','Test2', 'efguazielgf'))

        # Dissimulation du tableau
        self.tableau.grid_forget()


    # Evenement temporaire declenché par appui sur bouton
    def sidebar_button_event(self):
        print("Clic bouton")

    # Evenement permettant d'afficher le tableau tout en cachant la map
    def select_tab(self) :
        self.tableau.grid(row=1, rowspan=8, column=1, columnspan=4, sticky="nsew")
        self.map_widget.grid_forget()

    # Evenement permettant d'afficher la map tout en cachant le tableau
    def select_map(self) :
        self.map_widget.grid(row=1, rowspan=8, column=1, columnspan=4, sticky="nsew")
        self.tableau.grid_forget()

if __name__ == "__main__":
    app = App()
    app.mainloop()

