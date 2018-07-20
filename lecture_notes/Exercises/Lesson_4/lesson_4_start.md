# Exercises - Start

## Warm-up
* Given an array of numbers `cisla = [4.5, 1.5, 1.2, 8.9, 2.3]` calculate the **sum** of the numbers
  * Note: without using `sum()`
  * Hints: calculate the sum using a for loop and save partial results into a variable

```python
cisla = [ 4.5, 1.5, 1.2, 8.9, 2.3]
soucet = 0
for cislo in cisla:
    # 1. přičti číslo k proměnné soucet. Nezapomenout na odsazení zleva!
    soucet += 0

# 2. vytiskni odpověď
```

* Improve the above code so that it also prints the **average** of the numbers

```python
cisla = [4.5, 1.5, 1.2, 8.9, 2.3]
soucet = 0
for cislo in cisla:
    # přičti číslo k proměnné soucet. Nezapomenout na odsazení zleva!
    soucet += 0

# 2. vypočítej průměr

# 3. vytiskni součet a průměr čísel

```  

## Food list
* Create a list of your favorite foods, for example: `jidla = ["bun cha", "knedlo vepro zelo", "pho", "gulas"]`
* print the list of foods in the following format:

```
1. bun cha
2. knedlo vepro zelo
3. pho
4. gulas
```

```python
jidla = ["bun cha", "knedlo vepro zelo", "pho", "gulas"]  # Uloz do pole svoje oblibena jidla podle tvych priorit.

#
poradi = 1
for jidlo in jidla:
    #  1. Vytiskni pořadí a jídlo
    print()
    # 2. Zvyš pořadí o 1

```

## Input in for loop
* Get 5 favourite foods from a user using a loop
 * Hint: `for i in range(5):` to make the loop run 5 times, `jidla.append(input("Zadejte jídlo: "))`, `', '.join(jidla)`,

```python
jidla = []
for i in range(5):
    # 1. získej hodnotu jídla od uživatele a připoj ho do listu jidla
    input()

# 2. Vytiskni odpověď  - pro tisk všechno hodnot v listu jidla použij: ', '.join(jidla)

```
## Average from input
* Calculate the average shoe size in your class. First ask for the number of students, then get all of their sizes. Then sum and divide them to get the average

```python
soucet_velikosti_bot = 0
# 1. Získej počet studentů

# 2. proveď smyčku přes počet studentů
  # 3. přičti velikosti bot - odsazení je tu schválně, aby se na to nezapomnělo.

# 4. Vypočítej průměr velikosti bot

# 5. Vytiskni odpověď
```
