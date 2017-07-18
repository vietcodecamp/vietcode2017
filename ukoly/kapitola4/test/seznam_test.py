import unittest
from contextlib import redirect_stdout
from io import StringIO
from ukoly.kapitola4.seznam import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_inicializace_pole(self):
        with redirect_stdout(self.out):
            inicializace_pole()
            self.assertEqual(self.out.getvalue(), "[1, 2, 10, 5]\n")


if __name__ == '__main__':
    unittest.main()
