# Vypis (s pomoci funkce input).
# Zadej prosim cislo x:
# Zadej prosim cislo y:
# Uzivatel zada cislo x a pote cislo y

# Vypis soucet mezi x a y.
# Soucet je: [soucet x a y]
def soucet():
    x = int(input("Zadej prosim cislo x:"))
    y = int(input("Zadej prosim cislo y:"))
    soucet = x + y
    print("Soucet je: " + str(soucet))


# Vypis rozdil mezi x a y.
# Rozdil je: [rozdil x a y]
def rozdil():
    x = int(input("Zadej prosim cislo x:"))
    y = int(input("Zadej prosim cislo y:"))
    rozdil = x - y
    print("Rozdil je: " + str(rozdil))


# Vypis soucin mezi x a y.
# Soucin je: [soucin x a y]
def soucin():
    x = int(input("Zadej prosim cislo x:"))
    y = int(input("Zadej prosim cislo y:"))
    soucin = x * y
    print("Soucin je: " + str(soucin))

# Vypis podil se zbytkem mezi x a y.
# Podil se zbytkem je: [podil x a y]
def podil_se_zbytkem():
    x = int(input("Zadej prosim cislo x:"))
    y = int(input("Zadej prosim cislo y:"))
    podil = x / y
    print("Podil se zbytkem je: " + str(podil))

# Vypis celociselny podil mezi x a y.
# Celociselny podil je: [podil x a y]
def podil_celociselny():
    x = int(input("Zadej prosim cislo x:"))
    y = int(input("Zadej prosim cislo y:"))
    podil = x // y
    print("Celociselny podil je: " + str(podil))


