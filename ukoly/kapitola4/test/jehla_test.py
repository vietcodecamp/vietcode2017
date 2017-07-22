import unittest
from contextlib import redirect_stdout
from io import StringIO
from ukoly.kapitola4.jehla import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_kupka_sena(self):
        with redirect_stdout(self.out):
            kupka_sena()
            self.assertEqual(self.out.getvalue(), "6\n4\n1\n")


if __name__ == '__main__':
    unittest.main()
