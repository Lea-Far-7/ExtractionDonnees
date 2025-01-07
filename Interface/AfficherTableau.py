from tkinter import ttk, CENTER

class AfficherTableau:

    def __init__(self, interface):
        self.interface = interface

    def __set_tableau(self, colonnes, proportions):
        # Supprimer les anciennes colonnes et données
        for item in self.interface.tableau.get_children():
            self.interface.tableau.delete(item)

        # Configurer les nouvelles colonnes
        self.interface.tableau.configure(columns=colonnes, show='headings')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 13, 'bold'))
        style.configure("Treeview", font=('Arial', 11), rowheight=25)

        # Largeur du tableau
        width_totale = self.interface.tableau.winfo_width()

        for col in colonnes:
            self.interface.tableau.heading(col, text=col)
            width = int( (width_totale * proportions[col]) / 100) # Calcul de la largeur
            self.interface.tableau.column(col, width=width, anchor=CENTER)

        # Configuration de la scrollbar
        self.interface.scrollbar.configure(command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=self.interface.scrollbar.set)


    def tableau_producteurs(self, infos_producteurs: list):
        colonnes = ("ID", "Coord", "Capacite", "Partenaires", "Dispo", "NbTournees", "NbCommandes")

        # Calcul des proportions pour chaque colonne (total = 100)
        proportions = {
            "ID": 5,
            "Coord": 20,
            "Capacite": 10,
            "Partenaires": 20,
            "Dispo": 20,
            "NbTournees": 12.5,
            "NbCommandes": 12.5,
        }

        self.__set_tableau(colonnes, proportions)

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

        def redimensionnement(event):
            # Recalculer les largeurs quand la fenêtre est redimensionnée
            new_width = event.width
            for col in colonnes:
                width = int((new_width * proportions[col]) / 100)
                self.interface.tableau.column(col, width=width)

        self.interface.tableau.bind("<Configure>", redimensionnement)


    def tableau_clients(self, infos_clients: list):
        colonnes = ("ID", "Coord", "Dispo", "NbCommandes")

        # Calcul des proportions pour chaque colonne (total = 100)
        proportions = {
            "ID":20,
            "Coord":35,
            "Dispo":25,
            "NbCommandes":20,
        }

        self.__set_tableau(colonnes, proportions)

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

        def redimensionnement(event):
            # Recalculer les largeurs quand la fenêtre est redimensionnée
            new_width = event.width
            for col in colonnes:
                width = int((new_width * proportions[col]) / 100)
                self.interface.tableau.column(col, width=width)

        self.interface.tableau.bind("<Configure>", redimensionnement)


    def tableau_commandes(self, infos_commandes : list):
        colonnes = ("ID", "IDClient", "IDProducteur", "Masse")

        # Calcul des proportions pour chaque colonne (total = 100)
        proportions = {
            "ID": 25,
            "IDClient": 25,
            "IDProducteur": 25,
            "Masse": 25,
        }

        self.__set_tableau(colonnes, proportions)

        for c in infos_commandes:
            self.interface.tableau.insert(parent='', index="end", values=(
                c.idDemande,
                c.client.id,
                c.producteur.id,
                str(c.masse) + "kg"
            ))

        def redimensionnement(event):
            # Recalculer les largeurs quand la fenêtre est redimensionnée
            new_width = event.width
            for col in colonnes:
                width = int((new_width * proportions[col]) / 100)
                self.interface.tableau.column(col, width=width)

        self.interface.tableau.bind("<Configure>", redimensionnement)


    def tableau_tournees(self, infos_tournees : list):
        colonnes = ("ID", "Producteur", "DemiJ", "Horaire", "DureeTotale", "NbTaches", "DistanceTotale", "ChargeMax", "ChargementTotal")

        # Calcul des proportions pour chaque colonne (total = 100)
        proportions = {
            "ID": 5,
            "Producteur": 10,
            "DemiJ": 10,
            "Horaire": 10,
            "DureeTotale": 10,
            "NbTaches": 10,
            "DistanceTotale": 15,
            "ChargeMax": 15,
            "ChargementTotal": 15
        }

        self.__set_tableau(colonnes, proportions)

        for t in infos_tournees:
            nbTaches = len(t.taches)
            horaireDebut = t.taches[0].horaire
            horaireFin = t.taches[nbTaches-1].horaire
            _, _, distTotale = t.distance()
            liste_durees, _, dureeT = t.duree()
            nbH = dureeT // 60
            nbM = dureeT % 60
            dureeTotale = str(nbH) + "h " + str(nbM) + "m"
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

        def redimensionnement(event):
            # Recalculer les largeurs quand la fenêtre est redimensionnée
            new_width = event.width
            for col in colonnes:
                width = int((new_width * proportions[col]) / 100)
                self.interface.tableau.column(col, width=width)

        self.interface.tableau.bind("<Configure>", redimensionnement)