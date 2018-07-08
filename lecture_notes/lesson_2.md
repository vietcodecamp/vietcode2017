# Lesson 2
* Lists, again len() and indexing, append, delete, pop
* Joining lists
* Strings, len(), concatenation, indexing, upper(), lower(), find()

## String
* We mentioned Strings in the first lesson already
* We will first go through indexing and then some basic functions

### Indexing
* We can access specific characters in a string
* Indexes are natural numbers rising from 0
* Note, we **cannot** change the value at the given index!!!
```python
x = "Texty text"
print(x[0]) # prints the 1st character of the string
x = "chiba"
x[2] = "y"  # 2 is the 3rd character
# TypeError: 'str' object does not support item assignment


### Functions and methods
* If we need the length of a string, we use `len()`
```python
x = len("ahoj") # x = 4
```
* If we need to change the case of the string, we use `upper()` for uppercase or `lower()` for lowercase at the end of the string
* This is different from `len()` is a function that takes any list or string and tells you its length
* `.upper()` and `.lower()` are functions specific for a given string


 ![alt text](https://orig00.deviantart.net/dd22/f/2017/151/5/8/mocking_spongebob_meme_by_thevideogameteen-dbb5ar0.jpg "Logo Title Text 1")


```python
my_brain_says = "aNd ThE DiSheS beTtEr Be CleA-"
what_should_i_say = x.lower() # here we say: take the sentence, change it's characters to lower case, save the result to a new variable
print(what_should_i_say)

# result: "and the dishes better be clea-"
```
No violence needed...

* We can add multiple strings together as seen in Lesson 1
```python
a = "Wingardium"
b = "Leviosa"
zaklinadlo = a + " " + b + "!"
```
* We use this feature often when printing output to the user (also seen in Lesson 1)
```python
pocet_knedliku = 8
print("Chtel bych gulas s " + str(pocet_knedliku) + " knedliky")
cela_veta = "Chtel bych gulas s " + str(pocet_knedliku) + " knedliky"
print(cela_veta)
```

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
* Lists are very similar to strings. However, unlike strings, it is possible to change each item in a list
```python
my_list = [1,2,3]
print(my_list)
my_list[0] = 0
print(my_list)
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
* Anything can be an item in a list, including another list 
```python
list_ovoce = ["Jablko", "Hruska", "Pomeranc"]
list_zelenina = ["Okurka", "Salat", "Mrkev"]
ovoce_a_zelenina = [list_ovoce, list_zelenina]
print(ovoce_a_zelenina)
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

### Fighting a dragon
* Create a list called 'inventory' for your knight that includes "sword", "puppy", "ice cream", "fancy hat" and 2 more items of your choice.
```python
inventory = ["sword", "puppy", ...]
```
* Find the right indexes to get the right item to fight the dragon and save the princess, make a good impression on the princess to fall in love with you and give her a wedding gift.

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

```python
****
*  *
*  *
****
```
```python
radek = "****"
sloupec = "*  *"
vysledek = radek + "\n" + sloupec + "\n" + sloupec + "\n" + radek
print(vysledek)
```

# Notes
* People confuse lists and indexing a lot
* They shouldn't name their list "list"
* We should go through loops very carefully.
* We can't assign while looping, try to *softly* explain why. (Concurrent write error)
* Indexing needs to be practiced specifically.
* split list and string and put exercise in between
* bring back `join` and `split`
