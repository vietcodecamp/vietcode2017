import random
import math
def RNG():
    try:
        min_number = int(input("Zadej, od jakeho cisla chces hadat. "))
        if min_number < 0:
            min_number = 0
            print("Musis hadat v kladnych cislech nastavuju na 0")

    except ValueError:
        min_number = 0
        print("To neni cele cislo, nastavuji nejmensi cislo na 0.")

    try:
        max_number = int(input("Zadej, do jakeho cisla chces hadat. "))
        if max_number < 0:
            max_number = min_number + 20
            print("Musis hadat v kladnych cislech nastavuju na " + str(min_number+20))

    except ValueError:
        max_number = min_number+20
        print("To neni cele cislo, nastavuji cislo na " + str(max_number)+".")

    try:
        x = int(input("Na kolik pokusu si myslis, ze to das(moc pokusu, moc easy)? "))
        if x < 0:
            x = abs(x)
            print("Nemuzes zaporny pocet pokusu, udelam ti z toho kladny pocet pokusu ")

    except ValueError:
        x = 5
        print("Za trest mas jen 5 pokusu.")

    if min_number > max_number:
        z = min_number
        min_number = max_number
        max_number = z
    nahodne_cislo = random.randint(min_number,max_number)
    print("Mas " + str(x) + " pokusu na tipnuti cisla.")

    for y in range(x):

        try:
            cislo = int(input("Tipni si cislo od "+ str(min_number) + " do "+ str(max_number)+ "."))
            print("Zbyva ti "+ str(int(x - (y+1)))+" pokusu.")
            print()

            if cislo == nahodne_cislo:
                print("Ale, ty jsi to dal, CG.")
                break

            elif cislo>nahodne_cislo:
                print("Zkus mensi.")

            elif cislo<nahodne_cislo:
                print("Zkus vetsi.")

        except ValueError:
            print()
            print("To neni cele cislo. Smula, mas o pokus mene.")
            print("Zbyva ti " + str(int(x - (y+1))) + " pokusu.")

    else:
        print("Neuhadl jsi, smolik.")
        print("Hledane cislo bylo " + str(nahodne_cislo))

vetsi = "vetsi"
mensi = "mensi"
rovno = "rovno"

def AI():
    ans = ""

    try:
        x = int(input("Zadej do jakeho cisla myslis. "))

        if x > 0:
            x = x//2
            y = x

        else:
            print("Hadame v kladnych cislech, takze si mysli cislo od 0 do 100 ")
            x = 100

    except ValueError:
        print("Neplatny vstup, vyberu za tebe cislo 20. Mysli si cislo od 0 do 20 ")
        x = 20
        x = x//2
        y = x
    while ans != rovno:
        ans = input("Je tvoje cislo vetsi/mensi/rovno " + str(x)+ " ")

        if ans == vetsi:
            x = math.ceil(y/2 + x)

            if y//2 == 0:
                y = 1

            else:
                y = y//2

        elif ans == mensi:
            x = math.floor(x - y/2)

            if y//2 == 0:
                y = 1

            else:
                y = y//2

        elif ans == rovno:
            print("Tvoje cislo je " + str(x) + " ")
            break

        else:
            print("Neplatny vstup. Zadej vetsi/mensi/rovno ")

print("1 - Pokud chces hadat cislo. ")
print("2 - Pokud si chces myslet cislo ")
print("3 - Pokud chces hadat a pak si myslet cislo ")
x = input("konec - Zadej konec pro ukonceni ")
while x != 1 or 2 or 3 or "konec":

    if x == "1":
        RNG()
        print()
        x = input("Zadej konec pro ukonceni, nebo 2/3 pro zmenu hry ")
    elif x == "2":
        AI()
        print()
        x = input("Zadej konec pro ukonceni, nebo 1/3 pro zmenu hry ")
    elif x == "3":
        RNG()
        print()
        AI()
        print()
        x = input("Zadej konec pro ukonceni, nebo 1/2 pro zmenu hry ")

    elif x == "konec":
        print("Diky za hru ")
        break

    else:
        print("Neplatna volba, zadej 1/2/3 ")
        x = input()