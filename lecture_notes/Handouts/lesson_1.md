# Lesson 1
**Lesson Goal**: At the end of this lecture the learner will be able to get an input from a user and use
it to do basic calculations.

## Outline
1. Why do we need programming?
2. Variables
3. Basic operators
4. Data Types and Casting
5. Input and Output (IO)
6. Exercises


## Why do we need programming?
To make life easier! Computers can do a lot for us. Let's show it on this motivational example
### Programming lvl 1: calculator
* You all are familiar with solving quadratic equations. What is the general cookbook for solving them?
Try calculating solution for this simple task (to get hands on Python shell):

   5x<sup>2</sup> + 6x + 1 = 0

* now try it for:

  10x<sup>2</sup> - 9x + 6 = 0

* still not tired? Go with this one:

  -23.12x<sup>2</sup> - 16.09x + 9.88 = 0

How about calculating all quadratic equations there is? Introducing...

### Programming lvl 2: scripts
* Look at the process of solving the equation. Are there steps, which you have to type into the calculator every time
to solve an equation?
* If you guessed the formula for discriminant and the formula for actual solution(s), you were right!
  Those are the *common* part for every solution. We want to write them only once. Imagine solving millions of equations. **Your fingers would fall off!**
* What are however the symbols, that change with every equation?

  Right, the coefficients of the equation. Now tell me, are those coefficients all we need for solution?

  The answers is yes! Those 3 numbers are really what we need to solve any quadratic equation!

  How do we do it? Well, as we said before, we write down the common parts:

```python
from math import sqrt

D = b**2 - 4*a*c

x1 = (-b + sqrt(D)) / (2*a)
x2 = (-b - sqrt(D)) / (2*a)
```
* And now, if we substitute for *a*, *b* and *c* we get the solutions. Try it for our first example:

```python
from math import sqrt

a = 5
b = 6
c = 1

D = b**2 - 4*a*c

x1 = (-b + sqrt(D)) / (2*a)
x2 = (-b - sqrt(D)) / (2*a)

print(x1)
print(x2)
```
There you go - solving (almost) every quadratic equation there is - just change *a*, *b* and *c*. No typos, no numeric errors. Oh, how I wish I had this during my math exams....

## Variables
* **Goal**: Store data that can be **reused**
* **Analogy**: Let's have a box and put a number in it. Then send this box to a machine (function) and the machine will do something with the number (for example calculate logarithm of that number)

* In the previous example we used a sign " = " to tell the computer, what  *a*, *b* and *c* are. Notice the word **tell**. This is an difference in meaning from math, which
is better seen on an example:
* `x = 3` in programming doesn't mean *"x is equal to 3"*. It means: *"Computer, I order you to take number 3 and save it to the variable x. AND DO IT NOW!!!"*
  In other words, it's a command, not a statement!
* We can also **store** strings (words) too: `cat = "Khajit"`, but most importantly the results of functions: `x = sqrt(y)` Note we have to read the text from right to left:
 *"Computer, do the square root of whatever is in y and save the result in x."*
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
y = input("Please enter a number")
```

## Exercises
* [Files](../Exercises/Lesson_1)
* [Start](../Exercises/Lesson_1/lesson_1_start.md)
* [Finished](../Exercises/Lesson_1/lesson_1_finished.md)

# Notes
Add to list of required functions to each assignment

input is difficult, describe exactly what it does

terminal vs source code
