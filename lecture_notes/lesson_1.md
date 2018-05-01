# Lesson 1
* We should explain variables properly (especially the = operator), then speed through input and output (skip string formatting for lesson 2)
* Variables, data types, casting, input, output, arithmetic operators
* Ideally we would end with each student having a simple script that gets user input and outputs something
 
## Variables
* To work with data, a computer needs to store the values somewhere accessible to a human as well. For that we use the '=' operator.
* Note that x = 3 doesn't mean "x is equal to 3", but "save the number 3 to the variable x" It's a command, not a statement!
* We can save constants, strings, but most importantly the results of functions. Note we have to read the text from right to left, as in x = f(y) "do this and save the result in x"
* People tend to want say "this is how the solution should look like" instead of "this is what you should do"
* Reading code exercise 

```python
x = "test" # save the string test to the variable x

y = x # now y has "test"

z = 5
z = z + 5 # Remember to read this from right to left!

x + 4 = 5 # an equation, not usable! Some languages allow formulas, though
```
*TODO*: Add pythagoras as an example
## Data types, casting
* *NOTE: specify difference between float and integers*

In Python3 we have integers, float, strings, boolean, objects
* Strings are always between parentheses (We will show how to include parentheses next lesson)
* Some things are automatically castable:

int + float => float

If we add a integer with a float, the result will automatically be a float
```
1 + 4.0 = 5.0
```
* Some are not:

int + str => error
```
x = 3 + "ahoj" # error
```
* Some are dangerous

int / int => int

We can cast types to different types using the following functions
int(), float(), str()
```
x = 3.0 # x is a float
x = int(x) # x is now 3
x = str(x) # x is now "3"
x = x + " kg"   # x is now "3 kg"

y = "5.6" # a string
y = float(y) # y is 5.6
```

## Input and output
* The easiest way to get input from the user is the input() function in python3. Note the data type is a string.
* Print is a large chapter and might need a separate lesson. 
* Mention input sanitization.

```
x = input() # retrieve string input from user, we can cast this to integers or floats!
print(x) # print takes the parameter x and prints it on the console

y = input("Zadejte prosim cislo") # Input takes a optional parameter for a user prompt, improving usability. Explain what is a function parameter.
```

## Operators
* Basic things such as +, -, /, //, \*, \*\*, ==
* What happens when we nest functions together?
* Please mention string concatenation at this point
```
x = "ahoj"
y = "ky"
z = x + y
print(z)
```



## Exercises
* Write a program that gets your age and tells you how many years you have left before you retire. (The age of retirement should be 65.
You will only need input(), print(), int(), str() and float() for casting

```python
# expected output at this point
# explain how to divide the program into steps
vek = input("Kolik je ti let? ")
let_do_duchodu = 65 - int(vek)
odpoved = "Zbyva ti " + str(let_do_duchodu) + " let do duchodu!"
print(odpoved)
```
* Write a program asks you for your weight and height and calculates your BMI. Lookup the BMI formula on wikipedia. Use meters instead of centimeters
You will only need input(), print(), str() and float() for casting

```python
# expected output at this point
# explain how to divide the program into steps
vaha = float(input("Kolik vazis? (v kg)"))
vyska = float(input("Kolik meris? (v metrech)"))
bmi = vaha / vyska ** 2
print(bmi)
```
# Notes
Add to list of required functions to each assignment

input is difficult, describe exactly what it does

terminal vs source code
