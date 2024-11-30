## Programme pour calculer la distance entre 2 points sur Terre avec leurs coordonnées

from math import *
r = 6371 #rayon de la Terre en km

def distance(A:list,B:list):
    """Calcule la distance en km entre deux points sur Terre
    A et B sont les couples (listes) de coordonnées (latitude, longitude) en degrés des 2 points
    """

    A[0],A[1],B[0],B[1] = radians(A[0]), radians(A[1]), radians(B[0]), radians(B[1])

    # distance orthodromique (avec formule de haversine)
    # https://fr.wikipedia.org/wiki/Distance_du_grand_cercle

    d = 2 * r * asin(sqrt( sin((B[0]-A[0])/2)**2 + ( cos(A[0]) * cos(B[0]) * (sin((B[1]-A[1])/2)**2) ) ))

    return round(d,2)


if __name__ == '__main__':
    A_la = float(input('Latitude du point A (en °): '))
    A_lo = float(input('Longitude du point A (en °): '))
    B_la = float(input('Latitude du point B (en °): '))
    B_lo = float(input('Longitude du point B (en °): '))
    print('→ '+ str(distance([A_la,A_lo],[B_la,B_lo])) + ' km')