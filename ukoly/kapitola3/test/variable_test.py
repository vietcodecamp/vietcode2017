import unittest
from contextlib import redirect_stdout
from io import StringIO
from ukoly.kapitola3.variable import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_assign_value_to_variable(self):
        with redirect_stdout(self.out):
            assign_value_to_variable()
            self.assertEqual(self.out.getvalue(), "uranus, slunecnice, Odin\n")


if __name__ == '__main__':
    unittest.main()
