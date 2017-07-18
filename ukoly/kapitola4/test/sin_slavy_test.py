import unittest
from ukoly.kapitola4.sin_slavy import *

legends = ["Einstein", "Newton", "Dacos", "Napoleon", "Caesar", "Musk", "Gates", "Jobs"]


class MyTestCase(unittest.TestCase):
    def test_pole_pridej(self):
        nove_pole = pole_pridej()
        self.assertEqual(len(nove_pole), len(legends) + 1)
        self.assertEqual(nove_pole[:-1], legends)
        self.assertNotEqual(nove_pole[-1], "Jobs")

    def test_pole_smaz(self):
        nove_pole = pole_smaz()
        self.assertEqual(len(nove_pole), len(legends) - 1)
        self.assertEqual(nove_pole, ["Einstein", "Newton", "Dacos", "Napoleon", "Caesar", "Gates"])

    def test_pole_obrat(self):
        nove_pole = pole_obrat()
        self.assertEqual(nove_pole, ['Jobs', 'Gates', 'Musk', 'Caesar', 'Napoleon', 'Dacos', 'Newton', 'Einstein'])

    def test_pole_prepis(self):
        nove_pole = pole_prepis()
        self.assertEqual(len(nove_pole), len(legends))
        self.assertEqual(nove_pole[3], "Roman")

if __name__ == '__main__':
    unittest.main()
