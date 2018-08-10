# Lesson 3
**Lesson goal:** At the end of this lesson the learner will understand the basic concepts of conditionals and logical operators

## Outline
1. Conditionals `if` and `not`
2. Comparison operators (used inside `if` and `not`)
3. Logical operators (used inside `if` and `not`)
4. Nested conditions
7. Program termination.
8. Exercises

## Booleans
* For conditionals, we work with the boolean data type, which is either `True` or `False`.
  * You can also use `1` and `0` in Python
  * or you can create a language which uses `:)` and `:(`
* Note a boolean is a data type we can assign to a variable (`is_Earth_round = False`)
* We create a boolean as a result of comparison operators
```python
# Basic comparison operators
x = 3 # This is not equal! This is a declaration!
x > 3 # False
x >= 3 # True
x < 5  # True
x <= 2  # False
x == 3  # is x equal to three? Yes!
x != 4  # is x not equal to 4? Yes!
y = x != 4  # Evaluate x is not equal to 4, save the result to y
```

## Conditionals
* The basic conditional is `if <expression>`:
  * `expression` can be anything that is boolean. For example `if 2 > 1: print("I'm not mad")`
* If the logical expression is true, the if will run the indented commands. Otherwise nothing will happen
* We also have `else`. If the condition in the if evaluates to `False`, the else branch gets run. Either the code in the `if` section runs, or the code in the `else` section runs. Never both!

```python
x = 4
if x == 4:
    print("this should be printed out)
print("This should also be printed out")
```

```python
x = 3
y = 5
if x == 4:
    print("this should NOT be printed out)
elif y == 5:
    print("this should be printed out)
else:
    print("This should NOT be printed out")
print("This should be printed out again")
```

```python
x = 4
if x == 4:
    print("this should be printed out)
else:
    print("This should NOT be printed out")
print("This should be printed out again")
```

## Logical operators
* To combine conditions, we can use `and` and `or` operators
* To invert a value use `not`
* **NOTE**: recall the truth value table

## Nested conditions
* For more complex schemes, we can nest if statements in each other.
* It is often better to combine them into **and** statements, sometimes it is not possible

```python
if x > 2:
    if x < 4:
        print("x is between 2 and 4")
# OR
if x > 2 and x < 4:
    print("x is between 2 and 4")

# OR
if 2 < x < 4:
    print("x is between 2 and 4")    
```

## Terminating a program
* There are cases where we need to terminate program earlier because there is no need to process anything further.
* To exit a program we can use the function `exit()` or `quit()`, with the parameter that determines the exit code (we do not cover exit codes in this course).
* Note: It's recommended to use `sys.exit()` in programs instead of `exit()` or `quit()`. To see more read the official Python [documentation](https://docs.python.org/3/library/sys.html#sys.exit).
```python
login = input("Enter your login name: ")
if login != "kemper":
    print("The login name: " + login + " is invalid!")
    exit(1)
password = input("Enter your password: ")
print("Your password is obsolete. Please change your password!")
```

## Exercises
* [Files](../Exercises/Lesson_3)
* [Start](../Exercises/Lesson_3/lesson_3_start.md)
* [Finished](../Exercises/Lesson_3/lesson_3_finished.md)

# Hackaday #1
* Ifs are a big part of computing, we can show them examples of scripts that make our lives better. If someone has a good suggestion, you can do live coding

# Notes
* People often try to put the results of a function in a if statement
```python
if x = input() < 3:
```

Discourage that
* People also tend to insert too many statements into one if
```python
if x > 4 and 5:
    <code>
```
Is semantically wrong, because x > 4 gets evaluated to 4 and then you compare True and 5.
