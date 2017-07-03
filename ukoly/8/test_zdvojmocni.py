import unittest
from zdvojmocni import zdvojmocni

class MyTestCase(unittest.TestCase):
    
    def test(self):
        self.assertEqual(zdvojmocni(9119), 811181)

if __name__ == '__main__':
    unittest.main()
