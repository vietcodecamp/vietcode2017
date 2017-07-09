import unittest
from contextlib import redirect_stdout
from io import StringIO
from ukoly.kapitola3.my_string import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_my_uppercase_string(self):
        with redirect_stdout(self.out):
            my_uppercase_string()
            output = self.out.getvalue().split('\n')
            string_value = output[0]
            self.assertTrue(string_value.isupper())
            string_len = output[1]
            self.assertEqual(int(string_len), len(string_value))


if __name__ == '__main__':
    unittest.main()
