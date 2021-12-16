
# Exercises - Finished
## Retirement
* Write a program that receives your age and tells you **how many years** you have left **before you retire**. (The age of retirement should be **65**).
You will only need `input()`, `print()` to interact with the user and `int()`, `str()` for casting (i.e getting numbers from characters and vice versa)

```python
# expected output at this point
# explain how to divide the program into steps
vek = input("Kolik je ti let? ")
let_do_duchodu = 65 - int(vek)
odpoved = "Zbyva ti " + str(let_do_duchodu) + " let do duchodu!"
print(odpoved)
```

## Body Mass Index
* Write a program asks you for your **weight and height** and calculates your **BMI**. Lookup the BMI formula on wikipedia. Use meters instead of centimeters
You will only need `input()`, `print()`, and `float()` for casting

```python
# expected output at this point
# explain how to divide the program into steps
vaha = float(input("Kolik vazis? (v kg)"))
vyska = float(input("Kolik meris? (v metrech)"))
bmi = vaha / vyska ** 2
print("Tvé BMI je " + str(bmi))
```
## Circle
* Write a program that receives a **radius** of a circle and calculates its circumference, area and volume of a sphere. You will only need `input()`, `print()`, `str()` and `float()` for casting.
Hints:
  - Use a variable `PI` and set it to `3.14` instead of using 3.14 every time.
  - Volume of a sphere can be calculated as V = 4/3 * π * r<sup>3</sup>

```python
PI = 3.14 # definování konstanty - proměnná, která se nemění
polomer = float(input("Zadejte poloměr: "))
obvod = 2 * PI * polomer
obsah = PI * polomer ** 2 # ** je mocnina, polomer ** 2 znamená polomer na druhou
objem = 4 / 3 * PI * polomer ** 3
print("Obvod kružnice o poloměru " + str(polomer) + " je " + str(obvod))
print("Obsah kruhu o poloměru " + str(polomer) + " je " + str(obsah))
print("Objem koule o poloměru " + str(polomer) + " je " + str(objem))
```

## Minutes to hours and minutes
* Write a program that receives a number representing **minutes**. The goal is to convert minutes into **hours and minutes**. You will need `input()`, `print()`, `str()` and `int()` for casting. You will further need these operators: integer division (`//`) and modulo (`%`) (modulo calculates the reminder after division, eg. `5%3 = 2` - the remainder after dividing `5` by `3` is `2`)

```python
POCET_MINUT_V_HODINE = 60 # definování konstanty - proměnná, která se nemění

minuty = int(input("Zadejte počet minut: "))
pocet_hodin = minuty // POCET_MINUT_V_HODINE # celočíselné dělení
pocet_minut = minuty % POCET_MINUT_V_HODINE # zbytek po dělení

print(minuty + " minut = " + str(pocet_hodin) + " hodin a " + str(pocet_minut) + " minut")
```
