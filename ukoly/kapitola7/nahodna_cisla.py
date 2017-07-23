import random

# Zeptej se uzivatele: "Kolik nahodnych cisel chces vygenerovat? "
# Vygeneruj mu nahodna cisla v rozmezi od -100 do 100 pomoci funkce randint

pocet_cisel = int(input("Kolik nahodnych cisel chces vygenerovat? "))
for i in range(pocet_cisel):
    print(random.randint(-100, 100))
