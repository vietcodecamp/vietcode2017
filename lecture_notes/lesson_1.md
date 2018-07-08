# Lesson 1
* We should explain variables properly (especially the = operator), then speed through input and output (skip string formatting for lesson 2)
* Variables, data types, casting, input, output, arithmetic operators
* Ideally we would end with each student having a simple script that gets user input and outputs something


## Motivational example 
### Programming lvl 1: calculator
* You all are familiar with solving quadratic equations. What is the general cookbook for solving them?
Try calculating solution for this simple task (to get hands on Python shell):
 
* now try it for:

* still not tired? Go with this one:

How about calculating all quadratic equations there is? Introducing...

### Programming lvl 2: scripts
* Look at the process of solving the equation. Are there any parts, which you have to type into the calculator every time
you solve an equation? 
* If you guessed the formula for discriminant and the formula for actual solution(s), you were right!
  Those are the *common* part for every solution. We want to write them only once. Imagine solving millins of equations. **Your fingers would fall off!**
* What are however the symbols, that change with every equation? 

  Right, the coefficients of the equation. Now tell me, are those coefficients all we need for solution?
  
  The answers is yes! Those 3 numbers are really what we need to solve any quadratic equation! 
  
  How do we do it? Well as we said before, we write down the common parts:

```python
D = b**2 - 4*a*c 

x1 = (-b + math.sqrt(D)) / (2*a)
x2 = (-b - math.sqrt(D)) / (2*a)
```
* And now, if we substitute for *a*, *b* and *c* to get solutions. Try it for our first example:

```python
a = 5
b = 6
c = 1

D = b**2 - 4*a*c 

x1 = (-b + math.sqrt(D)) / (2*a)
x2 = (-b - math.sqrt(D)) / (2*a)

print(x1)
print(x2)
```
There you go - solving (almost) every quadratic quation there is. No typos, no numeric errors. Oh, how I wish I had this during my math exams....

## Some terms...
### Variables
* In the previous example we used a sign " = " to tell the computer, what  *a*, *b* and *c* are. Notice the word **tell**. The difference of meaning of " = " in programming and in math
is better seen on an example:
* Note that `x = 3` doesn't mean *"x is equal to 3"*, but it means: *"Computer, I order you to take number 3 and save it to the variable x. AND DO IT NOW!!!"* 

  In other words, it's a command, not a statement!
* We can also save strings (words) too: `my_cat_name = "Khajit"`, but most importantly the results of functions: `x = sqrt(y)` Note we have to read the text from right to left: 
 *"Computer, do the square root of whatever is in y and save the result in x. NO TALKING BACK!!"*
* People tend to want to say "this is how the solution should look like" instead of "this is what you should do". In other words - get used to commanding
* Reading code exercise

```python
x = "test" # save the string test to the variable x

y = x # now y has "test"

z = 5
z = z + 5 # Remember to read this from right to left!

x + 4 = 5 # an equation, not usable! Some languages allow formulas, though
```

Pythagoras Example:

```python
# Let ABC be a right-angled triangle with legs 'a', 'b' and hypotenuse 'c'
a = 3 # the length of leg 'a'
b = 4 # the length of leg 'b'
# What is the area of a square created on hypotenuse 'c' ?
area = a * a + b * b
```

## Data types, casting
* *NOTE: specify difference between float and integers*

In Python3 we have integers, float, strings, boolean, objects
* Strings are always between parentheses (We will show how to include parentheses next lesson)
* Some things are automatically castable:

int + float => float

If we add a integer with a float, the result will automatically be a float
```python
1 + 4.0 = 5.0
```
* Some are not:

int + str => error
```python
x = 3 + "ahoj" # error
```
* Some are dangerous

int / int => int

We can cast types to different types using the following functions
`int()`,`float()`, `str()`
```python
x = 3.0 # x is a float
x = int(x) # x is now 3
x = str(x) # x is now "3"
x = x + " kg"   # x is now "3 kg"

y = "5.6" # a string
y = float(y) # y is 5.6
```

## Input and output
* The easiest way to get input from the user is the `input()` function in python3. Note the **data type is a string**.
* Print is a large chapter and might need a separate lesson.
* Mention input sanitization.

```python
x = input() # retrieve string input from user, we can cast this to integers or floats!
print(x) # print takes the parameter x and prints it on the console

# Input takes a optional parameter for a user prompt, improving usability.
# Explain what is a function parameter.
y = input("Zadejte prosim cislo")
```

## Operators
* Basic things such as `+ `, `-`, `/`, `//`, `*`, `**`, `==`, `%`
* What happens when we nest functions together?
* Please mention string concatenation at this point
```python
x = "ahoj"
y = "ky"
z = x + y
print(z) # prints "ahojky"
```

## Exercises
### Retirement
* Write a program that receives your age and tells you **how many years** you have left **before you retire**. (The age of retirement should be **65**.
You will only need `input()`,`print()`,`int()`,`str()` and `float()` for casting

```python
# expected output at this point
# explain how to divide the program into steps
vek = input("Kolik je ti let? ")
let_do_duchodu = 65 - int(vek)
odpoved = "Zbyva ti " + str(let_do_duchodu) + " let do duchodu!"
print(odpoved)
```

### Body Mass Index
* Write a program asks you for your **weight and height** and calculates your **BMI**. Lookup the BMI formula on wikipedia. Use meters instead of centimeters
You will only need `input()`,`print()`, and `float()` for casting

```python
# expected output at this point
# explain how to divide the program into steps
vaha = float(input("Kolik vazis? (v kg)"))
vyska = float(input("Kolik meris? (v metrech)"))
bmi = vaha / vyska ** 2
print("Tvé BMI je " + str(bmi))
```
### Circle
* Write a program that receives a **radius** of a circle and calculates its circumference, area and volume of a sphere. You will only need `input()`,`print()`, `str()` and `float()` for casting.
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

### Minutes to hours and minutes
* Write a program that receives a number representing **minutes**. The goal is to convert minutes into **hours and minutes**. You will need `input()`,`print()`, `str()` and `int()` for casting. You will further need these operators: integer division (`//`) and modulo (`%`) (modulo calculates the reminder after division, eg. `5%3 = 2` - the remainder after dividing `5` by `3` is `2`)

```python
POCET_MINUT_V_HODINE = 60 # definování konstanty - proměnná, která se nemění

minuty = int(input("Zadejte počet minut: "))
pocet_hodin = minuty // POCET_MINUT_V_HODINE # celočíselné dělení
pocet_minut = minuty % POCET_MINUT_V_HODINE # zbytek po dělení

print(minuty + " minut = " + str(pocet_hodin) + " hodin a " + str(pocet_minut) + " minut")
```


# Notes
Add to list of required functions to each assignment

input is difficult, describe exactly what it does

terminal vs source code
