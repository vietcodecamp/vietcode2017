# Ziskejte od uzivatele pocet bodu od 0 do 100
# pokud je pocet bodu mezi 0 a 50, tak vypiste "F"
# pokud je pociet bodu mezu 50 a 60, vypiste E
# pro zbyle znamky plati nasledujici intervaly
# 60 - 70 D
# 70 - 80 C
# 80 - 90 B
# 90 - 100 A


def preved_znamky():
    body = int(input("Zadej pocet bodu: "))
    if (body < 0) or (body > 100):
        print("Neplatny pocet bodu!")
        return
    if (body >= 0) and (body < 50):
        print("F")
        return
    if (body >= 50) and (body < 60):
        print("E")
        return
    if (body >= 60) and (body < 70):
        print("D")
        return
    if (body >= 70) and (body < 80):
        print("C")
        return
    if (body >= 80) and (body < 90):
        print("B")
        return
    if (body >= 90) and (body <= 100):
        print("A")
        return
