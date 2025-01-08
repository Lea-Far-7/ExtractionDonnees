import tkinter.messagebox
from time import strftime, gmtime
from tkinter import *
from  tkinter import ttk

from tkintermapview import TkinterMapView
from PIL import Image, ImageGrab
import customtkinter

from Interface.AfficherTableau import AfficherTableau
from Interface.Createur import Createur
from Interface.PopupFiltre import PopupFiltre
from Interface.PopupImport import PopupImport

# Modes: "System", "Dark", "Light"
customtkinter.set_appearance_mode("Dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.tableau_frame = None
        self.sidebar = None
        self.createur = Createur()
        self.afficheurTableau = AfficherTableau(self)

        # Définition des composants essentiels
        self.map_widget = None
        self.tableau = None
        self.mark_list = {} # dictionnaire des marqueurs
        self.path_list = {} # dictionnaire des trajets
        self.donnees = [] # liste des lignes du fichier
        self.solution = [] # liste de liste des lignes de chaque fichier solution (si plusieurs sont sélectionnés)
        self.solutions_selectionnees = []

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL)

        # Permet de mettre un titre et de définir la taille originale de la fenêtre
        self.title("OLOCAP Viewer")
        self.iconbitmap("../Images/Logo_Olocap_small.ico")
        self.geometry(f"{1100}x{580}")

        # Crée une Image mise dans un Label pour être affichée et contenue dans la sidebar
        self.my_image = customtkinter.CTkImage(light_image=Image.open("../Images/Logo_Olocap.png"), dark_image=Image.open("../Images/Logo_Olocap.png"), size=(192,58))

        # Mise en arrière définitive de la fenêtre (pour que les pop-ups puissent toujours se situer devant)
        self.attributes('-topmost', False)

        # Insertion des éléments de l'interface
        self.interfacePrincipale()
        self.creationCarte()
        self.creationTableau()

        # Ajout du menu déroulant permettant de choisir le tableau
        self.options = ["Producteurs, Clients, Commandes"]
        self.option_selectionnee = tkinter.StringVar()
        self.menu_donnees = customtkinter.CTkOptionMenu(self.sidebar, fg_color="#1d7c69", button_hover_color="#275855",
                                                        variable=self.option_selectionnee,
                                                        values=self.options,
                                                        command=self.update_menu)
        self.menu_donnees.grid(row=10, column=0, sticky="w", padx=20, pady=10)
        self.menu_donnees.grid_forget() # On est sur la carte par défaut donc on masque le menu initialement

        # Ajout du menu déroulant permettant de choisir le fichier solution à visualiser dans le tableau
        self.options_solution = [] # Au début aucun fichier sélectionné donc aucune option
        self.option_solution_selectionnee = tkinter.StringVar()
        self.menu_solutions = customtkinter.CTkOptionMenu(self.sidebar, fg_color="#1d7c69", button_hover_color="#275855",
                                                          variable=self.option_solution_selectionnee,
                                                          values=self.options_solution,
                                                          command=self.update_menu_solutions)
        self.menu_solutions.grid(row=12, column=0, sticky="w", padx=20, pady=10)
        self.menu_solutions.grid_forget()

        # Lier l'événement de configuration pour mettre à jour les popups
        self.bind('<Configure>', self.update_all_popups_position)

    def update_all_popups_position(self, event=None):
        for marker in self.mark_list.values():
            marker.popup.update_popup_position()


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
        image_label = customtkinter.CTkLabel(self.sidebar, image=self.my_image, text=" ")
        image_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Utilisation d'une image contenant une seule couleur pour l'appliquer sur les boutons
        couleur_bouton = customtkinter.CTkImage(light_image=Image.open('../Images/Couleur_Boutons.png'),
                                                     size=(500, 150))

        # Création des boutons dans la sidebar
        importer = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855",
                                                command=lambda: PopupImport(self, self.createur), text="Importer")
        importer.grid(row=1, column=0, padx=20, pady=10)
        filtre_bouton = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855",
                                              command=lambda: PopupFiltre(self, self.createur), text="Filtres")
        filtre_bouton.grid(row=4, column=0, padx=20, pady=10)
        export_bouton = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855",
                                              command=self.screenshot, text="Export")
        export_bouton.grid(row=6, column=0, padx=20, pady=10)

        # Création des boutons de navigation entre la map et le tableau
        button_map = customtkinter.CTkButton(self, fg_color="#1d7c69", hover_color="#275855",
                                                  command=self.select_map, text="Carte")
        button_map.grid(row=0, column=2, sticky="e", padx=5, pady=5)

        button_tableau = customtkinter.CTkButton(self, fg_color="#1d7c69", hover_color="#275855",
                                                      command=self.select_tab, text="Tableau")
        button_tableau.grid(row=0, column=3, sticky="w", padx=5, pady=5)

    def creationCarte(self):
        # Création de la map et mise dans une grid (ligne 1 et colonne 1)
        self.map_widget = TkinterMapView()
        self.map_widget.grid(row=1, rowspan=8, column=1, columnspan=4, sticky="nsew")
        self.map_widget.set_zoom(8)

        # Définition de la position de départ
        self.map_widget.set_position(47.3565655, 0.7035767)

    def creationTableau(self):
        # Créer un frame conteneur pour le tableau
        self.tableau_frame = customtkinter.CTkFrame(self)
        self.tableau_frame.grid(row=1, rowspan=8, column=1, columnspan=4, sticky="nsew")

        # Permet l'extension du tableau sur toute la longueur du frame
        self.tableau_frame.grid_columnconfigure(0, weight=1)
        self.tableau_frame.grid_rowconfigure(0, weight=1)

        self.afficheurTableau.tableau_vide()

        self.tableau_frame.grid_forget()

    def screenshot(self):
        bbox = (self.map_widget.winfo_rootx(), self.map_widget.winfo_rooty(), self.map_widget.winfo_rootx()+self.map_widget.winfo_width(), self.map_widget.winfo_rooty()+self.map_widget.winfo_height())

        # Capture the screenshot
        screenshot = ImageGrab.grab(bbox)

        # Save the screenshot
        screenshot.save('../Exports/Screenshot_'+strftime("%Y%m%d_%H%M%S", gmtime())+'.png')

        tkinter.messagebox.showinfo(title="Information", message="Image enregistrée")

    # Evenement permettant d'afficher le tableau tout en cachant la map
    def select_tab(self) :
        self.map_widget.grid_forget()
        self.tableau_frame.grid(row=1, rowspan=8, column=1, columnspan=4, sticky="nsew")

        if self.mark_list :
            for mark in self.mark_list.values():
                mark.hide()

        # On affiche la scrollbar pour le tableau
        self.scrollbar.grid(row=1, rowspan=8, column=5, sticky="ns")
        # On affiche le menu déroulant pour choisir le tableau
        self.menu_donnees.grid()
        # Mise à jour des options
        self.update_options_menu()

    # Evenement permettant d'afficher la map tout en cachant le tableau
    def select_map(self) :
        self.tableau_frame.grid_forget()
        self.map_widget.grid(row=1, rowspan=8, column=1, columnspan=4, sticky="nsew")

        # On cache la scrollbar du tableau
        self.scrollbar.grid_forget()
        # On cache les menus déroulants du tableau
        self.menu_donnees.grid_forget()
        self.menu_solutions.grid_forget()

    def update_options_menu(self):
        if self.solutions_selectionnees:
            self.options = ["Producteurs", "Clients", "Commandes", "Tournées"]
        else:
            self.options = ["Producteurs", "Clients", "Commandes"]
        self.menu_donnees.configure(values=self.options)

    def update_options_menu_solutions(self):
        if self.solutions_selectionnees:
            self.options_solution = self.solutions_selectionnees
            self.menu_solutions.configure(values=self.options_solution)

    def update_menu(self, choix):
        producteurs, clients = self.createur.getActeurs(self.donnees, self.createur.projet)
        commandes = self.createur.getCommandes()

        # On cache le menu solutions par défaut
        self.menu_solutions.grid_forget()

        if choix == "Producteurs" :
            self.afficheurTableau.tableau_producteurs(producteurs)
        elif choix == "Clients" :
            self.afficheurTableau.tableau_clients(clients)
        elif choix == "Commandes" :
            self.afficheurTableau.tableau_commandes(commandes)
        elif choix == "Tournées" :
            # On affiche le menu solution
            self.update_options_menu_solutions()
            self.menu_solutions.grid()

    def update_menu_solutions(self, choix):
        if choix:   # Si une solution est sélectionnée
            index = self.solutions_selectionnees.index(choix)
            if 0 <= index < len(self.solution):
                liste_tournees = self.createur.getTournees(self.solution[index])
                self.afficheurTableau.tableau_tournees(liste_tournees)


if __name__ == "__main__":
    app = App()
    app.mainloop()