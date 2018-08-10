# Exercises - Finished

## Warm-up
* Given an array of numbers `cisla = [4.5, 1.5, 1.2, 8.9, 2.3]` calculate the **sum** of the numbers
  * Note: without using `sum()`
  * Hints: calculate the sum using a for loop and save the result to a variable

```python
cisla = [ 4.5, 1.5, 1.2, 8.9, 2.3]
soucet = 0
for cislo in cisla:
  soucet += cislo

print("Součet čísel je: " + soucet))
```


* Improve the above code so that it also prints the **average** of the numbers

```python
cisla = [ 4.5, 1.5, 1.2, 8.9, 2.3]
soucet = 0
for cislo in cisla:
  soucet += cislo

prumer = soucet / len(cisla)
print("Součet čísel je: " + soucet)
print("Průměr čísel je: " + prumer)
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
    print(str(poradi) + ". " + jidlo)
    poradi = poradi + 1

# Použití enumerated
for (index, prvek) in enumerate(jidla):
    print(str(index + 1) + ". " + prvek)
```

## Input in for loop
* Get 5 favourite foods from a user using a loop
 * Hint: `for i in range(5):`, `jidla.append(input("Zadejte jídlo: "))`, `', '.join(jidla)`,

```python
jidla = []
for i in range(1, 6):
  jidla.append(input("Zadej tvoje " + str(i) + ". nejoblíbenější jídlo: "))

print("Tvoje nejoblíbenější jídla jsou: " + ', '.join(jidla))  
```
## Average from input
* Calculate the average shoe size in your class. First ask for the number of students, then get all of their sizes. Then sum and divide them to get the average

```python
soucet_velikosti_bot = 0
pocet_studentu = int(input("Zadej počet studentů: "))
for i in range(pocet_studentu):
  soucet_velikosti_bot += float(input("Zadej velikost bot {}. studenta: ".format(i + 1)))

prumer = soucet_velikosti_bot / pocet_studentu
print("Průměrná velikost bot je " + str(prumer))  
```

## Class division
* Lets say we a class students stored in a list `trida = ["Kevin", "Honza", "Radek", "Tue", "Adéla", "Vojta"]` and we need to divide the class into two halves. We want to have every odd member in one list and every even member in a second list. The result should look like this: `trida_a = ["Honza", "Tue", "Vojta"]` and `trida_b = ["Kevin", "Radek", "Adéla"]`

```python
trida = ["Kevin", "Honza", "Radek", "Tue", "Adéla", "Vojta"]
trida_a = []
trida_b = []

for index in range(len(trida)):
  kemper = trida[index]
  if index % 2 == 0: # if index is even
    trida_b.append(kemper)
  else:
    trida_a.append(kemper)  

print(trida_a)
print(trida_b)
```
