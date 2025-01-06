import tkinter
from tkinter import ttk, CENTER
import customtkinter

class AfficherTableau:

    def __init__(self, interface):
        self.interface = interface
        self.options = ['producteurs', 'clients', 'commandes', 'tournees']
        self.selected_option = None
        self.selected_solution = None

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

        self.interface.tableau.column("ID", width=50)
        self.interface.tableau.column("Coord", width=130)
        self.interface.tableau.column("Capacite", width=70)
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

        self.interface.scrollbar.configure(command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=self.interface.scrollbar.set)
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

        self.interface.scrollbar.configure(command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=self.interface.scrollbar.set)
        self.interface.tableau.grid_forget()


    def tableau_tournees(self, infos_tournees : list):
        colonnes = ("ID", "Producteur", "DemiJ", "Horaire", "DureeTotale", "NbTaches", "DistanceTotale", "ChargeMax", "ChargementTotal")
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

        print(infos_tournees)

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
                str(round(distTotale,2)) + " km",
                str(round(chargeMax,2)) + " kg",
                chargeTotale
            ))

        self.interface.tableau.grid(row=1, rowspan=8, column=1, columnspan=len(colonnes), sticky="nsew")

        self.interface.scrollbar.configure(command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=self.interface.scrollbar.set)
        self.interface.tableau.grid_forget()