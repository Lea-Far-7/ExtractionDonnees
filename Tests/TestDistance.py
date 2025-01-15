import unittest

from Modules.distance import Distance 

class TestDistance(unittest.TestCase):

    def test_distance(self):
        result = Distance.distance([15.24, -11.49], [175.42, 27.53])
        self.assertEqual(result, 16.52)

if __name__ == '__main__':
    unittest.main()