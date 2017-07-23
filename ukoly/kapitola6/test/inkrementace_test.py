import unittest
from ukoly.kapitola6.inkrementace import *


class MyTestCase(unittest.TestCase):
    def test_inkrementuj(self):
        nove_pole = inkrementuj([1, 3, 6, 4, 10, 1999, 0, -1])
        self.assertEqual(nove_pole, [2, 4, 7, 5, 11, 2000, 1, 0])


if __name__ == '__main__':
    unittest.main()
