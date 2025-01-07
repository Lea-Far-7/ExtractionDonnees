from tkinter import ttk, CENTER

class AfficherTableau:

    def __init__(self, interface):
        self.interface = interface

    def tableau_producteurs(self, infos_producteurs: list):
        colonnes = ("ID", "Coord", "Capacite", "Partenaires", "Dispo", "NbTournees", "NbCommandes")

        # Supprimer les anciennes colonnes et données
        for item in self.interface.tableau.get_children():
            self.interface.tableau.delete(item)

        # Configurer les nouvelles colonnes
        self.interface.tableau.configure(columns=colonnes, show='headings')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 13, 'bold'))
        style.configure("Treeview", font=('Arial', 11), rowheight=25)

        # Configuration des en-têtes et colonnes
        for col in colonnes:
            self.interface.tableau.heading(col, text=col)
            self.interface.tableau.column(col, anchor=CENTER)

        # Ajout des données
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

        # Configuration de la scrollbar
        self.interface.scrollbar.configure(command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=self.interface.scrollbar.set)
        print("Affichage Tableau Producteurs")


    def tableau_clients(self, infos_clients: list):
        colonnes = ("ID", "Coord", "Dispo", "NbCommandes")

        # Supprimer les anciennes colonnes et données
        for item in self.interface.tableau.get_children():
            self.interface.tableau.delete(item)

        # Configurer les nouvelles colonnes
        self.interface.tableau.configure(columns=colonnes, show='headings')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 13, 'bold'))
        style.configure("Treeview", font=('Arial', 11), rowheight=25)

        # Configuration des en-têtes et colonnes
        for col in colonnes:
            self.interface.tableau.heading(col, text=col)
            self.interface.tableau.column(col, anchor=CENTER)

        """
        self.interface.tableau.column("ID", width=60)
        self.interface.tableau.column("Coord", width=130)
        self.interface.tableau.column("Dispo", width=120)
        self.interface.tableau.column("NbCommandes", width=100)
        """

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

        # Configuration de la scrollbar
        self.interface.scrollbar.configure(command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=self.interface.scrollbar.set)

        print("Affichage Tableau Clients")


    def tableau_commandes(self, infos_commandes : list):
        colonnes = ("ID", "IDClient", "IDProducteur", "Masse")

        # Supprimer les anciennes colonnes et données
        for item in self.interface.tableau.get_children():
            self.interface.tableau.delete(item)

        # Configurer les nouvelles colonnes
        self.interface.tableau.configure(columns=colonnes, show='headings')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 13, 'bold'))
        style.configure("Treeview", font=('Arial', 11), rowheight=25)

        # Configuration des en-têtes et colonnes
        for col in colonnes:
            self.interface.tableau.heading(col, text=col)
            self.interface.tableau.column(col, anchor=CENTER)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 13, 'bold'))
        style.configure("Treeview", font=('Arial', 11), rowheight=25)

        for c in infos_commandes:
            self.interface.tableau.insert(parent='', index="end", values=(
                c.idDemande,
                c.client.id,
                c.producteur.id,
                str(c.masse) + "kg"
            ))

        self.interface.scrollbar.configure(command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=self.interface.scrollbar.set)
        print("Affichage Tableau Commandes")


    def tableau_tournees(self, infos_tournees : list):
        colonnes = ("ID", "Producteur", "DemiJ", "Horaire", "DureeTotale", "NbTaches", "DistanceTotale", "ChargeMax", "ChargementTotal")

        # Supprimer les anciennes colonnes et données
        for item in self.interface.tableau.get_children():
            self.interface.tableau.delete(item)

        # Configurer les nouvelles colonnes
        self.interface.tableau.configure(columns=colonnes, show='headings')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 13, 'bold'))
        style.configure("Treeview", font=('Arial', 11), rowheight=25)

        # Configuration des en-têtes et colonnes
        for col in colonnes:
            self.interface.tableau.heading(col, text=col)
            self.interface.tableau.column(col, anchor=CENTER)

        """
        self.interface.tableau.column("ID", width=60)
        self.interface.tableau.column("Producteur", width=100)
        self.interface.tableau.column("DemiJ", width=120)
        self.interface.tableau.column("Horaire", width=140)
        """

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

        self.interface.scrollbar.configure(command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=self.interface.scrollbar.set)
        print("Affichage Tableau Tournées")