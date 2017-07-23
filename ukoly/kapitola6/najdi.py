# doplnte funkci najdi, ktera bere dva vstupy;
# prvni je seznam, druhy je hodnota, kterou v nem hledame
# pokud hodnota v seznamu je, vytisknete "hodnota nalezena"
# pokud tam neni, vytisknete "hodnota nenalezena"

def najdi(seznam :list, hodnota):
    if hodnota in seznam:
        print("hodnota nalezena")
    else:
        print("hodnota nenalezena")
