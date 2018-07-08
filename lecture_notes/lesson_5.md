# Lesson 5
* While loops, control flow, transforming between while and for

# While vs for loops
* What does a for loop mean? "Do something for every item in the list", "Do something 5 times"
* What if we want to do something as long as a condition is true? For that, we employ while loops.
* They are very similar (in fact, you can often transform for loops into while loops and vice versa and it is often debated as a matter of style)

```Python
x = 0
while x < 3:
    print(x)
    x = x + 1
```

# INFINITY
* You can easily run forever with a while loop
```Python
while True:
    # do stuff
```


# break, continue
* Now we are in a loop (doesn't matter whether it is a while or for loop) and we want to exit it due to some (un)expected circumstance. We can skip the current iteration using continue (the loop continues) or stop it completely using break (the loop ends)

# Exercises
## Average from input
* Předtím jsme vytvořili skript, který se uživatele zeptá na počet lidí a pak ve for smyčce získá hodnoty. Změňte for smyčku za while smyčku s tím, že bude skript sbírat data dokud nebude na vstupu "STOP". Po zadání stop se spočítá průměr jako předtím.

```python
soucet_velikosti_bot = 0
pocet_student = 0
while true
    vstup = input("Zadej velikost bot nebo \"STOP\" pro spočítání průměru: ")
    if vstup == "STOP":
        break
    else:
        soucet_velikosti_bot += float(vstup))
        pocet_studentu += 1
prumer = soucet_velikosti_bot / pocet_studentu
print("Průměrná velikost bot je {}".format(prumer))  
```

# Extra
* This lesson would be suitable for a programmer interview task (ideally coded by the lecturers). Most programmer inteviews are on data structures such as trees and maps which are covered during the first semester at University. These questions are from actual interviews. Sadly, the more interesting ones involve objects.
* A programmer interview has 1 to 3 tasks. You solve the task while commenting on it. Afterwards, you discuss the time complexity with your interviewer. Finally, you can ask the interviewer questions about the company. The whole process takes roughly an hour.

## Anagramy
* Napis metodu, co zjisti, jestli jsou dva retezce anagramy nebo ne.

## Unikat
* Napis metodu, co zjisti, jestli se v retezci nevyskytuje nejaky znak dvakrat. BONUS: bez pouziti datove struktury.

## prefix tree (my interview!! Dacos challenge)
* Napiste datovou strukturu reprezentujici prefixovy strom. (taky trie)
* Prefixovy strom uklada retezec s pomoci uzlu. V kazdem uzlu je jeden znak (prefix) a reference na zbytek slova. Konec nejakeho slova zjistite flagem true.
```
ahoj ->

start -> a -> h -> o -> j
```
* V prefixovem slove tak muzete mit vic slov
```
start -> a -> h -> o -> j(stop) -> k -> y
      \        \
       \        > a (stop)
        > h - > e - > j
```
* Diskutujte proc to je vyhodne a co se s tim da delat
