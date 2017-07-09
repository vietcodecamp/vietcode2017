import unittest
from contextlib import redirect_stdout
from io import StringIO
from ukoly.kapitola3.gravity import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_something(self):
        with redirect_stdout(self.out):
            gravity_value()
            self.assertEqual(self.out.getvalue(), "9.81 m/s2\n")


if __name__ == '__main__':
    unittest.main()
