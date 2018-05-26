# Lesson 6
* Review, functions, code organization and reuse, projects, problem examples with solutions
* Importing libraries
* Downloading new libraries (conda? pip?) and using them
* What is git? How do programmers share code?


## Exercises
* Import the time library, read up the sleep() and time() function
* Create a script that counts down 4 seconds and lets the user write "The quick brown fox jumps over the lazy dog"
* Afterwards, it validates the input (you can do both == compare or loop through the string
* finally, it tells the time elapsed between start of the input and when user wrote the new line, calculate words per minute
```python
# @Andrej
import time

def countdown(n=4):
    for x in range(n, 0, -1):
        time.sleep(1)
        print("{} seconds remaining".format(n))
    print("NOW")

def initial_message():
    print("Please write the \"quick brown fox jumps over the lazy dog\" when the countdown ends")
    print("all lowercase")

def time_input():
     correct_text = "quick brown fox jumps over the lazy dog"
     start = time.time()
     text = input()
     end = time.time()
     if text == correct_text:
         duration = end - start
         print("Correct!, you took {} seconds!".format(duration))
```

# Hackaday #2
* requests, beautifulsoup
* Selenium to control browser?
* Graphs?
* Loading facebook data?