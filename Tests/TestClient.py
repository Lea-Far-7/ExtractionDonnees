import unittest

from Metier.acteur import Acteur
from Metier.demiJour import DemiJour
from Metier.client import Client 

class TestClient(unittest.TestCase):

    # Creation de demiJours
    dj1 = DemiJour(7, "Jeudi M")
    dj2 = DemiJour(3, "Mardi M")
    dj3 = DemiJour(8, "Jeudi AM")
    dj4 = DemiJour(1, "Lundi M")

    # Creation de clients
    client0 = Client(144.36546, -146.346546, [dj1])
    client1 = Client(165.346546, 34.346546, [dj2, dj4])

    def test_affichageInfos(self):
        result = Client.__str__(TestClient.client0)
        self.assertEqual(result, "Client 0 :\nCoordonnées : (144.365460 ; -146.346546) \nDispos : dj1")

    def test_repr(self):
        result = Client.__repr__(TestClient.client1)
        self.assertEqual(result, "Client 1")


if __name__ == '__main__':
    unittest.main()