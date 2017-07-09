import unittest
from calculator import *


class MyTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5,3), 8)

    def test_sub(self):
        self.assertEqual(sub(5,3), 2)

if __name__ == '__main__':
    unittest.main()
