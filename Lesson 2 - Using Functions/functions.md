# Functions in Python


## Brief Introduction:

(Source: [https://www.w3schools.com/python/python_functions.asp](https://www.w3schools.com/python/python_functions.asp))



*   A function is a block of code which only runs when it is called. It performs a specific task.
*   You can pass data, known as parameters, into a function.
*   A function can return data as a result to the calling function.


### Python Sample program to display the use of functions:
```
#This function checks whether the entered number is a multiple of 5 or not:
def check( x ):
    if (x % 5 == 0):
        print "Yes"
    else:
        print "No"
#Driver code
check(2)
check(3)
```

In python we can also assign functions to variables

```
evenOdd = check
#Driver code
evenOdd(2)
evenOdd(3)
#the output will be same as of previous function calls: check(2) , check(3)

```

## Creating a Function

In Python a function is defined using the `def` keyword:


```
def my_function():
  print("I am a Function")
```



## Calling a Function

To call a function, use the function name followed by parenthesis:


```
def my_function():
  print("Hello from a function")

my_function()
```



# Some more examples

Here are some more examples showing how functions are used, and how they can be used.


```
def hasNoWhiteSpace (string):
    # Create a second variable to compare the first with, which does not have white space in it.
    nows = string.replace(" ", "")
    # If the new, non-white-space variable is the same as the first, then that means the first didn't have white space
    # in it in the first place.
    if nows == string:
        return string
    else:
        return None

string = "This string has white space, being the spaces."

# Functions can be called as parts of ifs, whiles, other functions, what have you.
if hasNoWhiteSpace(string) :
    print("The string doesn't have white space.")
else:
    print("The string has white space.")

# The result if there are no spaces.
string = "Thisstringdoesnothavewhitespace."

if hasNoWhiteSpace(string) :
    print("The string doesn't have white space.")
else:
    print("The string has white space.")

# Expected output:
# The string has white space.
# The string doesn't have white space.
```

```
# An example of a tally counter using a global variable and some functions.
COUNT = 0

# Set the counter back to 0.
def reset():
    global COUNT
    print("*unclick*")
    COUNT = 0

# Click the counter up one.
def click():
    global COUNT
    COUNT += 1
    print("*click*")

# Return the count of the tally counter.
def look():
    return COUNT

reset()
print(look())
click()
click()
click()
click()
print(look())
reset()
print(look())

# Expected output:
# *unclick*
# 0
# *click*
# *click*
# *click*
# *click*
# 4
# *unclick*
# 0
```



#### With this short and crisp refresher on functions in python, below you will find a walkthrough on some in-built functions in Python. It is expected that you have preliminary programming knowledge (Iterators, Conditions, Syntax, Semantics, etc.) 


# MODULE 1: CREATING  A REMINDER APP

Before heading further to Module 1, It is important to know where the functions of Python are stored. Python uses the concept of libraries to store functions and classes (later in this course).


# The Python Standard Library


(Source:[https://docs.python.org/3/library/](https://docs.python.org/3/library/))

While [The Python Language Reference](https://docs.python.org/3/reference/index.html#reference-index) describes the exact syntax and semantics of the Python language, this library reference manual describes the standard library that is distributed with Python. It also describes some of the optional components that are commonly included in Python distributions.


### Task 1: Create a Python script to set a reminder in a fix duration of time that opens a Youtube video using functions in Python. 

(This can be used to take a break from extended computer usage.)


### Hints: 



*   Python Standard Library has a module called 'webbrowser'
*   Check on Resources to get the solution 


### TASK 2: There is a message to be decoded. There have been pictures of file format .jpg which have to be renamed in such a way that the digits in the names have to be removed which upon sorting would show a message. There is a folder containing all those images along this lesson. Write a python script to decode the message.

(Wait What??....Yes! This can be used as a prank with your friends.)


### Hints: 



*   Python Standard Library has a module called 'os'
*   Use listdir function inside the os module
*   Refer to the Internet for complete documentation of os module
*   Check on Resources to get the solution 


# About Used Modules:



*   [https://docs.python.org/2/library/webbrowser.html](https://docs.python.org/2/library/webbrowser.html)
*   [https://docs.python.org/2/library/os.html](https://docs.python.org/2/library/os.html)


Refer to [https://data-flair.training/blogs/python-built-in-functions/](https://data-flair.training/blogs/python-built-in-functions/) for a list of python inbuilt functions and explore their potential.


