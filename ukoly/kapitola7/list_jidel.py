# Vytvor seznam svych oblibenych jidel.
# Vypis pro napr. jidla["bun cha", "knedlo vepro zelo", "pho", "gulas"]
# Seznam mych oblibenych jidel:
# 1. bun cha
# 2. knedlo vepro zelo
# 3. pho
# 4. gulas

jidla = ["bun cha", "knedlo vepro zelo", "pho", "gulas"]  # Uloz do pole svoje oblibena jidla podle tvych priorit.

i = 1
for prvek in jidla:
    print(str(i) + ". " + prvek)
    i = i + 1

