import unittest
from contextlib import redirect_stdout
from io import StringIO
from ukoly.kapitola4.vypis_prvek import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_vypis_prvek(self):
        with redirect_stdout(self.out):
            vypis_prvek()
            self.assertEqual(self.out.getvalue(), "banh mi\n")


if __name__ == '__main__':
    unittest.main()
