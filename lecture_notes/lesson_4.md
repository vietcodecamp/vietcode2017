# Lesson 4
* For loops, range, iterating through a list
* Note: very hard

# Iterating through a list
* We have a list of variables and we can access them using indexing. We can add to them using `.append()`.
* Now we might want to go through each value in the list and do something with it. For that, we need a for loop.
* the notation is as follows:

```python
seznam = [1, 2, 3, 4]
for x in seznam:
    print(x)    # note the indentation
```

* What happens here? *NOTE* Go through this slowly
* The for loop tells python to go through each value in `seznam` (1,2,3,4) and save it to `x`
* Afterwards, you can do anything you want with `x`. Everything you do with `x` has to be *indented* using either 4 spaces or tabs

* We can combine this with if conditions from the last lesson

```python
# print values larger than 4
seznam = [1, 2, 3, 4, 5, 6, 7, 8]
for x in seznam:
    if x > 4:
        print(x)
```

* Now with conditions, lists and loops we can implement most of our problems! We'll try to make more pratical exercises here

# range()
* We can iterate through a list directly by using
```python
for x in seznam:
    print(x)
```
* Often, we will want numbers from 0 to n (Often as in almost always) or maybe do something n times instead of once
* For that we could always create a list of a given length and use it
```python
seznam = [0, 1, 2, 3, 4, 5, 6, 7]
for x in seznam:
    # do something
```
* But more commonly, we will use the `range()` function
```python
for x in range(8):
    print(x)  # this will print all the numbers from 0 to 7 - 8 is excluded
```

* `range` is a so called generator. This is a very pythonic concept which we will not discuss in depth, but try:
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
even = range(0, 10, 2)
print(list(even)) # prints out "[0, 4, 6, 8]"
odd = range(1, 10, 2)
print(list(odd)) # prints out "[1, 3, 5, 7, 9]"
```

# Exercises
## Printing square
* Make a square using loops! Let the user set any size

```
****
*  *
*  *
****
```

## Input in for loop
* Get 5 favourite foods from a user using a loop

## Average
* Calculate the average shoe size in your class. First ask for the number of students, then get all of their sizes. Then sum and divide them to get the average
