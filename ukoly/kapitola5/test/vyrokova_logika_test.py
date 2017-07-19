import unittest
from ukoly.kapitola5.vyrokova_logika import *


class MyTestCase(unittest.TestCase):
    def test_hadka(self):
        self.assertTrue(hadka(True, True, False, False))
        self.assertTrue(hadka(False, True, True, False))
        self.assertTrue(hadka(True, False, False, True))
        self.assertFalse(hadka(False, False, False, False))
        self.assertTrue(hadka(True, True, True, True))

    def test_vysoky_tlak(self):
        self.assertTrue(vysoky_tlak(121, 81))
        self.assertTrue(vysoky_tlak(120, 81))
        self.assertTrue(vysoky_tlak(121, 80))
        self.assertFalse(vysoky_tlak(120, 80))

    def test_detektor_lzi(self):
        self.assertTrue(detektor_lzi(True, False, 91))
        self.assertTrue(detektor_lzi(False, True, 91))
        self.assertTrue(detektor_lzi(True, False, 91))
        self.assertTrue(detektor_lzi(True, True, 91))
        self.assertFalse(detektor_lzi(False, False, 91))
        self.assertFalse(detektor_lzi(True, True, 80))

if __name__ == '__main__':
    unittest.main()
