# Lesson 2
**Lesson goal:** At the end of this lesson the learner will understand the concept of strings and lists and how to use them.

## Outline
1. Strings
2. Indexing
3. Functions and methods to use with strings
4. Lists and their properties
5. Exercises

## Motivation
* Your avatar collects magical items throughout the game. How to save them all in your inventory without losing any?
```python
inventory = []
new_item = input("Insert a new inventory item: ")
inventory.append(new_item)
new_item = input("Insert a new inventory item: ")
inventory.append(new_item)
...
print(inventory)
```

## String
* We mentioned Strings in the first lesson already
* String is a data type that stores any sequence of characters - eg. letters, words or even whole sentences.
* We will first go through indexing and then some basic functions to work with strings.

### Indexing
* We can access specific characters in a string
* Indexes are natural numbers rising from 0.
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
**Goal:** Store data in one variable instead of multiple variables.

**Analogy:** Let's take the case with putting a number into a box and passing the box to the machine. What if we want the machine to process hundreds of different numbers? We can pass hundreds of boxes one by one or pass a single box with many little boxes inside for each number.
* Sometimes we want to have several variables. Instead of creating and naming
each variable by hand, we can create a list. A list is a variable that contains several values.
```python
x1 = 1
x2 = 2
x3 = 3
my_list = [1,2,3]
```
* What do you like more?
```python
day1 = "Monday"
day2 = "Tuesday"
day3 = "Wednesday"
day4 = "Thursday"
day5 = "Friday"
day6 = "Saturday"
day7 = "Sunday"
```
or
```python
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
```
* We access variables in the list using indexing
* Indexing tells us which value in the list we want.
* We have to index from 0 due to historical computer reasons. Ask them what is the first **non-negative** integer so they get the idea.
```python
my_list = [1,2,3]
print(my_list[0]) # output first element of the list
print(my_list[2]) # output the third element of the list
```
* What index does Monday have? What about Sunday? What day is on the index 7?
```python
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[7])
```
* Lists are very similar to strings. However, unlike strings, it is possible to change each item in a list
```python
my_list = [1,2,3]
print(my_list)
my_list[0] = 0
print(my_list)
```
* Anything can be an item in a list, including another list
```python
list_ovoce = ["Jablko", "Hruska", "Pomeranc"]
list_zelenina = ["Okurka", "Salat", "Mrkev"]
ovoce_a_zelenina = [list_ovoce, list_zelenina]
print(ovoce_a_zelenina)
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
* Another functions to use with lists are for example .pop(index), .insert(index, data). Try them out:
```python
my_list = [1,2,3]
my_list.pop(0)
print(my_list)
my_list.insert(0,1)
print(my_list)
```

## Exercises
* [Files](../Exercises/Lesson_2)
* [Start](../Exercises/Lesson_2/lesson_2_start.md)
* [Finished](../Exercises/Lesson_2/lesson_2_finished.md)

# Notes
* People confuse lists and indexing a lot
* They shouldn't name their list "list"
* We should go through loops very carefully.
* We can't assign while looping, try to *softly* explain why. (Concurrent write error)
* Indexing needs to be practiced specifically.
* split list and string and put exercise in between
* bring back `join` and `split`
