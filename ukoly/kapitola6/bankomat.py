# Naprogramuj jednoduchy bankomat.
# Pokud cislo karty se nebude rovnat 43-1199223344, tak vypis: "Neplatna karta! Vracim kartu!"
# Pokud zada spravne cislo karty, tak se overi cislo pinu. Pokud se pin nebude rovnat 3194, tak vypis: "Neplatny PIN! Vracim kartu!"
# Uzivatel si chce vybrat penize, ale ma na uctu jenom 1000 Kc. Pokud chce vybrat vic jak 1000, tak vypis: "Nedostatek penez na uctu! Vracim kartu!"
# Pokud vsechno projde, tak vypis: "Vyplacim [castka] Kc"


platna_karta = "43-1199223344"
platny_pin = 3194
zustatek_na_uctu = 1000

def bankomat(cislo_karty :str, pin :int, castka :int):
    if cislo_karty != platna_karta:
        print("Neplatna karta! Vracim kartu!")
        return
    if pin != platny_pin:
        print("Neplatny PIN! Vracim kartu!")
        return
    if castka > zustatek_na_uctu:
        print("Nedostatek penez na uctu! Vracim kartu!")
        return
    print("Vyplacim " + str(castka) + " Kc")