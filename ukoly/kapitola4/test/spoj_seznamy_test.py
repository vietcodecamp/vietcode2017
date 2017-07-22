import unittest
from ukoly.kapitola4.spoj_seznamy import *


class MyTestCase(unittest.TestCase):
    def test_spoj_seznamy(self):
        novy_seznam = spoj_seznamy()
        self.assertEqual(novy_seznam, ["ahoj", "tady", "se", "to", "ma", 'spojit', 'a', 'vzniknout', 'jeden', 'seznam'])


if __name__ == '__main__':
    unittest.main()
