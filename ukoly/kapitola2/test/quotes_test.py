import unittest
from contextlib import redirect_stdout
from io import StringIO

from ukoly.kapitola2.quotes import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_double_quotes(self):
        with redirect_stdout(self.out):
            double_quotes()
        self.assertEqual(self.out.getvalue(), 'Alenka rekla: "Bez mi koupit rohliky, Honzo."\n')

    def test_single_quotes(self):
        with redirect_stdout(self.out):
            single_quotes()
        self.assertEqual(self.out.getvalue(), "Alenka rekla: 'Bez mi koupit rohliky, Honzo.'\n")


if __name__ == '__main__':
    unittest.main()
