import unittest
from contextlib import redirect_stdout
from io import StringIO
from ukoly.kapitola4.iterace import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_umocni(self):
        with redirect_stdout(self.out):
            umocni([1, 2, 3, 4, 5, 11])
            self.assertEqual(self.out.getvalue(), "1\n4\n9\n16\n25\n121\n")


if __name__ == '__main__':
    unittest.main()
