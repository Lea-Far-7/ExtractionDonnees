import tkinter.messagebox
from time import strftime, gmtime
from tkinter import *
from  tkinter import ttk

from tkintermapview import TkinterMapView
from PIL import Image, ImageGrab
import customtkinter

from Interface.Createur import Createur
from Interface.PopupFiltre import PopupFiltre
from Interface.PopupImport import PopupImport

# Modes: "System", "Dark", "Light"
customtkinter.set_appearance_mode("Dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.createur = Createur()

        # Définition des composants essentiels
        self.map_widget = None
        self.tableau = None
        self.mark_list = [] # liste des marqueurs
        self.donnees = [] # liste des lignes du fichier
        self.solution = [] # liste des lignes du fichier solution

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

        # Lier l'événement de configuration pour mettre à jour les popups
        self.bind('<Configure>', self.update_all_popups_position)

    def update_all_popups_position(self, event=None):
        for marker in self.mark_list:
            marker.popup.update_popup_position()


    def interfacePrincipale(self):
        # Permet de configurer la grid,
        # "weight = 1" permet de remplir au maximum l'espace de la grid désigné
        # "weight = 0" permet de réduire au minimum l'espace de la grid désigné

        self.grid_columnconfigure((1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((1, 2), weight=1)

        # Création de la zone contenant les boutons de gestion
        sidebar = customtkinter.CTkFrame(self, width=230, corner_radius=0)
        sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # Création de l'image logo
        image_label = customtkinter.CTkLabel(sidebar, image=self.my_image, text=" ")
        image_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Utilisation d'une image contenant une seule couleur pour l'appliquer sur les boutons
        couleur_bouton = customtkinter.CTkImage(light_image=Image.open('../Images/Couleur_Boutons.png'),
                                                     size=(500, 150))

        # Création des boutons dans la sidebar
        importer = customtkinter.CTkButton(sidebar, fg_color="#1d7c69", hover_color="#275855",
                                                command=lambda: PopupImport(self, self.createur), text="Importer")
        importer.grid(row=1, column=0, padx=20, pady=10)
        filtre_bouton = customtkinter.CTkButton(sidebar, fg_color="#1d7c69", hover_color="#275855",
                                              command=lambda: PopupFiltre(self, self.createur), text="Filtres")
        filtre_bouton.grid(row=4, column=0, padx=20, pady=10)
        export_bouton = customtkinter.CTkButton(sidebar, fg_color="#1d7c69", hover_color="#275855",
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
        colonne_message = ("VIDE",)
        style = ttk.Style()
        style.configure("Treeview", font=('Arial', 25), rowheight=100)
        self.tableau = ttk.Treeview(self, columns=colonne_message, show='')
        self.tableau.heading("VIDE", text="VIDE")
        self.tableau.column("VIDE", width=400, anchor=CENTER)
        self.tableau.insert(parent='', index="end", values=("Vide : Veuillez importer des données",))
        self.tableau.grid(row=1, rowspan=8, column=1, columnspan=len(colonne_message), sticky="nsew")
        """
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tableau.yview)
        self.tableau.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, rowspan=8, column=5, sticky="ns")"""
        self.tableau.grid_forget()

        """
        # Liste des options pour le menu déroulant
        self.options = ['', 'producteurs', 'clients', 'commandes', 'tournees']
        self.selected_option = tkinter.StringVar(self)
        self.selected_option.set(self.options[0])

        # Création du menu déroulant
        self.dropdown = ttk.OptionMenu(self, self.selected_option, *self.options, command=self.update_tableau())
        self.dropdown.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        
        #liste_producteurs, liste_clients = self.createur.getActeurs(self.donnees, self.createur.projet)
        colonnes = ("ID", "Coord", "Capacite", "Partenaires", "Dispo", "NbTournees", "NbCommandes")
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 13, 'bold'))
        style.configure("Treeview", font=('Arial', 11), rowheight=25)

        self.tableau = ttk.Treeview(self, columns=colonnes, show='headings')

        self.tableau.heading("ID", text="ID")
        self.tableau.heading("Coord", text="Coordonnées")
        self.tableau.heading("Capacite", text="Capacité")
        self.tableau.heading("Partenaires", text="Partenaires")
        self.tableau.heading("Dispo", text="Disponibilités")
        self.tableau.heading("NbTournees", text="Nombre de Tournées")
        self.tableau.heading("NbCommandes", text="Nombre de Commandes")

        self.tableau.column("ID", width=60)
        self.tableau.column("Coord", width=130)
        self.tableau.column("Capacite", width=90)
        self.tableau.column("Dispo", width=120)
        self.tableau.column("NbTournees", width=100)
        self.tableau.column("NbCommandes", width=100)

        for col in colonnes:
            self.tableau.column(col, anchor=CENTER)

        self.tableau.grid(row=1, rowspan=8, column=1, columnspan=len(colonnes), sticky="nsew")

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tableau.yview)
        self.tableau.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, rowspan=8, column=len(colonnes) + 1, sticky="ns")

        self.tableau.grid_forget()
        """

    def screenshot(self):
        bbox = (self.map_widget.winfo_rootx(), self.map_widget.winfo_rooty(), self.map_widget.winfo_rootx()+self.map_widget.winfo_width(), self.map_widget.winfo_rooty()+self.map_widget.winfo_height())

        # Capture the screenshot
        screenshot = ImageGrab.grab(bbox)

        # Save the screenshot
        screenshot.save('../Exports/Screenshot_'+strftime("%Y%m%d_%H%M%S", gmtime())+'.png')

        tkinter.messagebox.showinfo(title="Information", message="Image enregistrée")

    # Evenement permettant d'afficher le tableau tout en cachant la map
    def select_tab(self) :
        self.tableau.grid(row=1, rowspan=8, column=1, columnspan=4, sticky="nsew")
        self.map_widget.grid_forget()
        if self.mark_list :
            for mark in self.mark_list:
                mark.hide()


    # Evenement permettant d'afficher la map tout en cachant le tableau
    def select_map(self) :
        self.map_widget.grid(row=1, rowspan=8, column=1, columnspan=4, sticky="nsew")
        self.tableau.grid_forget()


if __name__ == "__main__":
    app = App()
    app.mainloop()