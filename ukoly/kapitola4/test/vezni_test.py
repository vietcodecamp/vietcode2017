import unittest
from ukoly.kapitola4.vezni import *


class MyTestCase(unittest.TestCase):
    def test_pole_append(self):
        nove_pole = pole_append()
        self.assertEqual(nove_pole, ["Zlodej Petr", "Pedofil Honza", "Vrah David", "Dacos", "Roman", "BFU", "ABFU"])

    def test_pole_sort(self):
        nove_pole = pole_sort()
        self.assertEqual(nove_pole, ['ABFU', 'BFU', 'Dacos', 'Pedofil Honza', 'Roman', 'Vrah David', 'Zlodej Petr'])

    def test_pole_remove_index(self):
        nove_pole = pole_remove_index()
        self.assertEqual(nove_pole, ["Dacos", "Pedofil Honza", "Roman", "Vrah David", "Zlodej Petr"])

    def test_pole_pop(self):
        nove_pole = pole_pop()
        self.assertEqual(nove_pole, ["Dacos", "Pedofil Honza", "Roman", "Vrah David"])

    def test_pole_remove(self):
        nove_pole = pole_remove()
        self.assertEqual(nove_pole, ["Pedofil Honza", "Vrah David"])


if __name__ == '__main__':
    unittest.main()
