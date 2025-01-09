from tkinter import ttk, CENTER

from Metier.demande import Demande
from Metier.tournee import Tournee

class AfficherTableau:

    def __init__(self, interface):
        self.interface = interface
        self.nb_commandes_par_acteur = None
        self.projet_en_cours = ""

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

        # Liaison avec l'évènement de redimensionnement
        self.interface.tableau.bind('<Configure>', lambda event : self.__redimensionnement(event, colonnes, proportions))

    def __redimensionnement(self, event, colonnes, proportions):
        # Recalculer les largeurs quand la fenêtre est redimensionnée
        new_width = event.width
        for col in colonnes:
            width = int((new_width * proportions[col]) / 100)
            self.interface.tableau.column(col, width=width)


    def tableau_producteurs(self, infos_producteurs: list, projet: str):
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
        nb_tournees_par_prod = Tournee.getNbTourneesProd()
        for prod in infos_producteurs:

            coord = f"({round(prod.latitude, 6)}, {round(prod.longitude, 6)})"
            partners = ", ".join([str(partner.id) for partner in prod.partners])
            dispos = ", ".join([str(dispo.num) for dispo in prod.dispos])

            nbTournees = (nb_tournees_par_prod[prod] if prod in nb_tournees_par_prod else 0)

            if not self.nb_commandes_par_acteur or self.projet_en_cours != projet:
                self.projet_en_cours = projet
                self.nb_commandes_par_acteur = Demande.getNbDemandesActeurs()
            nbCommandes = (self.nb_commandes_par_acteur[prod] if prod in self.nb_commandes_par_acteur else 0)

            self.interface.tableau.insert(parent='', index="end", values=(
                prod.id,
                coord,
                prod.capacity,
                partners,
                dispos,
                nbTournees,
                nbCommandes
            ))


    def tableau_clients(self, infos_clients: list, projet: str):
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

            if not self.nb_commandes_par_acteur or self.projet_en_cours != projet:
                self.projet_en_cours = projet
                self.nb_commandes_par_acteur = Demande.getNbDemandesActeurs()
            nbCommandes = (self.nb_commandes_par_acteur[cl] if cl in self.nb_commandes_par_acteur else 0)

            self.interface.tableau.insert(parent='', index="end", values=(
                cl.id,
                coord,
                dispos,
                nbCommandes
            ))


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

            c, chargeMax,chargeT = t.chargement()
            chargeTotale = str(chargeT) + " kg"

            self.interface.tableau.insert(parent='', index="end", values=(
                t.idTournee,
                t.producteur.id,
                t.demiJour.__repr__(),
                horaireDebut + ' - ' + horaireFin,
                dureeTotale,
                nbTaches,
                str(round(distTotale,2)) + " km",
                str(chargeMax) + " kg",
                chargeTotale
            ))


    def tableau_vide(self):
        style = ttk.Style()
        style.configure("Treeview", font=('Arial', 25), rowheight=100)
        self.interface.tableau = ttk.Treeview(self.interface.tableau_frame, columns=("VIDE",), show='')
        self.interface.tableau.heading("VIDE", text="VIDE")
        self.interface.tableau.column("VIDE", width=400, anchor=CENTER)
        self.interface.tableau.insert(parent='', index="end", values=("Vide : Veuillez importer des données",))
        self.interface.tableau.pack(fill="both", expand=True)

    def tableau_post_import(self):
        style = ttk.Style()
        style.configure("Treeview", font=('Arial', 25), rowheight=100)
        self.interface.tableau.config(columns=("",))
        self.interface.tableau.heading("", text="")
        self.interface.tableau.column("", width=self.interface.tableau.winfo_width(), anchor=CENTER)
        self.interface.tableau.insert(parent="", index="end", values=("Veuillez sélectionner une option dans le menu",))
        self.interface.tableau.pack(fill="both", expand=True)