# napiste cast programu pro simulaci veznova dilematu
# dostane rozhodnuti od dvou hracu, bud "zradil", nebo "mlcel"
# pokud se oba hraci vzajemne zradili, vypiste "oba prohrali"
# pokud oba mlceli, vypiste "oba se dostali z basy"
# jinak vypiste ktery hrac byl zrazen, tedy bud "hrac1", nebo "hrac2"
def rozhodni(hrac1, hrac2):
    zradil = "zradil"
    mlcel = "mlcel"
    if (hrac1 == mlcel and hrac2 == mlcel):
        print("oba se dostali z basy")
        return
    if (hrac1 == zradil and hrac2 == zradil):
        print("oba prohrali")
        return
    if (hrac1 == zradil and hrac2 == mlcel):
        print("hrac2")
        return
    if (hrac1 == mlcel and hrac2 == zradil):
        print("hrac1")
        return
