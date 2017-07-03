# 1.Co myslis, ze bude vysledkem spusteni tohoto programu? Zjisti to.

# 2.Zmen funkci dvakrat() tak, aby prijmula dva argumenty - funkci a hodnotu. Dale
# by funkce dvakrat() mela vyvolat tu funkci dvakrat s tou hodnotou jako argument.

# 3.Pouzij svoji modifikovanou funkci dvakrat() a vyvolej funkci print_twice()
# dvakrat s argumentem 'spam'

# 4.Vytvor novou funkci ctyrikrat(), ktera prijma dva argumenty - hodnotu a funkci,
# kterou vyvola ctyrikrat s argumentem te hodnoty. Tato funkce by mela obsahovat
# pouze 2 radky.

# 5.Napis funkci, ktera nakresli obrazek nize:

'''

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

'''

# Napoveda: pouzij predchozi funkce a print('+', '-') nebo print('+', end=' ')

# 6.Vytvor funkci, ktera nakresli podobny obrazek, ale s 4 radky a 4 sloupci


def dvakrat(f):
    f()
    f()

def print_spam():
    print('spam')

dvakrat(print_spam)

def print_twice(honza):
    print(honza)
    print(honza)
