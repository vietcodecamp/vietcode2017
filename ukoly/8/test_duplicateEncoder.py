import unittest
from duplicateEncoder import duplicate_encode

class MyTestCase(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(duplicate_encode("din"),"(((")

    def test2(self):
        self.assertEqual(duplicate_encode("recede"),"()()()")

    def test3(self):
        self.assertEqual(duplicate_encode("Success"),")())())","should ignore case")

    def test4(self):
        self.assertEqual(duplicate_encode("(( @"),"))((")

if __name__ == '__main__':
    unittest.main()
