
def filtreTournees(tournees:list, producteursId:list, clientsId:list, demiJours:list)->list:

    """
    Filtrer les tournées selon les producteurs et clients impliqués ainsi que les demi-journées
    :param tournees: Liste des tournées à filtrer
    :param producteursId: Seuls les tournées qui impliquent l'un des producteurs représentés dans cette liste seront prises en compte.
    :param clientsId: Seuls les tournées qui impliquent l'un des clients représentés dans cette liste seront prises en compte.
    :param demiJours: Seuls les tournées qui se déroulent sur l'une des demi-journées de cette liste seront prises en compte.
    :return: Nouvelle liste de tournées filtrées.
    Une valeur None sur l'une des listes en paramètre permet d'évacuer la contrainte
    """

    tourneesFiltrees = []

    for tournee in tournees:

        # Contrainte sur les demi-journées
        if demiJours == None or tournee.demiJour.num in demiJours:

            # Contrainte sur les producteurs et clients
            prodContrainte = (producteursId == None or tournee.producteur.id in producteursId)
            clContrainte = (clientsId == None)

            # Si le producteur n'est pas le pilote da la tournée, il peut être aussi impliqué par son passage chez-lui
            # De la même manière que pour les clients
            # On doit donc parcourir les taches et comparer avec les lieux où elles se passent
            t = 0
            while (not prodContrainte or not clContrainte) and t < len(tournee.taches):
                idActeur = tournee.taches[t].lieu.id
                prodContrainte = prodContrainte or idActeur in producteursId
                clContrainte = clContrainte or idActeur in clientsId
                t+=1

            if prodContrainte and clContrainte:
                tourneesFiltrees.append(tournee)

    return tourneesFiltrees