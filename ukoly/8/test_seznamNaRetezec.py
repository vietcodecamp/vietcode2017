import unittest
from seznamNaRetezec import naRetezec

class MyTestCase(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(naRetezec(['apples', 'bananas', 'tofu', 'cats']), 'apples, bananas, tofu, and cats')

if __name__ == '__main__':
    unittest.main()
