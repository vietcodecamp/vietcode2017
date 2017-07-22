# mate 2D pole o velikosti 3x3
# v poli je bud "O" a "X" nebo " "
# vypada nasledovne
# [["X", "O", " "],
#  ["X", " ", "O"],
#  ["X", "O", " "]]

# Dopln funkci, co vypise, jestli vyhral hrac1 (X), nebo hrac2(O), nebo pokud nevyhraje ani jeden

def vyhral_hrac(pole: list, hrac: str) -> bool:
    if (pole[0][0] == hrac and pole[0][1] == hrac and pole[0][2] == hrac) or \
            (pole[1][0] == hrac and pole[1][1] == hrac and pole[1][2] == hrac) or \
            (pole[2][0] == hrac and pole[2][1] == hrac and pole[2][2] == hrac) or \
            (pole[0][0] == hrac and pole[1][0] == hrac and pole[2][0] == hrac) or \
            (pole[0][1] == hrac and pole[1][1] == hrac and pole[2][1] == hrac) or \
            (pole[0][2] == hrac and pole[1][2] == hrac and pole[2][2] == hrac) or \
            (pole[0][0] == hrac and pole[1][1] == hrac and pole[2][2] == hrac) or \
            (pole[0][0] == hrac and pole[1][1] == hrac and pole[2][2] == hrac) or \
            (pole[0][2] == hrac and pole[1][1] == hrac and pole[2][0] == hrac): \
            return True
    return False


def kdo_vyhral(pole):
    x = "X"
    o = "O"
    if vyhral_hrac(pole, x):
        print(x)
    elif vyhral_hrac(pole, o):
        print(o)
    else:
        print("Nikdo nevyhral")
