# Predpoved vysledek kazdeho print radku.

def salam():
    parky = 'lokalni salam'
    print(parky)
def slanina():
    parky = 'lokalni slanina'
    print(parky)
    salam()
    print(parky)

parky = 'globalni'
slanina()
print(parky)
