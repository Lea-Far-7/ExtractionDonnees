
def filtreTournees(tournees:list, producteursId:list, clientsId:list, demiJoursNum:list)->list:

    """
    Filtrer les tournées selon les producteurs et clients impliqués ainsi que les demi-journées
    :param list[Tournee] tournees: Liste des tournées à filtrer
    :param list[int] producteursId: Seuls les tournées conduites par l'un des producteurs représentés dans cette liste seront prises en compte.
    :param list[int] clientsId: Seuls les tournées qui impliquent l'un des clients représentés dans cette liste seront prises en compte.
    :param list[int] demiJoursNum: Seuls les tournées qui se déroulent sur l'une des demi-journées représentées dans cette liste seront prises en compte.
    :return: Nouvelle liste de tournées filtrées.

    Une valeur None sur l'une des listes en paramètre permet d'évacuer la contrainte
    """

    tourneesFiltrees = []

    for tournee in tournees:

        # Contrainte sur les demi-journées
        if demiJoursNum == None or tournee.demiJour.num in demiJoursNum:

            # Contrainte sur les producteurs (on prend en compte seulement les producteurs qui font les tournées)
            if producteursId == None or tournee.producteur.id in producteursId:

                # Contrainte sur les clients
                clContrainte = (clientsId == None)

                # On doit parcourir les taches et comparer avec les lieux où elles se passent
                t = 0
                while (not clContrainte) and t < len(tournee.taches):
                    idActeur = tournee.taches[t].lieu.id
                    clContrainte = idActeur in clientsId
                    t+=1

                if clContrainte:
                    tourneesFiltrees.append(tournee)

    return tourneesFiltrees