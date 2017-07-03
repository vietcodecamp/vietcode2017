# Vytvor seznam svych oblibenych jidel

jidla =         # prirad prazdny list k promenne oblibenych jidel
while True:
    print('Zadej svoje oblinene jidlo cislo ' + str(len(jidla) + 1) +
      ' (Or enter nothing to stop.):')
    jidlo = input()
    if jidlo == '':
        break
                      # <-- zde prirad kazde pridane jidlo k seznamu jidel
                      
print('Moje oblibena jidla jsou:')
                # <--- zde vytiskni kazde jidlo ze seznamu na novy radek
