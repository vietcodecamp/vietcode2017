import unittest
from fujSamohlasky import fujSamohlasky

class TestSamohlasky(unittest.TestCase):
    
    def test(self):
        self.assertEqual(fujSamohlasky("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")

if __name__ == '__main__':
    unittest.main()
