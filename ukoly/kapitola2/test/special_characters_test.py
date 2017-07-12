import unittest
from contextlib import redirect_stdout
from io import StringIO

from ukoly.kapitola2.special_characters import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_backslash(self):
        with redirect_stdout(self.out):
            backslash()
            self.assertEqual(self.out.getvalue(), "\\")

    def test_new_line_escaping(self):
        with redirect_stdout(self.out):
            new_line_escaping()
            self.assertEqual(self.out.getvalue(), "D:\moje_serialy\\naruto\n")

    def test_unicode(self):
        with redirect_stdout(self.out):
            unicode()
            self.assertEqual(self.out.getvalue(), "I ♥ Viet Code!\n")

if __name__ == '__main__':
    unittest.main()
