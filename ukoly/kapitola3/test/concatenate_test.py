import unittest
from contextlib import redirect_stdout
from io import StringIO
from ukoly.kapitola3.concatenate import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_concatenate_with_percentage_operator(self):
        with redirect_stdout(self.out):
            concatenate_with_percentage_operator()
            self.assertEqual(self.out.getvalue(), "Jmenuji se Boromir a jsem clovek. Moji oblibenou zbrani se stal mec "
                                                  "a muj ukol je ochranit nositele prstenu moci.\n")

    def test_concatenate_with_format(self):
        with redirect_stdout(self.out):
            concatenate_with_format()
            self.assertEqual(self.out.getvalue(), "Jmenuji se Boromir a jsem clovek. Moji oblibenou zbrani se stal mec "
                                                  "a muj ukol je ochranit nositele prstenu moci.\n")


if __name__ == '__main__':
    unittest.main()
