# Lesson 4
**Lesson goal:** After this lesson the learner will be able to use a construct (`for`- loop) for repeating a block of code and iterating though a list.

# Outline
1. Repeating a block of code
2. Inner loop
3. List iteration
4. Exercises

# Repeating code several times


![bart-blackboard-board](http://bartsblackboard.com/files/2009/11/the-simpsons-s01e02-Bart-the-Genius.jpg)
*Avoid this in coding!*

**Goal:** Repeat a block of code without duplicating it.

* Often, we will want numbers from 0 to n or maybe do something n times instead of once

```python
for x in range(8):
    print(x)  # this will print all the numbers from 0 to 7 (8 is excluded)
```
* The **indentation** of the `print(x)` is **very important!**. Everything you want to run in a loop must be indented. Otherwise it will be executed only once like a "regular" line of code:
```python
sentence = 'I will not waste chalk'
for x in range(100):
    print(sentence)  
```
and
```python
sentence = 'I will not waste chalk'
for x in range(100):
print(sentence)  
```

are different. One will print 100 sentences (and Bart would go home), the other will print just one sentence.

* `range` is a so called generator (like the real-life generators create power, Python generators create a sequence of something - here numbers). It's something we will not discuss in depth, but try:
```python
x = range(6)
print(x)
print(list(x))
```

* With `range`, you can create many sequences of numbers!
* We can also make a `range` that does not start with 0. For example:
```python
x = range(3, 7)
print(list(x)) # prints out "[3, 4, 5, 6]"
```
* We can also make a `range` that increments by different number than 1 For example:
```python
sudy = range(0, 10, 2)
print(list(even)) # prints out "[0, 4, 6, 8]"
odd = range(1, 10, 2)
print(list(odd)) # prints out "[1, 3, 5, 7, 9]"
```

# Inner loop
* **Problem:** Sometimes we need to iterate through more dimensional list. For example let's say we have a chess board with the location of the pieces saved in a list of lists like this:

```python
game_state = [
    ["B-Rook", "", "", " B-Queen", "", "B-Rook", "B-King", ""],
    ["B-Pawn", "B-Pawn", "", "", "B-Pawn", "B-Pawn", "B-Bishop", "B-Pawn"],
    ["", "B-Knight", "B-Pawn", "", "", "B-Knight", "", "B-Pawn"],
    ["", "", "W-Queen", "", "", "", "W-Bishop", ""],
    ["", "", "", "W-Pawn", "W-Pawn", "", "B-Bishop", ""],
    ["", "", "W-Knight", "", "", "W-Knight", "", ""],
    ["W-Pawn", "W-Pawn", "", "", "", "W-Pawn", "W-Pawn", "W-Pawn"],
    ["", "", "", "W-Rook", "W-King", "W-Bishop", "", "W-Rook"]
]
```
The corresponding board is this:
![chess-board](./images/chess_board.png)

Note the picture visually corresponds to the list of lists. The top left corner has index `(0,0)` and bottom right `(7,7)`. (The black queen has coordinates `(0,3)`)

And now we need to have an output like this:
```python
________________________________________________________________________________
|B-Rook  ||        ||        || B-Queen||        ||B-Rook  ||B-King  ||        |
________________________________________________________________________________
|B-Pawn  ||B-Pawn  ||        ||        ||B-Pawn  ||B-Pawn  ||B-Bishop||B-Pawn  |
________________________________________________________________________________
|        ||B-Knight||B-Pawn  ||        ||        ||B-Knight||        ||B-Pawn  |
________________________________________________________________________________
|        ||        ||W-Queen ||        ||        ||        ||W-Bishop||        |
________________________________________________________________________________
|        ||        ||        ||W-Pawn  ||W-Pawn  ||        ||B-Bishop||        |
________________________________________________________________________________
|        ||        ||W-Knight||        ||        ||W-Knight||        ||        |
________________________________________________________________________________
|W-Pawn  ||W-Pawn  ||        ||        ||        ||W-Pawn  ||W-Pawn  ||W-Pawn  |
________________________________________________________________________________
|        ||        ||        ||W-Rook  ||W-King  ||W-Bishop||        ||W-Rook  |
________________________________________________________________________________
```


 and we want to print the name of the figures on the play board. Now assume that w
* **Solution:**
  We can also make a loop inside a loop and print it like this:
```python
horizontal_line = "_" * 80
for row in range(8):
    print(horizontal_line)
    for column in range(8):
        print("|{:8s}|".format(game_state[row][column]), end="")
    print() #print new line
print(horizontal_line)
```
  **Note:** This is not the best way to print the chess board and this example is just to demonstrate that we can have a loop inside a loop.

# Iterating through a list
* **Goal**: We want to access each element in a list and then do something with it. This is how we do it:


```python
seznam = [1, 2, 3, 4]
for x in seznam:
    print(x)    # opět si všimni odsazení
```

* **How it works:**
  1. The loop takes values from the list `seznam` one by one and saves it to variable `x`.
  2. Afterwards, you can do anything you want with variable `x`. Everything you do with `x` has to be *indented* using either 4 spaces or tabs. Again, the indentation is very important

* Here is some intuitive example, to show you the usefulness:
```python
dárky = [voucher, šampon, šála, cash]
for dárek in dárky:
    zabalit(dárek)
    poslat(dárek)
```
* But it's not always this easy. In a lot of programming languages we would iterate through indexes and access the element in the list though indexing.

```python
seznam = [1, 2, 3, 4]
for i in range(len(seznam)): # len(seznam) vrací počet prvků v poli, to je důležité, abychom nepoužili index, který pole neobsahuje
    print(seznam[i])
    #udelej_neco(seznam[i])
```
* As you can see this syntax has a lot of repeating code and it's harder to read.

* Now with conditions, lists and loops we can implement most of our problems! We'll try to make more practical exercises here
```python
# print values larger than 4
seznam = [1, 2, 3, 4, 5, 6, 7, 8]
for x in seznam:
    if x > 4:
        print(x)
```

* Of for someone, who likes more the real-life intuition
```python
dárky = [voucher, šampon, šála, cash]
for dárek in dárky:
    zabalit(dárek)
    if pro_maminku or pro_Ivetku:
        přidat_přání_do(dárek)
    poslat(dárek)
```


# Exercises

* [Files](../Exercises/Lesson_4)
* [Start](../Exercises/Lesson_4/lesson_4_start.md)
* [Finished](../Exercises/Lesson_4/lesson_4_finished.md)
