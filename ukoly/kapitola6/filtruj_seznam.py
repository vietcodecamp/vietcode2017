# doplnte funkci, aby vytiskla vsechny prvky seznamu,
# ktere jsou mensi nez 5
# mate prototyp, ktery vytiskne vsechny prvky 

def filtr(seznam):
    for prvek in seznam:
        if prvek < 5:
            print(prvek)


# Jste schopni upravit funkci filter_2 tak, aby slo nastavit
# jine cislo na porovnani nez jenom 5? S pomoci parametru funkce
def filtr_2(seznam, limit):
    for prvek in seznam:
        if prvek < limit:
            print(prvek)
