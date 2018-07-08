# Lesson 3
* Conditionals if, not
* Boolean algebra intro
* Nested conditions
* Indentation, function scope (VERY HARD)
* For any kind of logic or control flow, we need conditional statements.

## Booleans
* For conditionals, we work with the boolean data type, which is either `True` or `False`
* Note a boolean is a data type we can assign to a variable!
* We create a boolean using comparison operators
```python
# Basic comparison operators
x = 3 # This is not equal! This is a declaration!
x > 3 # False
x >= 3 # True
x < 5  # True
x <= 2  # False
x == 3  # is x equal to three? Yes!
x != 4  # is x not equal to 4? Yes!
y = x != 4  # Evaluate x is not equal to 4, save the result to y
```

## Conditionals
* The basic conditional is `if <expression>`:
* If the logical expression is true, the if will run the indented commands. Otherwise nothing will happen
* We also have else. If the condition in the if evaluates to False, the else branch gets run. Either the code in the if section runs, or the code in the else section runs. Never both!
```python
x = 4
if x == 4:
    print("this should be printed out)
print("This should also be printed out")
```
```python
x = 3
y = 5
if x == 4:
    print("this should NOT be printed out)
elif y == 5:
    print("this should be printed out)
else:
    print("This should NOT be printed out")
print("This should be printed out again")
```
```python
x = 4
if x == 4:
    print("this should be printed out)
else:
    print("This should NOT be printed out")
print("This should be printed out again")
```

## Boolean algebra
* To combine conditions, we can use `and` and `or` operators
* To invert a truth value use `not`
* **NOTE** make truth value tables

## Nested conditions
* For more complex schemes, we can nest if statements in each other.
* It is often better to combine them into **and** statements, sometimes it is not possible

```python
if x > 2:
    if x < 4:
        print("x is between 2 and 4")
# OR
if x > 2 and x < 4:
    print("x is between 2 and 4")

# OR
if 2 < x < 4:
    print("x is between 2 and 4")    
```

## Exercises

### Reading exercise
* What will happen? Try to guess before running it in the python shell

```python
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
```
### Upgrade your scripts from the first and second lesson.
* For the age calculator, test if their age is over 65 and output something different

```python
vek = int(input("Kolik je ti let? "))
let_do_duchodu = 65 - vek
if vek <= 65 :
  odpoved = "Zbyva ti " + str(let_do_duchodu) + " let do duchodu!"
else:  
  odpoved = "Už jsi v důchodu {} let".format(vek - 65)  
print(odpoved)
```

* For the BMI calculator, do a quick check if people used meters instead of centimeters (the height should be over 100cm, for example)

```python
vaha = float(input("Kolik vazis? (v kg)"))
vyska = float(input("Kolik meris? (v metrech)"))
if vyska > 100:
  vyska = vyska/100 # převod na metry

bmi = vaha / vyska ** 2
print("Tvé BMI je " + str(bmi))
```

### Mini scripts
* Make a script that takes 2 numbers and says which one is bigger (note, don't just print the number, tell which one is larger! I.e. the first or the second)

```python
prvni_cislo =  int(input("cislo 1: "))
druhe_cislo =  int(input("cislo 2: "))

if prvni_cislo > druhe_cislo:
  print("První číslo je větší.")
elif prvni_cislo < druhe_cislo:
  print("Druhé číslo je větší.")
else:
  print("Obě čísla se rovnají")
```
* Make a script that takes a numeric input and gives you it's absolute value (if x is -5, it prints 5)

```python
cislo =  int(input("Zadej číslo: "))

if cislo < 0:
  print(f"Absolutní hodnota čísla {cislo} je {-cislo}")
else:
  print(f"Absolutní hodnota čísla {cislo} je {cislo}")"
```

### University grading
* Make a script that takes a number between 0 and 100 (check it!) and returns an university grading

| Points | Grade |
|---|---|
|100 - 90| A |
|89 - 80| B |
|79 - 70| C |
|69 - 60| D |
|59 - 50| E |
|< 50| F |

```python
body =  int(input("Počet bodů: "))
if body < 0 or body > 100 :
  print("Nesprávný počet bodů, zadejte body v rozmezí <0, 100>")
  body =  int(input("Počet bodů: "))

if body <= 100 and body >= 90:
  print("A")
elif body <= 89 and body >= 80:
  print("B")
elif body <= 79 and body >= 70:
  print("C")
elif body <= 69 and body >= 60:
  print("D")
elif body <= 59 and body >= 50:
  print("D")
else:
  print("F")  
```

### Blood pressure
* Tell if a user has high blood pressure. A user has high blood pressure if his systolic pressusure is more than 120 or diastolic pressure is higher than 80. The script should ask the users for both values and respond whether he has high blood pressure or not

```python
systolicky_tlak = int(input("Zadej systolický tlak:"))
diastolicky_tlak = int(input("Zadej diastolický tlak:"))
if (systolicky_tlak > 120) or (diastolicky_tlak > 80):
    print("Vysoký tlak")
else:
    print("Nízký tlak")

```

### Calculator
* Create a calculator! A script that asks you for 2 numbers, then asks you whether you want to add, subtract, multiply or divide them. Use if for the response and do the operation

```python
prvni_cislo =  int(input("cislo 1: "))
druhe_cislo =  int(input("cislo 2: "))
operace = input("Jakou operaci chceš použít?\n +, -, * nebo /  ")
if operace == '+':
  vysledek = prvni_cislo + druhe_cislo
elif operace == '-':
  vysledek = prvni_cislo - druhe_cislo
elif operace == '*':
  vysledek = prvni_cislo * druhe_cislo
elif operace == '/':
  if druhe_cislo == 0:
    print("Nulou nelze dělit!")
    vysledek = 0
  else:  
    vysledek = prvni_cislo / druhe_cislo

print(f"{prvni_cislo} {operace} {druhe_cislo} = {vysledek}")
```

### Simple ATM
* program a simple ATM @Dacos
* let the user input his card number, pin and how much money he wants
* If the card is not 43-1199223344, say "wrong card!"
* if the card is correct, proceed to check the pin. If the pin is not 3194, say "wrong pin!"
* if both card and pin are correct, check if he has enough money on his account (1000,- czk) he can take out
* If he has, say "Ok, paying [number] Kc, otherwise say "not enough money on your account"

# Hackaday #1
* Ifs are a big part of computing, we can show them examples of scripts that make our lives better. If someone has a good suggestion, you can do live coding

# Notes
* People often try to put the results of a function in a if statement
```
if x = input() < 3:
```

Discourage that
* People also tend to insert too many statements into one if
```
if x > 4 and 5:
    <code>
```
Is semantically wrong, because x > 4 gets evaluated to 4 and then you compare True and 5.
