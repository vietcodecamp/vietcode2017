# Exercises - Finished

## Average from input
* Předtím jsme vytvořili skript, který se uživatele zeptá na počet lidí a pak ve for smyčce získá hodnoty. Změňte for smyčku za `while` smyčku s tím, že bude skript sbírat data dokud nebude na vstupu `"STOP"`. Po zadání stop se spočítá průměr jako předtím.

```python
soucet_velikosti_bot = 0
pocet_student = 0
while True:
    vstup = input("Zadej velikost bot nebo \"STOP\" pro spočítání průměru: ")
    if vstup == "STOP":
        break
    else:
        soucet_velikosti_bot += float(vstup))
        pocet_studentu += 1
prumer = soucet_velikosti_bot / pocet_studentu
print("Průměrná velikost bot je " + str(prumer))
```

## Dacos casino
In 10 years, Dacos realizes teaching students programming is not profitable so he decides to open a casino instead.
There will a game, in which you play dices against Dacos himself. The rules are simple.

*Each of you rolls 3 dices and the greater sum wins (you can also extend the rules by adding bonuses for same-number combos).*
*A buy-in for each round is 10CZK. You take all your savings (100CZK) and face the owner with one goal - you either leave the casino with double of your savings, or with no money left*
*Run your script several times. Did you rip Dacos off, or did he rip you? How many rounds did you have to play?*

# Extra
* This lesson would be suitable for a programmer interview task (ideally coded by the lecturers). Most programmer interviews are on data structures such as trees and maps which are covered during the first semester at University. These questions are from actual interviews. Sadly, the more interesting ones involve objects.
* A programmer interview has 1 to 3 tasks. You solve the task while commenting on it. Afterwards, you discuss the time complexity with your interviewer. Finally, you can ask the interviewer questions about the company. The whole process takes roughly an hour.

## Anagrams
* Write a script, which tells, whether two words are "anagrams", or not. Two words are anagrams, if one word can be obtained by re-arranging letters of the other. The famous anagrams are `"Nomen" -"Omen"` 

## Unique
* Write a script, which tells, whether there is any letter in the given word present more, than once

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
