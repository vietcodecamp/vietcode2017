import unittest
from spocitatSamohlasky import spocitatSamohlasky

class MyTestCase(unittest.TestCase):
    
    def test(self):
        self.assertEqual(spocitatSamohlasky("abracadabra"), 5)

if __name__ == '__main__':
    unittest.main()
