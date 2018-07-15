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

*"When you brush your teeth, you don't stop after, say, 200 strokes right? (Or at least most of us don't). You stop when you feel the teeth are clean. It can be after 100 strokes, or it can be after 400 strokes (e.g. when you go out for a date with your crush ;) "*


Now let's go more programatic:

*Imagine a robot, which brushes the teeth for you. He has a single command `BRUSH-ONCE`. If you programmed him to use while-loop, he would do the following:*
  1. *He checks, if your teeth still dirty*
  2. *If they are, he executes the command BRUSH-ONCE and returns to point 1.*
  3. *If they are not dirty anymore, his job is done and he shuts down. (exiting the loop)*

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



*Imagine you have a company, that sells a wood chopping robots. They work this way:*

```
while the pile of wood logs is not empty
  1. take a log from a pile
  2. place it on the cutting surface
  3. chop
```
*One day, a customer calls you, that the robot injured one of his employees and demands you include some safety-measure inside your robot. So you re-program him and he does:*

```
while the pile of wood logs is not empty
   1. take a log from a pile
   2. place it on the cutting surface
   3. if human is nearby
         -> break job
   4. if clear, then chop
```

*You see, that the break is mostly used when the round if iteration should not be completed and the loop must be exited immediately. The use of `break` in programs is the same as in this "real-world" example - as a safety measure.*

**Example:** Write a program that takes coefficient of a quadratic equation ax<sup>2</sup> + bx + c = 0 and computes the solution. Stop the program when the quadratic coefficient `a` is zero.


```python
print('This script calculates the solutions of a quadratic equation in form ax^2 + bx + c = 0')

while True:
    a = input('Enter the coefficient a')

    if a == 0:
        print('The coefficient a equals to 0.\n The program will terminate.')
        break # After this command, the loop will be exited from. The commands after this while loop will be executed
        print('This will NEVER be executed.')

    b = input('Enter the coefficient b')
    c = input('Enter the coefficient c')

    dicriminant = b**2 - 4*a*c
    sqrt_discriminant = dicriminant ** (1/2)

    x1 = (-b + sqrt_discriminant)/(2*a)
    x2 = (-b - sqrt_discriminant)/(2*a)

    print('The solution of the quadratic equation is x1=' + str(x1) + ', x2=' + str(x2))

print('The script terminated.')

```

# Skipping the some code in a loop
* **Problem:** Sometimes you want to skip some code inside the loop but not exit the loop. 
* **Solution:** Use `continue` to skip the code after continue and start a new iteration.

*The use of the continue can be shown on a tax administration office worker. People approach with their tax forms and the official processes them. He/she does the job this way:*

```
While there are people waiting in a queue, do:
   1. ask them to hand in the form and their ID
   2. check if the form is valid 
   3. if not, skip that person by calling "Next!" (or if she/he was a computer by calling "Continue!")
   4. process the form if it is valid
```

**Example:** Modify the previous program to warn the user when the discriminant is negative

```python
print('This script calculates the solutions of a quadratic equation in form ax^2 + bx + c = 0')
while True:
    a = input('Enter the coefficient a')

    if a == 0:
        print('The coefficient a equals to 0.\n The program will terminate.')
        break # After this command, the loop will be exited from. The commands after this while loop will be executed.
        print('This will NEVER be executed.')


    b = input('Enter the coefficient b')
    c = input('Enter the coefficient c')

    dicriminant = b ** 2 - 4*a*c

    if dicriminant < 0:
        print('The discriminant is negative. There is no real number solution.')
        continue # After this command, the loop will be exited from. The commands after this while loop will be executed.

    sqrt_discriminant = dicriminant ** (1/2)

    print('If the discriminant is negative, this will not get printed.')
    x1 = (-b + sqrt_discriminant)/(2*a)
    x2 = (-b - sqrt_discriminant)/(2*a)

    print('The solution of the quadratic equation is x1=' + str(x1) + ', x2=' + str(x2))

print('The script terminated.')

```

* `break` and `continue` seem to do the same thing. But imagine this - what would happen, if you you replaced `break` with `continue` in the previous log-chopping-robot example?
This the crucial difference between those two commands

* `break` and `continue` can also be used in `for` loops.

**Summary:** `break` exits the most inner loop and `continue` just skips the code after and a new iteration begins (if there is one).


# While vs for loops
* What does a for loop mean? "Do something for every item in the list", "Do something 5 times"
* What if we want to do something as long as a condition is true? For that, we employ while loops.
* They are very similar (in fact, you can often transform for loops into while loops and vice versa and it is often debated as a matter of style)
* The main difference is in meaning of the loop. `for` loop is used generally when we know how many times we do the cycle. `while` loop is usually used if you don't know for sure how many times you should repeat the code (see the coin flip example above).

# Exercises
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
print("Průměrná velikost bot je " + prumer
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
