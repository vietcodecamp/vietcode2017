# doplnte funkci, aby vytiskla vetsi ze dvou cisel
# nepouzivejte vestavenou funkci max
def moje_maximum(cislo1, cislo2):
    if cislo1 > cislo2:
        print(cislo1)
    else:
        print(cislo2)


# doplnte funkci, aby vytiskla nejvetsi ze tri cisel
def moje_maximum_3(cislo1, cislo2, cislo3):
    if (cislo1 >= cislo2) and (cislo1 >= cislo3):
        print(cislo1)
        return
    if (cislo2 >= cislo1) and (cislo2 >= cislo3):
        print(cislo2)
        return
    if (cislo3 >= cislo1) and (cislo3 >= cislo2):
        print(cislo3)
        return
