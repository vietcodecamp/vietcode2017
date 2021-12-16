# Exercises - Start
## Retirement
* Write a program that receives your age and tells you **how many years** you have left **before you retire**. (The age of retirement should be **65**.
You will only need `input()`, `print()`, `int()`, `str()` and `float()` for casting

```python
vek = # 1. Použij input, abys zjistil věk. nezapomeň věk přetypovat na int !
let_do_duchodu = # 2. zde vypočítej kolik zbývá let do důchodu( 65 let v ČR)
odpoved = # 3. zde napiš nějakou odpověď a použij v ní proměnnou let_do_důchodu (nezapomeň jí přetypovat na str()!)
print(odpoved)
```

## Body Mass Index
* Write a program asks you for your **weight and height** and calculates your **BMI**. The BMI is calculated as weight / height <sup>2</sup>. The units should be kg and meters.
You will only need `input()`, `print()`, and `float()` for casting

```python
vaha = # 1. z input() vzít hodnotu a tu pak přetypovat na float()
vyska = # 2. z input() vzít hodnotu a tu pak přetypovat na float()
bmi = # 3. Použij vzorec BMI
# 4. Vytiskni odpověď
```
## Circle
* Write a program that receives a **radius** of a circle and calculates its circumference, area and volume of a sphere. You will only need `input()`, `print()`, `str()` and `float()` for casting.
Hints:
  - Use a variable `PI` and set it to `3.14` instead of using 3.14 every time.
  - Volume of a sphere can be calculated as V = 4/3 * π * r<sup>3</sup>

```python
PI = 3.14 # definování konstanty - proměnná, která se nemění
# 1. získat poloměr od uživatele.

# 2. Vypočítat obvod kruhu

# 3. Vypočítat obsah kruhu

# 4. Vypočítat objem koule

# 5. Vytisknutí všech hodnot.

```

## Minutes to hours and minutes
* Write a program that receives a number representing **minutes**. The goal is to convert minutes into **hours and minutes**. You will need `input()`, `print()`, `str()` and `int()` for casting. You will further need these operators: integer division (`//`) and modulo (`%`) (modulo calculates the reminder after division, eg. `5%3 = 2` - the remainder after dividing `5` by `3` is `2`)

```python
# 0. definování konstanty počtu minut v hodině - není nutné, ale je to lepší. Kód je čitelnější
POCET_MINUT_V_HODINE = 60

# 1. vypočítat počet hodin z minut (Hint: použít celočíselné dělení `//`)
# 2. vypočítat počet počet zbylých minut (Hint: zbytek po dělení - modulo `%`)
# 3. Tisk vypočtených proměnných
```
