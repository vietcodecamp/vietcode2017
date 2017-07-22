# V poli fronta mas ulozenou frontu veznu, kteri jdou postupne na gilotinu (ten uplne nalevo je 1.)
# Pridej do fronty jeste BFU a ABFU pomoci funkce append
def pole_append():
    fronta = ["Zlodej Petr", "Pedofil Honza", "Vrah David", "Dacos", "Roman"]
    fronta.append("BFU")
    fronta.append("ABFU")
    return fronta


# Nakonec jsme se rozhodli seradit vezne podle jmena. Pouzij na to funkci sort
def pole_sort():
    fronta = ["Zlodej Petr", "Pedofil Honza", "Vrah David", "Dacos", "Roman", "BFU", "ABFU"]
    fronta.sort()
    return fronta


# A to nejlepsi nakonec. Zbavime se ABFU a BFU pomoci remove. Pouzij index misto prime hodnoty
def pole_remove_index():
    fronta = ["ABFU", "BFU", "Dacos", "Pedofil Honza", "Roman", "Vrah David", "Zlodej Petr"]
    fronta.remove(fronta[0])
    fronta.remove(fronta[0])
    return fronta


# Zlodej Petr je nevinny. Odeber posledniho pomoci funkce pop
def pole_pop():
    fronta = ["Dacos", "Pedofil Honza", "Roman", "Vrah David", "Zlodej Petr"]
    fronta.pop()
    return fronta


# Dacos a Roman jsou jako vzdy take nevinni.
# Kdybyste je poslali na gilotinu, tak vas samozrejme uz dal nikdo ucit Python nebude,
# takze je taky odeberte z fronty pomoci funkce remove. Pouzij primo hodnoty nikoliv index.
def pole_remove():
    fronta = ["Dacos", "Pedofil Honza", "Roman", "Vrah David"]
    fronta.remove("Dacos")
    fronta.remove("Roman")
    return fronta
