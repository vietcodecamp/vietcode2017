import unittest
from ukoly.kapitola4.porovnani_delky import *


class MyTestCase(unittest.TestCase):
    def test_porovnej_druhy_delsi(self):
        self.assertEqual(porovnej([1, 2, 3], [1, 2, 3, 4]), "druhy seznam je delsi")

    def test_porovnej_prvni_delsi(self):
        self.assertEqual(porovnej([1, 2, 3], [1, 2]), "prvni seznam je delsi")

    def test_porovnej_stejne_dlouhe(self):
        self.assertEqual(porovnej([1, 2, 3], [1, 2, 66]), "seznamy jsou stejne dlouhe")


if __name__ == '__main__':
    unittest.main()
