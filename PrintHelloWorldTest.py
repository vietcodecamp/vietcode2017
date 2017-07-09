import unittest
from contextlib import redirect_stdout
from io import StringIO
from PrintHelloWorld import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.out = StringIO()

    def test_print_hello_world(self):
        with redirect_stdout(self.out):
            print_hello_world()
        self.assertEqual(self.out.getvalue(), "Hello World!\n")

    def test_concatenate_string(self):
        with redirect_stdout(self.out):
            concatenate_string()
        self.assertEqual(self.out.getvalue(), "ABC\n")


if __name__ == '__main__':
    unittest.main()
