# Dopln implementaci funkce, ktera porovna delku dvou seznamu
def porovnej(seznam1: list, seznam2: list):
    d1 = len(seznam1)
    d2 = len(seznam2)
    if d1 > d2:
        return "prvni seznam je delsi"
    elif d1 == d2:
        return "seznamy jsou stejne dlouhe"
    else:
        return "druhy seznam je delsi"
