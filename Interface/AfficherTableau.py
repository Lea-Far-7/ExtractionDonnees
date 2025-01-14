from tkinter import ttk, CENTER

from Metier.demande import Demande
from Metier.tournee import Tournee

"""
Cette classe doit gérer l'ensemble de l'affichage dans l'onglet tableau :
-> Lorsqu'il est vide avant l'importation de données
-> Lorsqu'il est vide après l'importation de données
-> Lorsqu'un affichage est choisi par l'utilisateur
Les affichages possibles sont :
-> Le tableau des producteurs
-> Le tableau des clients
-> Le tableau des commandes
-> Le tableau des tournées du fichier solution sélectionné parmi ceux importés
"""

class AfficherTableau:

    def __init__(self, interface):

        self.interface = interface # L'interface principale
        self.nb_commandes_par_acteur = None
        self.projet_en_cours = ""
        self.acteurs_id_filtres = None # Mise à jour de cette liste post filtrage
        self.tournees_filtrees = None # Mise à jour de cette liste post filtrage


    def tableau_producteurs(self, infos_producteurs: list, projet: str):
        """
        Se charge de récupérer et mettre en forme le contenu du tableau pour les producteurs.
        :param infos_producteurs: Liste des producteurs à afficher.
        :param projet: Nom du projet en cours d'affichage.
        :return: Remplissage du tableau de producteurs.
        """

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

            # On vérifie que le producteur n'est pas filtré
            if not self.acteurs_id_filtres or prod.id in self.acteurs_id_filtres:

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
        """
        Se charge de récupérer et mettre en forme le contenu du tableau pour les clients.
        :param infos_clients: Liste des clients à afficher.
        :param projet: Nom du projet en cours d'affichage.
        :return: Remplissage du tableau de clients.
        """

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

            # On vérifie que le client n'est pas filtré
            if not self.acteurs_id_filtres or cl.id in self.acteurs_id_filtres:

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
        """
        Se charge de récupérer et mettre en forme le contenu du tableau pour les commandes.
        :param infos_commandes: Liste des commandes à afficher.
        :return: Remplissage du tableau de commandes.
        """

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

            # On vérifie que les acteurs de la commande ne sont pas (tous) filtrés
            if not self.acteurs_id_filtres or c.client.id in self.acteurs_id_filtres or c.producteur.id in self.acteurs_id_filtres:
                self.interface.tableau.insert(parent='', index="end", values=(
                    c.idDemande,
                    c.client.id,
                    c.producteur.id,
                    str(c.masse) + "kg"
                ))


    def tableau_tournees(self, infos_tournees : list):
        """
        Se charge de récupérer et mettre en forme le contenu du tableau pour les tournées.
        :param infos_tournees: Liste des tournées à afficher.
        :return: Remplissage du tableau de tournées.
        """

        colonnes = ("ID", "Producteur", "DemiJ", "Horaire", "DureeTotale", "NbTaches", "Prod/Clients visités", "DistanceTotale", "ChargeMax", "ChargementTotal")

        # Calcul des proportions pour chaque colonne (total = 100)
        proportions = {
            "ID": 3,
            "Producteur": 8,
            "DemiJ": 11,
            "Horaire": 10,
            "DureeTotale": 10,
            "NbTaches": 8,
            "Prod/Clients visités": 15,
            "DistanceTotale": 12,
            "ChargeMax": 11,
            "ChargementTotal": 12
        }

        self.__set_tableau(colonnes, proportions)

        for t in infos_tournees:

            # On vérifie que la tournée n'est pas filtrée
            if not self.tournees_filtrees or t in self.tournees_filtrees:

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

                lieux = ", ".join([str(id) for id in t.get_id_lieux()])

                self.interface.tableau.insert(parent='', index="end", values=(
                    t.idTournee,
                    t.producteur.id,
                    repr(t.demiJour),
                    horaireDebut + ' - ' + horaireFin,
                    dureeTotale,
                    nbTaches,
                    lieux,
                    str(round(distTotale,2)) + " km",
                    str(chargeMax) + " kg",
                    chargeTotale
                ))


    def tableau_vide(self):
        """
        Se charge du tableau vide avant import des données
        :return: Affiche un message
        """
        style = ttk.Style()
        style.configure("Treeview", font=('Arial', 25), rowheight=100)
        self.interface.tableau = ttk.Treeview(self.interface.tableau_frame, columns=("VIDE",), show='')
        self.interface.tableau.heading("VIDE", text="VIDE")
        self.interface.tableau.column("VIDE", width=400, anchor=CENTER)
        self.interface.tableau.insert(parent='', index="end", values=("Vide : Veuillez importer des données",))
        self.interface.tableau.pack(fill="both", expand=True)

    def tableau_post_import(self):
        """
        Se charge du tableau vide après import des données
        :return: Affiche un message
        """
        style = ttk.Style()
        style.configure("Treeview", font=('Arial', 25), rowheight=100)
        self.interface.tableau.config(columns=("Selection",))
        self.interface.tableau.heading("Selection", text="Selection")
        self.interface.tableau.column("Selection", width=self.interface.tableau.winfo_width(), anchor=CENTER)
        self.interface.tableau.insert(parent="", index="end", values=("Veuillez sélectionner une option dans le menu",))
        self.interface.tableau.pack(fill="both", expand=True)


    def __set_tableau(self, colonnes : tuple, proportions : dict[str, int]):
        """
        Se charge du layout commun à tous les affichages de tableau.
        :param colonnes: Le nom de toutes les colonnes à afficher.
        :param proportions: Les proportions de chacune de ces colonnes.
        :return: Affiche le tableau vide avec le nom des colonnes.
        """

        # Supprimer les anciennes colonnes et données
        for item in self.interface.tableau.get_children():
            self.interface.tableau.delete(item)

        # Configurer les nouvelles colonnes
        self.interface.tableau.configure(columns=colonnes, show='headings')

        # Choix du style des éléments
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 13, 'bold'))
        style.configure("Treeview", font=('Arial', 11), rowheight=25)

        # Largeur du tableau
        width_totale = self.interface.tableau.winfo_width()

        # Placement des colonnes
        for col in colonnes:
            self.interface.tableau.heading(col, text=col)
            width = int( (width_totale * proportions[col]) / 100) # Calcul de la largeur
            self.interface.tableau.column(col, width=width, anchor=CENTER)

        # Configuration de la scrollbar
        self.interface.scrollbar.configure(command=self.interface.tableau.yview)
        self.interface.tableau.configure(yscrollcommand=self.interface.scrollbar.set)

        # Liaison avec l'évènement de redimensionnement
        self.interface.tableau.bind('<Configure>', lambda event : self.__redimensionnement(event, colonnes, proportions))


    def __redimensionnement(self, event, colonnes, proportions : dict[str, int]):
        """
        Redimensionne le tableau en fonction de la taille de la fenêtre.
        :param event: Détection d'un changement de dimensions.
        :param colonnes: Le nom des colonnes.
        :param proportions: Les proportions de chacune de ces colonnes.
        :return: L'affichage du tableau avec les proportions ajustées
        """
        # Calcul des largeurs quand la fenêtre est redimensionnée
        new_width = event.width
        for col in colonnes:
            width = int((new_width * proportions[col]) / 100)
            self.interface.tableau.column(col, width=width)