# Exercises - Finished

## Input length
* Write a script that reads the input of a user and tells him how many characters he wrote
```python
vstup = input("Napiš text ")
pocet_znaku = len(vstup)
odpoved = "Napsal jsi" + str(pocet_znaku) +  "znaků!"
print(odpoved)
```

## Saving inputs into a list
* Write a script that asks for 3 names, saves them to a list and prints it
```python
jmena = [] # empty list
jmena.append(input("Napiš první jméno: "))
jmena.append(input("Napiš druhé jméno: "))
jmena.append(input("Napiš třetí jméno: "))

print(jmena[0] + ", " + jmena[1] + " a " + jmena[2] + " se potkali v hospodě a dali si pivo.")
```

## READING exercise
```python
x = "kaktus klobasa kolovratek krab"
```
* What is `x[3]`?
* What is `x[6]`?
* What is `x[5:8]`?
```python
print(x[3]) # 't'
print(x[6]) # ' '
print(x[5:8]) # 's k'
```

## Fighting a dragon
* Create a list called 'inventory' for your knight that includes "sword", "puppy", "ice cream", "fancy hat" and 2 more items of your choice.
* Find the right indexes to get the right item to fight the dragon and save the princess, make a good impression on the princess to fall in love with you and give her a wedding gift.
```python
inventar = ["meč", "štěňátko", "velkým bicepsem"]
print("Zdolal jsem draka a přitom použil" + inventar[0])
print("Udělám dojem mým " + inventar[2])
print("Daruji jí " + inventar[1])
```

## Upper Case
* Write a script that yells back at you whatever you tell it. You will use `upper()`. You can put some bad word to the end, but don't tell anyone.
```python
vstup = input("Co delas ")
odpoved = vstup.upper() + "!!!"
print(odpoved)
```

## X-mass tree
* Draw a x-mass tree. Use a single print function and a string concatenation (joining) method
  * Note, we will improve this using loops later on
It should look like this:

```
   *
  ***
 *****
*******
   *
   *
```
```python
prostredni_hvezda = "   *\n"
print(prostredni_hvezda + "  ***\n" + " *****\n" + "*******\n" + prostredni_hvezda + prostredni_hvezda)
```

## Rectangle
* Draw a 4 x 4 empty rectangle using string concatenation and \n
  * Note, we will also improve this using loops later on

```python
****
*  *
*  *
****
```
```python
radek = "****"
sloupec = "*  *"
vysledek = radek + "\n" + sloupec + "\n" + sloupec + "\n" + radek
print(vysledek)
```
