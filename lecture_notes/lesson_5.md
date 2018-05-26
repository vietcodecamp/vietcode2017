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
* Predtim jsme vytvorili skript, co se uzivatele zepta na pocet lidi a pak ve for loopu ziska hodnoty. Zmente to na while loop s tim, ze bude skript sbirat data dokud nereknete "STOP", pak spocita prumer jako predtim

```python
soucet_velikosti_bot = 0
pocet_student = 0
While true
    vstup = input("Zadej velikost bot nebo \"STOP\": ")
    if vstup == "STOP":
        break
    else:
        soucet_velikosti_bot += float(vstup))
        pocet_studentu += 1
prumer = soucet_velikosti_bot / pocet_studentu
print("Průměrná velikost bot je {}".format(prumer))  
```

