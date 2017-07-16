import unittest
from unittest import mock
from contextlib import redirect_stdout
from io import StringIO

from ukoly.kapitola3.input import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_input_name(self):
        with mock.patch('builtins.input', return_value='VietCode'):
            with redirect_stdout(self.out):
                input_name()
                self.assertEqual(self.out.getvalue(), "Delka tveho jmena je 8\n")

    def test_input_age(self):
        with mock.patch('builtins.input', return_value='23'):
            with redirect_stdout(self.out):
                input_age()
                self.assertEqual(self.out.getvalue(), "Zbyva ti 42 let do duchodu!\n")

    def test_input_power(self):
        with mock.patch('builtins.input', return_value='234'):
            with redirect_stdout(self.out):
                input_power()
                self.assertEqual(self.out.getvalue(), "54756\n")

if __name__ == '__main__':
    unittest.main()
