# Lesson 5
**Lesson goal:** After this lesson the learner will be able to use `while` loops and will know when to use `for` loop or `while` loop

# Outline
1. While loop
2. Exiting the while loop
3. Skipping the some code in a loop
4. while vs for loops
5. When to use while loop and when for loop
6. Exercises

# While loop
* **Problem:** With `for` loops we can loop through a `list` or a `range` which implies that the loop will eventually stop after the last element has been iterated through. What if we need something to run in a loop until something happens?
* **Solution:** We use a `while` loop. While loop repeats itself when a condition is `True`.
When the condition is `False` in time of checking (the beginning of every iteration), the code inside of the loop will not be executed.

**Example:**
```python
from random import random
# Flip a coin until it is not heads
is_heads = True
while is_heads:
  is_heads = random() > 0.5 # random() returns a random number between 0.0 and 1.0

```

# Exiting the while loop
* One of the obvious way is to set the condition to `False` inside the loop so that the next iteration will not happen. But consider the following problem.
* **Problem:** Sometimes you need to decide inside the loop whether to continue in the loop or not.

* **Solution:** We can use a `break` statement to exit the loop.

```python

while 1 < 2:
  ... # do something here

  if condition_is_true:
    break # Exit this loop
  ... # the rest of the code
  print("If the condition_is_true is True, this will NOT be printed.")

print("This will be printed after the loop finishes.")
```

# Skipping the some code in a loop
* **Problem:** Sometimes you want to skip some code inside the loop but not exit the loop. For example.
* **Solution:** Use `continue` to skip the code after continue and start a new iteration.

```python
while some_condition:
  ... # do something here
  if something_bad_happens:
    continue

  ... # if continue is called this code will be skipped

```

* `break` and `continue` can also be used in `for` loops. Summary: `break` exits the most inner loop and `continue` just skips the code after and a new iteration begins (if there is one).


# While vs for loops
* What does a for loop mean? "Do something for every item in the list", "Do something 5 times"
* What if we want to do something as long as a condition is true? For that, we employ while loops.
* They are very similar (in fact, you can often transform for loops into while loops and vice versa and it is often debated as a matter of style)
* The main difference is in meaning of the loop. `for` loop is used generally when we know how many times we do the cycle. `while` loop is usually used if you don't know for sure how many times you should repeat the code (see the coin flip example above).

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
