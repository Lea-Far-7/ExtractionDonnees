import tkinter
import customtkinter

from Interface.AfficherCarte import AfficherCarte
from Interface.AfficherTableau import AfficherTableau
from Interface.Createur import Createur
from Interface.MarkerActeur import MarkerActeur
from Interface.PopUp import PopUp

# Création d'une pop-up et inclusion d'éléments pour l'importation de fichiers
class PopupImport:
    def __init__(self, interface, createur : Createur):

        self.interface = interface
        self.createur = createur

        self.projet_en_cours = ""
        self.nom_fichier_donnees = ""
        self.liste_noms_fichiers_solutions = [] # Liste des fichiers solution du projet en cours
        self.liste_boutons_solutions = {} # Dictionnaire {nom_solution : switch}
        self.choixSolutions = [] # Liste des solutions sélectionnées pour le projet en cours
        self.fichier_donnees = [] # Liste des lignes du fichier de données du projet en cours
        self.fichiers_solutions = [] # liste de liste des lignes de chaque fichier solution (si plusieurs sont sélectionnés)

        # Initialisation du popup
        self.popup = PopUp(self.interface)

        # Création de la Frame contenant les RadioButtons
        scrollable_frame = customtkinter.CTkScrollableFrame(self.popup.window, label_text="Projets")
        scrollable_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        radio_var = tkinter.IntVar(value=0)

        # Récupère la liste des projets du répertoire Projets
        liste_dossiers = createur.getDossiers()

        # Génère la Frame qui va contenir les Switchs
        frame_solutions = customtkinter.CTkScrollableFrame(self.popup.window, label_text="Fichiers Solution Associés")
        frame_solutions.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # Création de la liste des boutons pour les projets
        liste_boutons_projets = {}
        i = 0
        for projet in liste_dossiers:
            liste_boutons_projets[projet] = customtkinter.CTkRadioButton(master=scrollable_frame, fg_color="#1d7c69", hover_color="#275855",
                                                                 variable=radio_var, value=i+1, text=f"{projet}", command=lambda p=projet: self.assignProjet(p,frame_solutions))
            liste_boutons_projets[projet].grid(row=i, column=0, padx=10, pady=(0, 20))
            i += 1

        boutonValider = customtkinter.CTkButton(self.popup.window, fg_color="#1d7c69", hover_color="#275855", command=self.valider, text="Valider")
        boutonValider.grid(row=9, column=0, columnspan=10, padx=20, pady=10)

        # Placement de la pop-up au centre de la fenêtre principale
        self.popup.window.geometry("+%d+%d" % ((self.popup.masterwindow.winfo_rootx() + self.popup.masterwindow.winfo_width() / 2)-(self.popup.window.winfo_width()*1.5),
                (self.popup.masterwindow.winfo_rooty() + self.popup.masterwindow.winfo_height() / 2)-(self.popup.window.winfo_height()*1.25)))
        self.interface.wait_window(self.popup.window)


    def assignProjet(self, projet, frame_solutions):

        self.projet_en_cours = projet
        # Si des marqueurs sont déjà présents, on les cache pour éviter une surcharge visuelle
        if self.interface.mark_list :
            for mark in self.interface.mark_list:
                mark.hide()

        # Détruit les objets précédemment créés dans la ScrollableFrame où sont contenues les solutions
        for widget in frame_solutions.winfo_children():
            widget.destroy()

        # Remets la liste des solutions sélectionnées à vide
        self.choixSolutions = []

        # Récupère le fichier de données dans le projet sélectionné
        # indice 0, car il ne peut y avoir qu'un seul fichier de données par projet
        self.nom_fichier_donnees = self.createur.getFichiers(self.projet_en_cours)[0]

        # Récupère la liste des fichiers solutions dans le projet sélectionné
        self.liste_noms_fichiers_solutions = self.createur.getFichiers(self.projet_en_cours + "\Solutions")

        # Extrait les données du fichier de données du projet
        self.fichier_donnees = self.createur.getContenuFichierDonnees(self.projet_en_cours + "\\" + self.nom_fichier_donnees)

        # Crée les différents Switchs permettant de sélectionner les boutons
        self.liste_boutons_solutions = {}
        j = 0
        for solutions in self.liste_noms_fichiers_solutions:
            self.liste_boutons_solutions[solutions] = customtkinter.CTkSwitch(master=frame_solutions, progress_color="#1d7c69", text=f"{solutions}")
            self.liste_boutons_solutions[solutions].grid(row=j, column=0, padx=10, pady=(0, 20))
            j = j + 1


    def valider(self):

        if self.fichier_donnees:
            self.__synchronisation_carte_tableau()

            # On met à jour l'attribut "données" de l'interface principale pour les filtres
            self.interface.donnees = self.fichier_donnees

            # /!\ Temporaire pour les filtres : à replacer lors de l'implémentation de l'affichage des solutions
            self.interface.solution = self.createur.getContenuFichierSolution(self.liste_noms_fichiers_solutions[0])


    def __synchronisation_carte_tableau(self):
        # Supprime tous les marqueurs présents sur la map
        self.interface.map_widget.delete_all_marker()
        self.interface.mark_list.clear()

        # Supprime toutes les lignes du tableau
        for item in self.interface.tableau.get_children():
            self.interface.tableau.delete(item)

        producteurs, clients = self.createur.getActeurs(self.fichier_donnees, self.projet_en_cours)

        afficheurCarte = AfficherCarte(self.interface)
        afficheurCarte.markers_producteurs(producteurs)
        afficheurCarte.markers_clients(clients)
        afficheurTab = AfficherTableau(self.interface)

        # On récupère la liste des noms de fichiers sélectionnés (état switch = 1)
        self.choixSolutions = (c for c,b in self.liste_boutons_solutions.items() if b.get() == 1)
        # On récupère le contenu de chaque fichier solution sélectionné
        liste_tournees = []
        for index, fichier in enumerate(self.choixSolutions):
            self.fichiers_solutions.append(self.createur.getContenuFichierSolution(fichier))
            liste_tournees.append(self.createur.getTournees(self.fichiers_solutions[index])) # Ajout de la liste de tournées de chaque fichier

        self.interface.solution = self.fichiers_solutions
        for c in self.choixSolutions:
            print("solution : " + c)
        if self.choixSolutions:
            afficheurTab.tableau_tournees(liste_tournees[0])
        else:
            afficheurTab.tableau_producteurs(producteurs)
        #Commentaire