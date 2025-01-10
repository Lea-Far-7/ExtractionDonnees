from tkinter import messagebox

class PopupErreurSolution:

    def __init__(self, erreurs:dict[str:int]):

        self.erreurs = erreurs

    def afficher_question_erreur(self, nom_fichier):
        drop_pick_message = "Commande non récupérée"
        charge_message = "Commande non livrée"
        acteurs_message = "Acteur de la tournée inconnu"
        dispo_message = "Acteur indisponible au cours de la tournée"

        message_erreur = ("Le chargement du fichier " + nom_fichier + " a rencontré des erreurs :\n"
                                + acteurs_message + " : " + str(self.erreurs["acteurs"]) + "\n"
                                + dispo_message + " : " + str(self.erreurs["demi_jour"]) + "\n"
                                + drop_pick_message + " : " + str(self.erreurs["drop_pick"]) + "\n"
                                + charge_message + " : " + str(self.erreurs["charge"]) + "\n"
                                + "Voulez-vous quand même continuer le chargement du fichier ?"
                                )
        return messagebox.askyesno("Des erreurs sont survenues !", message_erreur)

    def afficher_information_nb_erreurs(self, nom_fichier : str, nb_total_erreurs):
        message = "Le chargement du fichier " + nom_fichier + " s'est terminé avec un total de " + str(nb_total_erreurs) + " erreurs."
        messagebox.showinfo("Fin du chargement", message)

    def afficher_annulation(self):
        messagebox.showinfo("Annulation", "Le chargement du fichier solution a été annulé")
