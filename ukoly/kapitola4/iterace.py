# Nasledujici kod navstivi kazdy prvek pole seznam
# Uprav funkci, aby pro dany seznam vypis druhe mocniny vsech jeho prvku
# Vstup: [1, 2, 3, 4, 5]
# Vypise se:
# 1
# 4
# 9
# 16
# 25

def umocni(seznam: list):
    for prvek in seznam:
        print(prvek**2)
