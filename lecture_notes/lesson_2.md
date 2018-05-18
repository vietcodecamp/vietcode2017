# Lesson 2
* Lists, again len() and indexing, append, delete, pop
* Joining lists
* Strings, len(), concatenation, indexing, upper(), lower(), find()

## List
* Sometimes we want to have several variables. Instead of creating and naming
each variable by hand, we can create a list. A list is a variable that contains several values.
```python
x1 = 1
x2 = 2
x3 = 3
my_list = [1,2,3]
```
* We access variables in the list using indexing
* Indexing tells us which value in the list we want.
* We have to index from 0 due to historical computer reasons. Ask them what is the first **non-negative** integer so they get the idea.
```python
my_list = [1,2,3]
print(my_list[0]) # output first element of the list
print(my_list[2]) # output the third element of the list
```
* To add to an existing list, we can use `.append()` to add the value to the end
```python
my_list = []
my_list.append(1) # Take my_list, add number 1 to the end of it!
my_list.append(2)
my_list.append(3)
print(my_list)
```
* If you ever want to know how many values there are in a list, you can use the `len()` function. The `len()` function tells you how many items a list has
```python
lecturers = ["Dacos", "Dagy"]
lecturers_count = len(lecturers)
print("there are " + str(lecturers_count) " lecturers")
```
* If we have two lists, we can simply concatenate them together using the `+` operator!
```python
prvni_list = [1,2,3]
druhy_list = [4,5,6]
treti_list = prvni_list + druhy_list
```

## String
* We mentioned Strings in the first lesson already
* In many languages we can see strings as a list of characters
* In python, it is very similar (you will see how we can have both indexing and len), but also has some additional things that makes it easier to work with.
* We will first go through the functions and then go through indexing

### Functions and methods
* If we need the length of a string, we use `len()` again! Yay!!!!!
```python
x = len("ahoj") # x = 4
```
* If we need to change the case of the string, we use `upper()` for uppercase or `lower()` for lowercase at the end of the string
* This is different from `len()` is a function that takes any list or string and tells you its length
* `.upper()` and `.lower()` are functions specific for a given string
```python
x = "malym"
x_caps = x.upper() # here we say: take x, change it's characters to upper case, save the result to x_caps
print(x_caps)
x_zase_malym = x_caps.lower()
print(x_zase_malym)
```
* Can you append to a string? Sadly not! Booo!

### Indexing
* Again, we can access specific characters in a string
* Note, we **cannot** change the value at the given index!!!
```python
x = "Texty text"
# Using indices just like in lists!
print(x[0]) # prints "T"
x = "chiba"
x[2] = "y"  # 2 is the 3rd character
# TypeError: 'str' object does not support item assignment
```

## Escaping characters
* We encapsulate strings in `""`, so how do we write `""` inside a string? We use escaping. By adding the `\` sign, the quote sign loses it's power and becomes a regular character.
* Alternatively, use single quotes

```python
x = "Petr rekl \"Ahoj.\""
y = 'Maria mu odpovedela "Cauky"'
```

* If you want to make a new line in python, you have to use a special combination of charaters, `\n`
* How would you print "\n"? Why, using escaping again! The escape character always modified the next character

```python
print("\\n")
```

## Formatting intro
* Let's asume we calculated circumference and area of a circle and we wan't to print the result to the user. The most common way of doing this is the following:
  * basic concatenation
```python
print("Obvod kružnice je " + str(obvod) + " a obsah kruhu je " + str(obsah) )
```
  * using `format` function
```python
print("Obvod kružnice je {} a obsah kruhu je {}".format(obvod, obsah))
```
  * using formatted string
```python
# note the "f" in front of the string
print(f"Obvod kružnice je {obvod} a obsah kruhu je {obsah}")
```

## Exercises
### Input length
* Write a script that reads the input of a user and tells him how many characters he wrote

```python
vstup = input("Napis text ")
pocet_znaku = len(vstup)
odpoved = "Napsal jsi" + str(pocet_znaku) +  "znaku!"
print(odpoved)
```

### Quotes in string
* Write a script that asks the user for input, then repeats the input in quotes like this: __"You said " ", am I right?"__
  * Note we want the **quote marks inside**!

```python
vstup = input("Napis text ")
odpoved = 'You said "' + vstup + '", am I right?'
print(odpoved)
```

### Saving inputs into a list
* Write a script that asks for 3 names, saves them to a list and prints it

```python
jmena = [] # empty list
jmena.append(input("Napiš první jméno: "))
jmena.append(input("Napiš druhé jméno: "))
jmena.append(input("Napiš třetí jméno: "))
odpoved = "{}, {} a {} se potkali v hospode a dali si pivo".format(jmena[0], jmena[1], jmena[2])
print(odpoved)
```

### READING exercise
```python
x = "kaktus klobasa kolovratek krab"
```
* What is `x[3]`?
* What is `x[6]`?
* What is `x[5:8]`?

```python
print(x[3]) # 't'
print(x[6]) # ' '
print(x[5:8]) # 's k'
```

### Upper Case
* Write a script that yells back at you whatever you tell it. You will use `upper()`

```python
vstup = input("Co delas ")
odpoved = vstup.upper() + "!!!"
print(odpoved)
```

### X-mass tree
* Draw a x-mass tree. Use a single print function and a string concatenation method
  * Note, we will improve this using loops later on
It should look like this:

```
   *
  ***
 *****
*******
   *
   *
```
```python
prostredni_hvezda = "   *\n"
print(prostredni_hvezda + "  ***\n" + " *****\n" + "*******\n" + prostredni_hvezda + prostredni_hvezda)
```

### Rectangle
* Draw a 4 x 4 empty rectangle using string concatenation and \n
  * Note, we will also improve this using loops later on

```
****
*  *
*  *
****
```

```python
radek = "****"
sloupec = "*  *"
vysledek = "{}\n{}\n{}\n{}".format(radek, sloupec, sloupec, radek)
```

### Single quotes and escaping
* print out `Alenka řekla: "Běž mi koupit rohlíky, Honzo."` using single quotes AND escaping

```python
print( "Alenka řekla: \"Běž mi koupit rohlíky, Honzo.\"")
print( 'Alenka řekla: "Běž mi koupit rohlíky, Honzo."')
```
## Extras
* `String.split()` to create a list out of a string
* `" ".join(list)` to get a string out of a list

# Notes
* People confuse lists and indexing a lot
* They shouldn't name their list "list"
* We should go through loops very carefully.
* We can't assign while looping, try to *softly* explain why. (Concurrent write error)
* Indexing needs to be practiced specifically.
* split list and string and put exercise in between
* bring back `join` and `split`
