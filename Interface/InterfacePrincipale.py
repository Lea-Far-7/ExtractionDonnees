import tkinter.messagebox
from time import strftime, gmtime
from tkinter import *
import os
from  tkinter import ttk

from folium.plugins import MarkerCluster
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk, ImageGrab
import customtkinter

from Interface.MarkerClient import MarkerClient
from Interface.MarkerProducteur import MarkerProducteur
from Interface.PopupFiltre import PopupFiltre
from Interface.PopupImport import PopupImport
from Metier.acteur import Acteur
from Metier.client import Client
from Modules.FileManager import FileManager
from Modules.CreerClasses import CreerClasses
from Modules.DataExtractor import DataExtractor

# Modes: "System", "Dark", "Light"
customtkinter.set_appearance_mode("Dark")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Définition des composants essentiels
        self.mark_list = []
        self.donnees = None
        self.person_var_name = {}
        self.tableau = None

        # Permet de mettre un titre et de définir la taille originale de la fenêtre
        self.title("OLOCAP Viewer")
        self.iconbitmap("../Images/Logo_Olocap_small.ico")
        self.geometry(f"{1100}x{580}")

        # Charge les images pour les icônes des producteurs et clients
        self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.image_client = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "../Images", "client.png")).resize((35, 35)))

        # Crée une Image mise dans un Label pour être affichée et contenue dans la sidebar
        self.my_image = customtkinter.CTkImage(light_image=Image.open("../Images/Logo_Olocap.png"), dark_image=Image.open("../Images/Logo_Olocap.png"), size=(192,58))

        # Mise en arrière définitive de la fenêtre (pour que les pop-ups puissent toujours se situer devant)
        self.attributes('-topmost',False)

        self.interfacePrincipale()

        self.creationCarte()
        self.creationTableau()

    def interfacePrincipale(self):
        # Permet de configurer la grid,
        # "weight = 1" permet de remplir au maximum l'espace de la grid désigné
        # "weight = 0" permet de réduire au minimum l'espace de la grid désigné

        self.grid_columnconfigure((1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((1, 2), weight=1)

        # Création de la zone contenant les boutons de gestion
        self.sidebar = customtkinter.CTkFrame(self, width=230, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # Création de l'image logo
        self.image_label = customtkinter.CTkLabel(self.sidebar, image=self.my_image, text=" ")
        self.image_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Utilisation d'une image contenant une seule couleur pour l'appliquer sur les boutons
        self.couleur_bouton = customtkinter.CTkImage(light_image=Image.open('../Images/Couleur_Boutons.png'),
                                                     size=(500, 150))

        # Création des boutons dans la sidebar
        self.importer = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855",
                                                command=lambda: PopupImport(self), text="Importer")
        self.importer.grid(row=1, column=0, padx=20, pady=10)
        self.filtre = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855",
                                              command=lambda: PopupFiltre(self), text="Filtres")
        self.filtre.grid(row=4, column=0, padx=20, pady=10)
        self.export = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855",
                                              command=self.screenshot, text="Export")
        self.export.grid(row=6, column=0, padx=20, pady=10)

        # Création des boutons de navigation entre la map et le tableau
        self.button_map = customtkinter.CTkButton(self, fg_color="#1d7c69", hover_color="#275855",
                                                  command=self.select_map, text="Carte")
        self.button_map.grid(row=0, column=2, sticky="e", padx=5, pady=5)

        self.button_tableau = customtkinter.CTkButton(self, fg_color="#1d7c69", hover_color="#275855",
                                                      command=self.select_tab, text="Tableau")
        self.button_tableau.grid(row=0, column=3, sticky="w", padx=5, pady=5)

    def creationCarte(self):
        # Création de la map et mise dans une grid (ligne 1 et colonne 1)
        self.map_widget = TkinterMapView()
        self.map_widget.grid(row=1, rowspan=8, column=1, columnspan=4, sticky="nsew")
        self.map_widget.set_zoom(8)

        # Définition de la position de départ
        self.map_widget.set_position(47.3565655, 0.7035767)

    def creationTableau(self):
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

        # Dissimulation du tableau
        self.tableau.grid_forget()

    # /!\ Attention, ici commence le code métier à bouger /!\
    # Valide le projet sélectionné
    def valider(self):
        if self.donnees_projet :
            # Supprime tous les marqueurs présent sur la map
            self.map_widget.delete_all_marker()
            self.mark_list.clear()

            # Créé une liste contenant toutes les informations du projet (Producteurs et Clients avec leurs informations respectives, pas le fichier solution)
            self.donnees = CreerClasses()
            self.donnees.load_donnees(self.donnees_projet)

            # Parcourt les producteurs créés et créé les marqueurs associés
            for producteur in self.donnees.getProducteurs():
                self.mark_list.append(MarkerProducteur(self.map_widget, producteur, self))

            # Parcourt les clients créés et créé les marqueurs associés
            for client in self.donnees.getClients():
                self.mark_list.append(MarkerClient(self.map_widget, client, self))


            # Lecture de choix de solutions en cours de construction, pas fonctionnel
            for selected in self.choixSolutions:
                if (selected.get() == 1) :
                    self.donnees.load_solutions(DataExtractor().extraction_solution(os.path.join(self.current_path, "../Projets/" + self.projet_selected +"/Solutions/"+ selected.cget('text'))))

            for tournee in self.donnees.getTournees():
                if tournee.producteur.id == 1:
                    pass



    def assignProjet(self, projet, frame_solutions):

        # Détruit les objets précédemment créés dans la ScrollableFrame où sont contenues les solutions
        for widget in frame_solutions.winfo_children():
            widget.destroy()

        # Remets la liste des solutions à vide
        self.choixSolutions = []

        # Récupère la liste des fichiers solutions dans le projet sélectionné
        self.liste_fichiers_solutions = FileManager().lister_fichiers(
            os.path.join(self.current_path, "../Projets/" + projet + "/Solutions"))

        # Récupère le fichier données dans le projet sélectionné
        fichier_donnees = FileManager().lister_fichiers(
            os.path.join(self.current_path, "../Projets/" + projet))

        # Extrait les données du fichier de données du projet
        self.donnees_projet = DataExtractor().extraction(os.path.join(self.current_path, "../Projets/" + projet +"/"+ fichier_donnees[0]))

        self.projet_selected = projet

        # Créé les différents Switchs permettant de selectionner les boutons et les ajoute dans
        # l'attribut contenant les différents noms des fichiers solution
        liste_solutions = {}
        j = 0
        for solutions in self.liste_fichiers_solutions:
            liste_solutions[solutions] = customtkinter.CTkSwitch(master=frame_solutions, progress_color="#1d7c69",
                                                                     text=f"{solutions}")
            liste_solutions[solutions].grid(row=j, column=0, padx=10, pady=(0, 20))
            self.choixSolutions.append(liste_solutions[solutions])
            j = j + 1

    def screenshot(self):
        bbox = (self.map_widget.winfo_rootx(), self.map_widget.winfo_rooty(), self.map_widget.winfo_rootx()+self.map_widget.winfo_width(), self.map_widget.winfo_rooty()+self.map_widget.winfo_height())

        # Capture the screenshot
        screenshot = ImageGrab.grab(bbox)

        # Save the screenshot
        screenshot.save('../Exports/Screenshot_'+strftime("%Y%m%d_%H%M%S", gmtime())+'.png')

        tkinter.messagebox.showinfo(title="Information", message="Image enregistrée")

    def showDataLine(self,line):
        if line.name != "" and line.name is not None:
            line.name = ""
        else :
            line.name = "Infos : \nInfos : \nInfos : \nInfos : \nInfos : \nInfos : \nInfos : \n"

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

