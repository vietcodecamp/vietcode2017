import unittest
from contextlib import redirect_stdout
from io import StringIO

from ukoly.kapitola2.string import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_string_length(self):
        with redirect_stdout(self.out):
            string_length()
        self.assertEqual(self.out.getvalue(), "450\n")

    def test_uppercase(self):
        with redirect_stdout(self.out):
            upper_case()
        self.assertEqual(self.out.getvalue(),
                         "MÁ KRESBA OVŠEM NENÍ ZDALEKA TAK PŮVABNÁ JAKO MODEL.ALE ZA TO JÁ NEMOHU. "
                         "DOSPĚLÍ MĚ ODRADILI OD MALÍŘSKÉ KARIÉRY,KDYŽ MI BYLO ŠEST LET, "
                         "A PROTO JSEM SE NENAUČIL KRESLIT NIC JINÉHO NEŽ ZAVŘENÉ A OTEVŘENÉ HROZNÝŠE. "
                         "UDIVENĚ JSEM SE DÍVAL NA TEN ZJEV. POVAŽTE JEN, "
                         "ŽE JSEM BYL NA TISÍC MIL OD JAKÉHOKOLIV OBYDLENÉHO KRAJE. A MŮJ ČLOVÍČEK NEVYPADAL, "
                         "JAKO BY ZABLOUDIL ANI JAKO BY BYL NA SMRT UNAVENÝ NEBO VYHLADOVĚLÝ, "
                         "POLOMRTVÝ ŽÍZNÍ NEBO NA SMRT VYLEKÁN.\n")

    def test_char_127th(self):
        with redirect_stdout(self.out):
            char_127th()
        self.assertEqual(self.out.getvalue(), "š\n")


if __name__ == '__main__':
    unittest.main()
