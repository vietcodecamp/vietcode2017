import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest import mock

from ukoly.kapitola5.aritmetika import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def input_mock(self):
        def mock_input(prompt):
            if "Zadej prosim cislo x:" in prompt:
                return 7
            if "Zadej prosim cislo y:" in prompt:
                return 3

        return mock_input

    def test_soucet(self):
        mock_input = self.input_mock()
        with mock.patch('builtins.input', mock_input):
            with redirect_stdout(self.out):
                soucet()
                self.assertEqual(self.out.getvalue(), "Soucet je: 10\n")

    def test_rozdil(self):
        mock_input = self.input_mock()
        with mock.patch('builtins.input', mock_input):
            with redirect_stdout(self.out):
                rozdil()
                self.assertEqual(self.out.getvalue(), "Rozdil je: 4\n")

    def test_soucin(self):
        mock_input = self.input_mock()
        with mock.patch('builtins.input', mock_input):
            with redirect_stdout(self.out):
                soucin()
                self.assertEqual(self.out.getvalue(), "Soucin je: 21\n")

    def test_podil_se_zbytkem(self):
        mock_input = self.input_mock()
        with mock.patch('builtins.input', mock_input):
            with redirect_stdout(self.out):
                podil_se_zbytkem()
                self.assertEqual(self.out.getvalue(), "Podil se zbytkem je: 2.3333333333333335\n")

    def test_podil_celociselny(self):
        mock_input = self.input_mock()
        with mock.patch('builtins.input', mock_input):
            with redirect_stdout(self.out):
                podil_celociselny()
                self.assertEqual(self.out.getvalue(), "Celociselny podil je: 2\n")


if __name__ == '__main__':
    unittest.main()
