# Jaky je vysledek kazdeho radku? Vyzkousej si v Python interaktivni konzoli
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)


# Doma nastane hadka v pripade kdyz se potkaji:
# 1. sestra a bratr nebo
# 2. bratr a mama nebo
# 3. sestra a tata
def hadka(sestra_prijde: bool, bratr_prijde: bool, mama_prijde: bool, tata_prijde: bool):
    pohadaji_se = (sestra_prijde and bratr_prijde) or (bratr_prijde and mama_prijde) or (sestra_prijde and tata_prijde)
    return pohadaji_se


# Zjisti, zda ma uzivatel vysoky tlak. Clovek ma ysoky tlak prave tehdy,
# kdyz hodnota systolic je vetsi nez 120
# nebo kdyz hodnota diastolic je vetsi nez 80
def vysoky_tlak(systolic: int, diastolic: int):
    ma_vysoky_tlak = (systolic > 120) or (diastolic > 80)
    return ma_vysoky_tlak


# Zjisti, zda vezen lze. Vezen lze pokud
# ma tep srdce vyssi nez 90 uderu za minutu a zaroven se cervena nebo se poti
def detektor_lzi(cervena_se: bool, poti_se: bool, tep: int):
    vezen_lze = (tep > 90) and (cervena_se or poti_se)
    return vezen_lze
