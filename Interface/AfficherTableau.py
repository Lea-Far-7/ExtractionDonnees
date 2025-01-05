import tkinter
from tkinter import ttk, CENTER
import customtkinter

class AfficherTableau:

    def __init__(self, interface):
        self.interface = interface
        self.options = ['producteurs', 'clients', 'commandes', 'tournees']
        self.selected_option = None
        self.selected_solution = None

    """
    def afficher_menu_deroulant(self, liste_clients, liste_producteurs, liste_commandes, dico_tournees):
        self.selected_option = customtkinter.StringVar(self.interface)
        self.selected_option.set(self.options[0])
        menu = customtkinter.CTkOptionMenu(self.interface.tableau, self.selected_option, *self.options, command=self.update_tableau(liste_clients, liste_producteurs, liste_commandes, dico_tournees))
        menu.grid(row=0, column=0, sticky="ew", padx=5, pady=5, columnspan=len(self.options))
    """

    def update_tableau(self, liste_clients, liste_producteurs, liste_commandes, dico_tournees):
        selected = self.selected_option.get()
        if selected == 'producteurs':
            self.tableau_producteurs(liste_producteurs)
        elif selected == 'clients':
            self.tableau_clients(liste_clients)
        elif selected == 'commandes':
            self.tableau_commandes(liste_commandes)
        elif selected == 'tournees':
            self.tableau_tournees(dico_tournees)


    def update_tableau_solutions(self, colonnes, infos_tournees, titre_colonnes):
        selected_solution = self.selected_solution.get()
        infos_tournees = self.createur.getTournees(selected_solution)
        self.creer_tableau(colonnes, infos_tournees, titre_colonnes)


    def creer_tableau(self, colonnes, infos, titre_colonnes):
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 13, 'bold'))
        style.configure("Treeview", font=('Arial', 11), rowheight=25)

        self.interface.tableau = ttk.Treeview(self.interface, columns=colonnes, show='headings')

        for col, titre in zip(colonnes, titre_colonnes):
            self.interface.tableau.heading(col, text=titre)
            self.interface.tableau.column(col, anchor=CENTER)

        for item in infos:
            self.interface.tableau.insert(parent='', index="end", values=item)

        self.interface.tableau.grid(row=2, rowspan=8, column=1, columnspan=len(colonnes), sticky="nsew")

        scrollbar = ttk.Scrollbar(self.interface, orient="vertical", command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=2, rowspan=8, column=len(colonnes) + 1, sticky="ns")

        self.interface.tableau.grid_forget()
        
    def afficher_tableau_producteurs(self, infos_producteurs):
        colonnes = ("ID", "Coord", "Capacite", "Partenaires", "Dispo", "NbTournees", "NbCommandes")
        titre_colonnes = ("ID", "Coordonnées", "Capacité", "Partenaires", "Disponibilités", "Nombre de Tournées", "Nombre de Commandes")
        self.creer_tableau(colonnes, infos_producteurs, titre_colonnes)
        
    def afficher_tableau_clients(self, infos_clients):
        colonnes = ("ID", "Coord", "Dispo", "NbCommandes")
        titre_colonnes = ("ID", "Coordonnées", "Disponibilités", "Nombre de Commandes")
        self.creer_tableau(colonnes, infos_clients, titre_colonnes)
        
    def afficher_tableau_commandes(self, infos_commandes):
        colonnes = ("ID", "IDClient", "IDProducteur", "Masse")
        titre_colonnes = ("ID", "IDClient", "IDProducteur", "Masse")
        self.creer_tableau(colonnes, infos_commandes, titre_colonnes)

    def afficher_tableau_tournees(self, dico_tournees):
        colonnes = ("ID", "Producteur", "DemiJ", "Horaire", "DureeTotale", "NbTaches", "DistanceTotale", "ChargeMax", "ChargementTotal")
        titre_colonnes = ("ID", "Producteur", "Demi-jour", "Horaire", "Durée Totale", "Nombre de tâches", "Distance Totale", "Charge Maximale", "Chargement Total")
        liste_noms, infos_tournees = [], []
        for nom_fichier, fichier in dico_tournees.items():
            liste_noms.append(nom_fichier)
            infos_tournees.append(fichier)
        self.creer_tableau(colonnes, infos_tournees[0], titre_colonnes)

        self.selected_solution = tkinter.StringVar(self.interface)
        self.selected_solution.set(liste_noms[0])

        menu_solution = ttk.OptionMenu(self.interface, self.selected_solution, *liste_noms, command=self.update_tableau_solutions(colonnes, infos_tournees, titre_colonnes))
        menu_solution.grid(row=1, column=1, sticky="w", padx=5, pady=5)
    

        









    def tableau_producteurs(self, infos_producteurs : list):
        colonnes = ("ID", "Coord", "Capacite", "Partenaires", "Dispo", "NbTournees", "NbCommandes")
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 13, 'bold'))
        style.configure("Treeview", font=('Arial', 11), rowheight=25)

        self.interface.tableau = ttk.Treeview(self.interface, columns=colonnes, show='headings')

        self.interface.tableau.heading("ID", text="ID")
        self.interface.tableau.heading("Coord", text="Coordonnées")
        self.interface.tableau.heading("Capacite", text="Capacité")
        self.interface.tableau.heading("Partenaires", text="Partenaires")
        self.interface.tableau.heading("Dispo", text="Disponibilités")
        self.interface.tableau.heading("NbTournees", text="Nombre de Tournées")
        self.interface.tableau.heading("NbCommandes", text="Nombre de Commandes")

        self.interface.tableau.column("ID", width=60)
        self.interface.tableau.column("Coord", width=130)
        self.interface.tableau.column("Capacite", width=90)
        self.interface.tableau.column("Dispo", width=120)
        self.interface.tableau.column("NbTournees", width=100)
        self.interface.tableau.column("NbCommandes", width=100)

        for col in colonnes:
            self.interface.tableau.column(col, anchor=CENTER)

        for prod in infos_producteurs:
            coord = f"({round(prod.latitude, 6)}, {round(prod.longitude, 6)})"
            partners = ", ".join([str(partner.id) for partner in prod.partners])
            dispos = ", ".join([str(dispo.num) for dispo in prod.dispos])
            nbTournees = "1"
            nbCommandes = "2"
            self.interface.tableau.insert(parent='', index="end", values=(
                prod.id,
                coord,
                prod.capacity,
                partners,
                dispos,
                nbTournees,
                nbCommandes
            ))

        self.interface.tableau.grid(row=1, rowspan=8, column=1, columnspan=len(colonnes), sticky="nsew")

        scrollbar = ttk.Scrollbar(self.interface, orient="vertical", command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, rowspan=8, column=len(colonnes) + 1, sticky="ns")

        self.interface.tableau.grid_forget()


    def tableau_clients(self, infos_clients: list):
        colonnes = ("ID", "Coord", "Dispo", "NbCommandes")
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 13, 'bold'))
        style.configure("Treeview", font=('Arial', 11), rowheight=25)

        self.interface.tableau = ttk.Treeview(self.interface, columns=colonnes, show='headings')

        self.interface.tableau.heading("ID", text="ID")
        self.interface.tableau.heading("Coord", text="Coordonnées")
        self.interface.tableau.heading("Dispo", text="Disponibilités")
        self.interface.tableau.heading("NbCommandes", text="Nombre de Commandes")

        """
        self.interface.tableau.column("ID", width=60)
        self.interface.tableau.column("Coord", width=130)
        self.interface.tableau.column("Dispo", width=120)
        self.interface.tableau.column("NbCommandes", width=100)
        """
        for col in colonnes:
            self.interface.tableau.column(col, anchor=CENTER)

        for cl in infos_clients:
            coord = f"({round(cl.latitude, 6)}, {round(cl.longitude, 6)})"
            dispos = ", ".join([str(dispo.num) for dispo in cl.dispos])
            nbCommandes = "10"
            self.interface.tableau.insert(parent='', index="end", values=(
                cl.id,
                coord,
                dispos,
                nbCommandes
            ))

        self.interface.tableau.grid(row=1, rowspan=8, column=1, columnspan=len(colonnes), sticky="nsew")

        scrollbar = ttk.Scrollbar(self.interface, orient="vertical", command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, rowspan=8, column=len(colonnes) + 1, sticky="ns")

        self.interface.tableau.grid_forget()


    def tableau_commandes(self, infos_commandes : list):
        colonnes = ("ID", "IDClient", "IDProducteur", "Masse")
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 13, 'bold'))
        style.configure("Treeview", font=('Arial', 11), rowheight=25)

        self.interface.tableau = ttk.Treeview(self.interface, columns=colonnes, show='headings')

        self.interface.tableau.heading("ID", text="ID")
        self.interface.tableau.heading("IDClient", text="IDClient")
        self.interface.tableau.heading("IDProducteur", text="IDProducteur")
        self.interface.tableau.heading("Masse", text="Masse")

        for col in colonnes:
            self.interface.tableau.column(col, anchor=CENTER)

        for c in infos_commandes:
            self.interface.tableau.insert(parent='', index="end", values=(
                c.idDemande,
                c.client.id,
                c.producteur.id,
                c.masse + "kg"
            ))

        self.interface.tableau.grid(row=1, rowspan=8, column=1, columnspan=len(colonnes), sticky="nsew")

        scrollbar = ttk.Scrollbar(self.interface, orient="vertical", command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, rowspan=8, column=len(colonnes) + 1, sticky="ns")

        self.interface.tableau.grid_forget()

    def tableau_tournees(self, infos_tournees : list):
        colonnes = ("ID", "Producteur", "DemiJ", "Horaire", "DureeTotale", "NbTaches", "DistanceTotale", "ChargeMax", "ChargementTotal") # Max = max(tous les chargements)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 13, 'bold'))
        style.configure("Treeview", font=('Arial', 11), rowheight=25)

        self.interface.tableau = ttk.Treeview(self.interface, columns=colonnes, show='headings')

        self.interface.tableau.heading("ID", text="ID")
        self.interface.tableau.heading("Producteur", text="Producteur")
        self.interface.tableau.heading("DemiJ", text="Demi-jour")
        self.interface.tableau.heading("Horaire", text="Horaire")
        self.interface.tableau.heading("DureeTotale", text="Durée Totale")
        self.interface.tableau.heading("NbTaches", text="Nombre de tâches")
        self.interface.tableau.heading("DistanceTotale", text="Distance Totale")
        self.interface.tableau.heading("ChargeMax", text="Charge Maximale")
        self.interface.tableau.heading("ChargementTotal", text="Chargement Total")

        self.interface.tableau.column("ID", width=60)
        self.interface.tableau.column("Producteur", width=100)
        self.interface.tableau.column("DemiJ", width=120)
        self.interface.tableau.column("Horaire", width=140)

        for col in colonnes:
            self.interface.tableau.column(col, anchor=CENTER)

        for t in infos_tournees:
            nbTaches = len(t.taches)
            horaireDebut = t.taches[0].horaire
            horaireFin = t.taches[nbTaches-1].horaire
            _, _, distTotale = t.distance()
            liste_durees, _, dureeT = t.duree()
            nbH = dureeT // 60
            nbM = dureeT % 60
            dureeTotale = str(nbH) + "h" + str(nbM) + "m"
            _, chargeMax,chargeT = t.chargement()
            chargeTotale = str(round(chargeT, 2)) + " kg"
            self.interface.tableau.insert(parent='', index="end", values=(
                t.idTournee,
                t.producteur.id,
                t.demiJour.__repr__(),
                horaireDebut + ' - ' + horaireFin,
                dureeTotale,
                nbTaches,
                str(distTotale) + " km",
                str(chargeMax) + " kg",
                chargeTotale
            ))

        self.interface.tableau.grid(row=1, rowspan=8, column=1, columnspan=len(colonnes), sticky="nsew")

        scrollbar = ttk.Scrollbar(self.interface, orient="vertical", command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, rowspan=8, column=len(colonnes) + 1, sticky="ns")

        self.interface.tableau.grid_forget()