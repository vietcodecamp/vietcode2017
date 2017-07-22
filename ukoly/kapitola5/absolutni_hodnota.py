# doplnte funkci, aby vzala vstup (cisla) od uzivatele
# a nasledne vypsala jeji absolutni hodnotu
# vypis "absolutni hodnota je [cislo]"

def absolutni_hodnota():
    cislo = int(input("Zadej cele cislo: "))
    if cislo < 0:
        cislo = - cislo
    print("absolutni hodnota je " + str(cislo))
