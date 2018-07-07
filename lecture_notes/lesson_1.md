# Lesson 1
**Lesson Goal**: At the end of this lecture the learner will be able to get an input from a user and use
it to do basic calculations.

## Outline

1. Variables
2. Basic operators
3. Data Types and Casting
4. Input and Output (IO)
5. Exercises

## Variables
* **Goal**: Store data that can be **reused**
* **Analogy**: Let's have a box and put a number in it. Then send this box to a machine (function) and the machine will do something with the number (for example calculate logarithm of that number)
* To work with data, a computer needs to store the values somewhere accessible to a human as well. For that we use the '=' operator.
* Note that `x = 3` doesn't mean "x is equal to 3", but "save the number 3 to the variable x" It's a command, not a statement!
* We can save constants, strings, but most importantly the results of functions. Note we have to read the text from right to left, as in `x = f(y)` "do this and save the result in x"
* People tend to want say "this is how the solution should look like" instead of "this is what you should do"
* Variable names should be meaningful.
* If the variable name is described by more words, the variable naming convention in python is snake_case. It means that the words are "separated" by an underscore `_` for example `number_of_students` (`numberofstudents` is much harder to read). Other languages use pascalCase (Java, Swift etc.). For more conventions and details visit [wiki](https://en.wikipedia.org/wiki/Naming_convention_(programming)).

Reading code exercise:

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

Quadratic equation:
* Lets say we have a quadratic formula ax<sup>2</sup> + bx + c = 0 and we want to get the solution

```python
a =  3
b = -11
c = 6

discriminant = (b ** 2 - 4*a*c) ** 0.5 # ** 0.5 - power to 1/2 is the square root
x1 = (-b  + discriminant) / (2 * a)
x2 = (-b  - discriminant) / (2 * a)
print(x1)
print(x2)
```

Swap:

```python
# We want to swap the numbers so that variable a holds number 4 and b holds number 3
a = 3
b = 4

# We can use a helper variable
helper_box = a
a = b
b = helper_box
```
What would happen if we just did this?
```python
a = b
b = a
```


## Arithmetic Operators
* Basic operators:
  * `+ `: addition
  * `-` : subtraction
  * `/` : division
  * `*` : multiplication
* Less basic operators:
  * `**` : exponent (`2**10` stands for 2<sup>10</sup> and returns 1024)
  * `%` : modulus - the remainder after division: `21 % 6` equals 3 because the remainder after division 21 by 6 is 3. It is used a lot for determining whether the number is odd or even ` x % 2 == 0` - "Is the remainder after division equal to 0?" If yes the number is even, odd otherwise
  * `//` : floor division - the result after division is rounded down ( `5.9 // 2.0` returns `2.0`)

* Please mention string concatenation at this point
```python
x = "ahoj"
y = "ky"
z = x + y
print(z) # prints "ahojky"
```


## Data types
* **Problem:** Data can be in various formats (for example integers ` a = 5 `, text ` a = "text"`) and the computer needs be able to distinguish whether it is working with a number or a text.
Example: The computer sums two numbers differently than two strings (`2 + 3` returns 5 but `"2" + "3"` returns `23` )

* **Solution:** Variables have an information of which type it is. This information is used to determine how to handle the data.

In Python3 we have integers, float, strings, boolean, objects

| Short |Type| Explanation|
| -- | -- | -- | -- |
| `int` | integer  | whole numbers |
| `float` | float | numbers with decimals |
| `bool` | boolean | `True` or `False`|
| `str` | string | texts and always between parentheses|

## Casting
* **Problem:** Sometimes we have data in one format but we want to use it differently.
```python
 >>> "2" + "3" #note the double quotes
'23'
```
* **Solution:** We "say" to the computer that it is a number and not a text and it will behave that way.
```python
>>> int("2") + int("3")
5
```
* What will happen when we cast something, that is not castable?
  * the computer will throw an error
```python
>>> int("text")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'text'
```  
* Some things are automatically castable:

int + float => float

If we add a integer with a float, the result will automatically be a float
```python
>>> 1 + 4.0
5.0
```
* Some are not:

int + str => error
```python
>>> x = 3 + "ahoj"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
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
* The program usually wants some data from the user (input). And the users want to see the results also (output).
* The easiest way to get input from the user is the `input()` function in python3. Note the **data type is a string**.
* Print is a large chapter and might need a separate lesson.
* Note: It is preferable that we validate and sanitize the input first

```python
x = input() # retrieve string input from user, we can cast this to integers or floats!
print(x) # print takes the parameter x and prints it on the console

# Input takes a optional parameter for a user prompt, improving usability.
# Explain what is a function parameter.
y = input("Zadejte prosim cislo")
```

## Exercises

### Retirement
* Write a program that receives your age and tells you **how many years** you have left **before you retire**. (The age of retirement should be **65**.
You will only need `input()`, `print()`, `int()`, `str()` and `float()` for casting

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
You will only need `input()`, `print()`, and `float()` for casting

```python
# expected output at this point
# explain how to divide the program into steps
vaha = float(input("Kolik vazis? (v kg)"))
vyska = float(input("Kolik meris? (v metrech)"))
bmi = vaha / vyska ** 2
print("Tvé BMI je " + str(bmi))
```
### Circle
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

### Minutes to hours and minutes
* Write a program that receives a number representing **minutes**. The goal is to convert minutes into **hours and minutes**. You will need `input()`, `print()`, `str()` and `int()` for casting. You will further need these operators: integer division (`//`) and modulo (`%`) (modulo calculates the reminder after division, eg. `5%3 = 2` - the remainder after dividing `5` by `3` is `2`)

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
