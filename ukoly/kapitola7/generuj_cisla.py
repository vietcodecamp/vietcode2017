# Popros uzivatele pomoci funkce input: "Zadej prosim nejake nezaporne cislo: "
# Pokud zada cislo mensi nebo rovno 0, tak vypis: "BFU detected! Prosim priste zadej NEZAPORNE cislo!"
# Vypis vsechny druhe mocniny cisel od 1 do zadaneho cisla pomoci ridici struktury for.
# Uzivatel zada napr. cislo 6, tak vypises:
# 1
# 4
# 9
# 16
# 25
# 36
def generuj_cisla_for():
    cislo = int(input("Zadej prosim nejake nezaporne cislo: "))
    if cislo <= 0:
        print("BFU detected! Prosim priste zadej NEZAPORNE cislo!")
        return
    for i in range(cislo):
        print(i**2)


# Udelej to same co nahore, akorat s pomoci ridici struktury while.
def generuj_cisla_while():
    cislo = int(input("Zadej prosim nejake nezaporne cislo: "))
    if cislo <= 0:
        print("BFU detected! Prosim priste zadej NEZAPORNE cislo!")
        return
    i = 1
    while i <= cislo:
        print(i**2)
        i = i + 1
