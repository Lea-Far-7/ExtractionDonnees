from tkinter import *
from  tkinter import ttk
from tkintermapview import TkinterMapView
from PIL import Image
import customtkinter
from Interface.PopUp import PopUp

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

        # Mise en arrière définitive de la fenêtre (pour que les pop-ups puissent toujours se situer devant)
        self.attributes('-topmost',False)

        # Permet de configurer la grid,
        # "weight = 1" permet de remplir au maximum l'espace de la grid désigné
        # "weight = 0" permet de réduire au minimum l'espace de la grid désigné

        self.grid_columnconfigure((1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((1, 2), weight=1)

        # Création de la zone contenant les boutons de gestion
        self.sidebar = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # Crée une Image mise dans un Label pour être affichée et contenue dans la sidebar
        self.my_image = customtkinter.CTkImage(light_image=Image.open("../Images/Logo_Olocap.png"), dark_image=Image.open("../Images/Logo_Olocap.png"), size=(192,58))

        self.image_label = customtkinter.CTkLabel(self.sidebar, image=self.my_image, text=" ")
        self.image_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.couleur_bouton = customtkinter.CTkImage(light_image=Image.open('../Images/Couleur_Boutons.png'), size=(500, 150))

        # Création des boutons dans la sidebar
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855", text = "Importer")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855",  command=self.sidebar_button_event, text = "Filtres")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855", command=self.sidebar_button_event, text = "Export")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855", command=self.sidebar_button_event, text = "Ajout")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar, fg_color="#1d7c69", hover_color="#275855", command=self.sidebar_button_event, text = "Supprimer")
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)

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
        self.pos1 = self.map_widget.set_marker(47.3565655, 0.7035767, text="Pos1")
        self.pos2 = self.map_widget.set_marker(47.3561294, 0.6977163, text="Pos2")

        self.traj1 = self.map_widget.set_path([self.pos2.position, self.pos1.position],color="#1d7c69")


        # Définition d'une variable exclusive pour le resize de la fenêtre
        self.zoom = 1
        self.bind("<Configure>", self.resize_button)

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

    # Evenement déclenché lors d'une maximisation de fenêtre OU lorsque l'on quitte la maximisation pour revenir sur une fenêtre plus petite
    def resize_button(self, event):
        # print(self.state())
        if (self.state() == 'zoomed' and self.zoom == 1) :
            customtkinter.set_widget_scaling(1.25)
            self.zoom = 0
        elif (self.state() != 'zoomed' and self.zoom == 0) :
            customtkinter.set_widget_scaling(1)
            self.zoom = 1


"""
    def popup(self):
        # Création d'une nouvelle fenêtre
        window = customtkinter.CTkToplevel()

        # Ouvre une fenêtre de selection de multiples fichiers et (Actuellement mais à changer) Affiche le contenu de chaque fichier
        def search():
            listfile = filedialog.askopenfilename(multiple = True, title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
            print (listfile)
            for i in range(0,len(listfile),1):
                with open(listfile[i], 'r') as file:
                    content = file.read()
                    print (content)



        #Focus sur cette nouvelle fenêtre (cela désactive la fenêtre principale)
        window.grab_set()

        # Création d'un Label
        label = customtkinter.CTkLabel(window, text="Test")
        label.pack(pady=50)

        # Création d'un bouton pour chercher les fichiers à importer
        button_search = customtkinter.CTkButton(window, text="Rechercher", command=search)
        button_search.pack(pady=10, padx=50)

        # Création d'un bouton pour fermer la pop-up et revenir sur la fenêtre principale
        button_close = customtkinter.CTkButton(window, text="Fermer", command=window.destroy)
        button_close.pack(pady=10, padx=50)






        # Suppression de la topbar (Titre, Minimiser, Maximiser, Fermer)
        window.overrideredirect(True)

        # Placement de la fenêtre à des coordonnées relatives à la fenêtre principale
        window.geometry("+%d+%d" % (window.master.winfo_rootx()+window.master.winfo_width()/5, window.master.winfo_rooty()+window.master.winfo_height()/4))
"""





if __name__ == "__main__":
    app = App()
    app.mainloop()

