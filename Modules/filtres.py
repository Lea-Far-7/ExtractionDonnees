def filtreTournees(tournees:list, producteursId:list, clientsId:list, demiJoursNum:list)->list:

    """
    Filtrer les tournées selon les producteurs et clients impliqués ainsi que les demi-journées
    :param list[Tournee] tournees: Liste des tournées à filtrer
    :param list[int] producteursId: Seuls les tournées conduites par l'un des producteurs représentés dans cette liste seront prises en compte.
    :param list[int] clientsId: Seuls les tournées qui impliquent l'un des clients représentés dans cette liste seront prises en compte.
    :param list[int] demiJoursNum: Seuls les tournées qui se déroulent sur l'une des demi-journées représentées dans cette liste seront prises en compte.
    :return: Nouvelle liste de tournées filtrées.

    Une liste vide en paramètre permet d'évacuer la contrainte
    """

    tourneesFiltrees = []

    for tournee in tournees:

        # Contrainte sur les demi-journées
        if not demiJoursNum or tournee.demiJour.num in demiJoursNum:

            #print("T"+str(tournee.idTournee)+" DJ OK")

            # Contrainte sur les producteurs (on prend en compte seulement les producteurs qui font les tournées)
            if not producteursId or tournee.producteur.id in producteursId:

                #print("T" + str(tournee.idTournee) + " Prod OK")

                # Contrainte sur les clients
                clContrainte = not clientsId # not liste renvoie true si liste vide

                # On doit parcourir les taches et comparer avec les lieux où elles se passent
                t = 0
                while (not clContrainte) and t < len(tournee.taches):
                    idActeur = tournee.taches[t].lieu.id
                    clContrainte = idActeur in clientsId
                    t+=1

                if clContrainte:
                    #print("T" + str(tournee.idTournee) + " Cl OK")
                    tourneesFiltrees.append(tournee)

    return tourneesFiltrees


def filtreListesTournees(listesTournees:list, producteursId:list, clientsId:list, demiJoursNum:list)->list:
    """Permet de filtrer chaque liste de tournées contenue dans une liste avec la fonction filtreTournees."""
    return [filtreTournees(liste, producteursId, clientsId, demiJoursNum) for liste in listesTournees]


# Attention cette fonction renvoie les ID des acteurs pas les objets eux-mêmes (peut être sujet à changement plus tard)
def filtreActeurs(listeTournees:list, listeActeursID:list)->list:
    """
    Récupère les ID des acteurs qui sont impliqués (parcourus) par au moins une des tournées spécifiées.
    :param listeTournees: Liste des tournées filtrées.
    :param listeActeursID: Liste des acteurs à inclure dans le résultat (utile si aucune tournée ou aucune ne correspond).
    :return: Liste des acteurs impliqués et souhaités.
    """
    acteurs = listeActeursID.copy()
    for tournee in listeTournees:
        prod_leader = tournee.producteur
        if not prod_leader.id in acteurs:
            acteurs.append(prod_leader.id)
        for tache in tournee.taches:
            act = tache.lieu
            if not act.id in acteurs:
                acteurs.append(act.id)
    return acteurs