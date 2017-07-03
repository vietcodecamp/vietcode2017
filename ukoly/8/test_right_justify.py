import unittest
from right_justify import right_justify

class MyTestCase(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(right_justify('hello world'), '                                                           hello world')

if __name__ == '__main__':
    unittest.main()
