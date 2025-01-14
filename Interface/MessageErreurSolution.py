from tkinter import messagebox

"""
Cette classe se charge de gérer toutes les messagebox de l'application.
"""

class MessageErreurSolution:

    def __init__(self):
        pass


    def afficher_question_erreur(self, nom_fichier, erreurs:dict[str:int]):
        """
        Se charge de la MessageBox pour demander à l'utilisateur s'il souhaite
        continuer le chargement du fichier solution en dépit des erreurs présentes dans celui-ci.
        :param nom_fichier:
        :param erreurs: {nom_erreur : int}
        :return: Affiche la MessageBox
        """
        drop_pick_message = "Commande non récupérée"
        charge_message = "Commande non livrée"
        acteurs_message = "Acteur de la tournée inconnu"
        dispo_message = "Acteur indisponible au cours de la tournée"

        message_erreur = ("Le chargement du fichier " + nom_fichier + " a rencontré des erreurs :\n"
                                + acteurs_message + " : " + str(erreurs["acteurs"]) + "\n"
                                + dispo_message + " : " + str(erreurs["demi_jour"]) + "\n"
                                + drop_pick_message + " : " + str(erreurs["drop_pick"]) + "\n"
                                + charge_message + " : " + str(erreurs["charge"]) + "\n"
                                + "Voulez-vous quand même continuer le chargement du fichier ?"
                                )
        return messagebox.askyesno("Des erreurs sont survenues !", message_erreur)


    def afficher_information_nb_erreurs(self, nom_fichier : str, nb_total_erreurs):
        """
        Se charge de la MessageBox qui informe du nombre d'erreurs total trouvé dans le fichier à la fin du chargement.
        :param nom_fichier:
        :param nb_total_erreurs:
        :return: Affiche la MessageBox
        """
        message = "Le chargement du fichier " + nom_fichier + " s'est terminé avec un total de " + str(nb_total_erreurs) + " erreurs."
        messagebox.showinfo("Fin du chargement", message)


    def afficher_annulation(self):
        """
        Se charge de la MessageBox informant de l'annulation du chargement.
        :return: Affiche la MessageBox
        """
        messagebox.showinfo("Annulation", "Le chargement du fichier solution a été annulé")
