# Exercises - Finished

## Importing time library

* Import the `time` library, read up the `sleep()` and `time()` function
* Create a script that counts down 3 seconds and lets the user write *"The quick brown fox jumps over the lazy dog"*
* Afterwards, it validates the input (you can do both `==` compare the strings or loop through the all characters
* finally, it tells the time elapsed between start of the input and when user wrote the new line, calculate words per minute
```python
import time

def countdown(n=3):
    for x in range(n, 0, -1):
        time.sleep(1)
        print("{} ...".format(x))
    print("GO!")

def initial_message():
    print("Please write the \"the quick brown fox jumps over the lazy dog\" when the countdown ends")
    print("all lowercase")

def time_input():
     correct_text = "the quick brown fox jumps over the lazy dog"
     start = time.time()
     text = input()
     end = time.time()
     if text == correct_text:
         duration = end - start
         print("Correct! It took you {} seconds!".format(duration))
     else:
         print("Incorrect! You entered a wrong text.")

initial_message()
countdown()
time_input()
```
