# Vypis "Jake je tvoje jmeno? ". A potom pozadej souseda, aby zadal sve jmeno.
# Po zadani jmena vypis delku zadaneho jmena. "Delka tveho jmena je [delka_jmena]"
def input_name():
    jmeno = input("Jake je tvoje jmeno? ")
    delka_jmena = len(jmeno)
    print("Delka tveho jmena je " + str(delka_jmena))
    pass


# Vypis "Kolik je ti let? ". Pozadej souseda o jeho vek.
# Oznam mu kolik let mu zbyva do duchodu tak, ze vypises "Zbyva ti [pocet_roku] let do duchodu!"
# Do duchodu pujdeme v 65 letech.
def input_age():
    vek = input("Kolik je ti let? ")
    let_do_duchodu = 65 - int(vek)
    print("Zbyva ti " + str(let_do_duchodu) + " let do duchodu!")
    pass


# Vypis "Druha mocnina z: "
# Zadej cislo a vypis druhou mocninu ze zadaneho cisla
def input_power():
    cislo = input("Druha mocnina z: ")
    print(int(cislo)**2)
    pass
