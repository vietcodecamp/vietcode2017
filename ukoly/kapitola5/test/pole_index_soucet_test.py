import unittest
from ukoly.kapitola5.pole_index_soucet import *


class MyTestCase(unittest.TestCase):
    def test_pole_index_soucet(self):
        soucet = pole_index_soucet([3, 1, 3, 66, 1, 5, 8, 2, 11, 5, 8])
        self.assertEqual(soucet, 77)

if __name__ == '__main__':
    unittest.main()
