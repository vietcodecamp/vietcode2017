# Exercises - Start

## Reading exercise
* What will happen? Try to guess before running it in the python shell

```python
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
```
## Upgrade your scripts from the first and second lesson.
* For the age calculator, test if their age is over 65 and output something different

```python
vek = int(input("Kolik je ti let? "))

# Poznámka. V if a else nezapomeňte na odsazení! Buď tab nebo 2 mezery od začátku.
if ... :    # 1. doplň podmínku místo teček (podmínka: *let_do_duchodu je 65 a méně*)
    # 2. vypiš kolik let zbývá do důchodu
    let_do_duchodu = 0
else:  
    # 3. v opačném případě vypsat kolik let již v chůdodu je.
    let_v_duchodu = 0
```

* For the BMI calculator, do a quick check if people used meters instead of centimeters (the height should be over 100cm, for example)

```python
vaha = float(input("Kolik vážíš? (v kg)"))
vyska = float(input("Kolik měříš? (v metrech nebo centimetrech)"))

if ... : # 1. doplnit podmínku (podmínka: *pokud je hodnota výšky nad 100*)
    # 2. pokud ano, převeď na metry
    vyska_v_metrech = 0

# 3. výpočet BMI

# 4. Tisk
```

## Mini scripts
* Make a script that takes 2 numbers and says which one is bigger (note, don't just print the number, tell which one is larger! I.e. the first or the second)

```python
prvni_cislo =  int(input("Číslo 1: "))
druhe_cislo =  int(input("Číslo 2: "))

if ...: # 1. první podmínka
  print("První číslo je větší.")
elif ...: # 2. podmínka
  print("Druhé číslo je větší.")
else:
  print("Obě čísla se rovnají")
```
* Make a script that takes a numeric input and gives you it's absolute value (if x is -5, it prints 5)


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
if ... : # 1. přidat podmínku pro nesprávný počet bodů
  print("Nesprávný počet bodů, zadejte body v rozmezí <0, 100>")
  body =  int(input("Počet bodů: "))

# 2. pro každý případ udělat podmínku
if ...:
  print("A")
elif ...:
  print("B")
elif ...:
  print("C")
elif ...:
  print("D")
elif ...:
  print("D")
else:
  print("F")  
```

## Blood pressure
* Tell if a user has high blood pressure. A user has high blood pressure if his systolic pressusure is more than 120 or diastolic pressure is higher than 80. The script should ask the users for both values and respond whether he has high blood pressure or not

## Calculator
* Create a calculator! A script that asks you for 2 numbers, then asks you whether you want to add, subtract, multiply or divide them. Use if for the response and do the operation

```python
prvni_cislo =  int(input("cislo 1: "))
druhe_cislo =  int(input("cislo 2: "))
operace = input("Jakou operaci chceš použít?\n +, -, * nebo /  ")

# 1. napsat podmínky pro operace

# 2. Tisk výsledku

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

# 1. Nejdřív získej číslo karty od uživatele.

# 2. Ověř jestli je číslo karty validní (je rovno VALID_CARD_NUMBER). Pokud ne, ukonči program - exit(1)

# 3. Zeptej se na PIN uživatele

# 4. Ověř jestli je PIN validní. Pokud ne, ukonči program - exit(1)

# 5. Zeptej se, kolik chce vybrat

# 6. Pokud je účetní zůstatek menší než požadovaná částka, ukonči program, jinak peníze vydej (odečíst peníze z účtu)

# 7. Vytiskni odpověď s informací o tom, kolik vybral, a kolik mu zbývá peněz na účtě.

```
