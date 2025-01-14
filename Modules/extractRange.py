def extractRange(text: str) -> list[int]:

    """
    Extrait la liste triée des nombres à partir d'un texte contenant des plages et des valeurs séparées par des virgules.

    :param text: Chaîne spécifiant des plages et des nombres (exemple : "1-5, 8, 11-13")
    :return: Liste triée des nombres extraits
    """

    values = []

    # Supprime les espaces et récupère chaque entrée
    elements = text.replace(" ", "").split(",")

    for element in elements:
        if '-' in element:
            # Si c'est une plage
            start, end = map(int, element.split('-'))   # Récupère les entiers de chaque côté du tiret
            values.extend(range(start, end+1))    # Ajoute tous les nombres de la plage
        else:
            # Si c'est un nombre unique
            values.append(int(element))

    return sorted(values)


if __name__ == '__main__':
    print(extractRange("1-5, 8, 11-13"))