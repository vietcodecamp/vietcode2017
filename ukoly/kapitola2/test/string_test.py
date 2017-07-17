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

    def test_char_1st(self):
        with redirect_stdout(self.out):
            char_1st()
        self.assertEqual(self.out.getvalue(), "M\n")

    def test_char_last(self):
        with redirect_stdout(self.out):
            char_last()
        self.assertEqual(self.out.getvalue(), ".\n")

    def test_char_100th_last(self):
        with redirect_stdout(self.out):
            char_100th_last()
        self.assertEqual(self.out.getvalue(), "b\n")

    def test_char_first_52(self):
        with redirect_stdout(self.out):
            char_first_52()
        self.assertEqual(self.out.getvalue(), "Má kresba ovšem není zdaleka tak půvabná jako model.\n")

    def test_char_from_100(self):
        with redirect_stdout(self.out):
            char_from_100()
        self.assertEqual(self.out.getvalue(), "ířské kariéry,když mi bylo šest let, a proto jsem se nenaučil kreslit "
                                              "nic jiného než zavřené a otevřené hroznýše. Udiveně jsem se díval na ten"
                                              " zjev. Považte jen, že jsem byl na tisíc mil od jakéhokoliv obydleného"
                                              " kraje. A můj človíček nevypadal, jako by zabloudil ani jako by byl na "
                                              "smrt unavený nebo vyhladovělý, polomrtvý žízní nebo na smrt vylekán.\n")

    def test_repeated_string(self):
        with redirect_stdout(self.out):
            repeated_string()
        self.assertEqual(self.out.getvalue(),
                         "Viet Code je nejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnej"
                         "nejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnej"
                         "nejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnejnej"
                         "nejnejnejnejnejnejnejnejnejnejnejnejlepsi kurz ever!\n")


if __name__ == '__main__':
    unittest.main()
