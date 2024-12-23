from Metier.producteur import Producteur
from Metier.client import Client
from Metier.acteur import Acteur
from Metier.tache import Tache
from Metier.tournee import Tournee
from Metier.demiJour import DemiJour
from Modules.ListeDemiJours import ListeDemiJours
"""
TODO
Chaque fichier solution est composé de plusieurs tournées
Renvoyer une liste de tournées pour chaque fichier

Pour chaque tournée :
Extraction première ligne : numéro de producteur et numéro de la demi-journée correspondante
Deuxième ligne = les noeuds visités (sans le prod qui fait la tournée)
-> un noeud peut être un producteur ou un client avec num prod de 0 à nbProd - 1 et num client de nbProd à nbProd+nbClients - 1
-> récupérer sous forme de liste d'entiers

Chaque ligne ensuite = une tâche
-> un type (P ou D)
-> Une charge (float : celle de la demande)
-> Le lieu de la tâche = un Acteur (Producteur pour pick-up et Client pour Drop-off)
-> info sur la requête : Acteur associé à l'action (Client pour pick-up et Producteur pour Drop-off)
-> Horaire de l'action : HH:MM
"""

