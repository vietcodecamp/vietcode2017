# Exercises - Finished

## Reading exercise
* What will happen? Try to guess before running it in the python shell

```python
(5 > 4) and (3 == 5) # False
not (5 > 4) # False
(5 > 4) or (3 == 5) # True
not ((5 > 4) or (3 == 5)) # False
(True and True) and (True == False) # False
(not False) or (not True) # True
```
## Upgrade your scripts from the first and second lesson.
* For the age calculator, test if their age is over 65 and output something different

```python
vek = int(input("Kolik je ti let? "))
let_do_duchodu = 65 - vek

if let_do_duchodu > 0 :
  odpoved = "Zbyva ti " + str(let_do_duchodu) + " let do duchodu!"
else:  
  odpoved = "Už jsi v důchodu " + str(-let_do_duchodu) + " let"
print(odpoved)
```

* For the BMI calculator, do a quick check if people used meters instead of centimeters (the height should be over 100cm, for example)

```python
vaha = float(input("Kolik vážíš? (v kg)"))
vyska = float(input("Kolik měříš? (v metrech nebo centimetrech)"))

if vyska > 100:
  vyska = vyska/100 # převod na metry

bmi = vaha / vyska ** 2
print("Tvé BMI je " + str(bmi))
```

## Mini scripts
* Make a script that takes 2 numbers and says which one is bigger (note, don't just print the number, tell which one is larger! I.e. the first or the second)

```python
prvni_cislo =  int(input("Číslo 1: "))
druhe_cislo =  int(input("Číslo 2: "))

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
  print("Absolutní hodnota čísla " + str(cislo) + " je " +  str(-cislo))
else:
  print("Absolutní hodnota čísla " + str(cislo) + " je " +  str(cislo))
```

## University grading
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

## Blood pressure
* Tell if a user has high blood pressure. A user has high blood pressure if his systolic pressusure is more than 120 or diastolic pressure is higher than 80. The script should ask the users for both values and respond whether he has high blood pressure or not

```python
systolicky_tlak = int(input("Zadej systolický tlak:"))
diastolicky_tlak = int(input("Zadej diastolický tlak:"))
if (systolicky_tlak > 120) or (diastolicky_tlak > 80):
    print("Vysoký tlak")
else:
    print("Nízký tlak")

```

## Calculator
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

print(prvni_cislo, operace, druhe_cislo, " = ", vysledek)
```

## Simple ATM
Implement a simple ATM.
1. let the user put to the input his card number, PIN and the amount of money to withdraw.
2. If the card number is not 43-1199223344, say "Invalid card number!"
3. if the card number is correct, proceed to check the PIN. If the PIN is not 3194, say "Invalid PIN!"
4. if both card number and PIN are correct, check if it's possible to withdraw the requested amount of money from his banking account with the balance 1000 CZK.
5. If it's possible, print to the output "You have withdrawn [amount] CZK and your new balance is [balance] CZK.", otherwise print "Not enough money in the bank account!"

```python
VALIDNI_CISLO_KARTY = "43-1199223344"
VALIDNI_PIN = 3194

ucetni_zustatek = 1000

cislo_karty = input("Zadejte číslo karty: ")
if cislo_karty != VALIDNI_CISLO_KARTY:
    print("Neznámé číslo karty!")
    exit(1)
pin = input("Zadejte PIN: ")
if pin != VALIDNI_PIN:
    print("Špatný PIN!")
    exit(1)
vyber = int(input("Zadejte výši výběru v Kč: "))
if vyber > ucetni_zustatek:
    print("Nemáte dostatek peněz na účtě!")
    exit(1)

ucetni_zustatek = ucetni_zustatek - vyber
print("Vybrali jste " + str(vyber) + " Kč a účetní zůstatek je " + str(ucetni_zustatek) + " Kč.")
```
