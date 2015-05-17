![Girl Develop It Logo](../images/gdi_logo_badge.png)

###Intro to Python
####Section 2
@@@

###Review

* Arithmetic
* Variables
* Data types
* Text editor, command line, and python shell
* Conditionals - if, elif, else
* Loops - while
@@@


###What we will cover today
* Loops - for
* Functions
* Method calls
* Python built-in funtions
@@@

###For loops
```python
numbers = [1, 3, 8]
for number in numbers:
    print "The current number is:"
    print number
```
@@@

###For loops continued
Let's examine the example carefully
```python
numbers = [1, 3, 8]
for number in numbers:
    print "The current number is:"
    print number
```
The for loop has three parts:

* The collection to loop over - numbers
* The name to give each element when the loop begins again - number
* The block of statements to execute with the element - The two print statements
@@@

### Let's Develop It!

Sam, Sally, Sarah are sudents. Write a loop that iterates over student names in a list and prints them.

@@@

###Greeting Robot

```python
"Hello, Marianna!"
"Please take Seat 1"

"Hello, Allen!"
"Please take Seat 2"

"Hello, Sally!"
"Please take Seat 3"
```

@@@

###What changes and what stays the same?

```python
"Hello, Marianna!"
"Please take Seat 1"

"Hello, Allen!"
"Please take Seat 2"

"Hello, Sally!"
"Please take Seat 3"
```

@@@

###Wouldn't this be nice?

```python
>>> greet("Marianna", 1)
"Hello, Marianna!"
"Please take Seat 1"

>>> greet("Allen", 2)
"Hello, Allen!"
"Please take Seat 2"

>>> greet("Sally", 3)
"Hello, Sally!"
"Please take Seat 3"

```
@@@

###We have seen this before!

```python
>>> a = '3'
>>> print type(a)
<type 'str'>
>>> a = float(a)
>>> print type(a)
<type 'float'>
```

@@@

###Functions

Also known as "procedures", a named unit of code that performs a specific task

```python
# Repeating the previous example for reference
>>> my_int_variable = 3
>>> print type(my_int_variable)
<type 'int'>
```

A function can take **arguments** (sometimes called **parameters**)

```python
# Some more function call examples

>>> str(3.2)
'3'
>>> int(3.2)
3
```
@@@

###Function definition

The following example is a **function definition**. This allows us to create our own functions

```python
def greet(name, seat):
    print "Hello ", name
    print "Please take Seat ", seat
```

The function definition has the following parts

* The <strong>def</strong> keyword signifies we are defining a function</li>
* The name of the function being defined - `greet`</li>
* The arguments in parentheses - `name`, `seat`</li>
* The function <strong>body</strong>, which is a block of indented code that executes when the function is called. - `print "Hello ", name...`</li>
@@@

### Let' Develop It!

Write a function that calculates the number of pets a person has. The function should take the following arguments as parameters:

* owner's name
* number of cats
* number of dogs
* number of birds

The function should print how many pets the owner has.
@@@

### Let's Develop It!

```python
def numberOfPets(owner, cats, dogs, birds):
    numPets = cats + dogs + birds
    print owner, "has", numPets, "pets"
```
@@@

###Function returns</h3>

A function can also **return** a value

To do this, one uses the **return** keyword
```
def plus_5(x):
    return x + 5

y = plus_5(4)
```

* This allows us to call a function to obtain a value for later use. (Not the same as printing the value)</li>
* If return is not used, the function returns <strong>None</strong></li>
@@@


### Let' Develop It!

Instead of printing the number of pets an owner has in the previous example, have the function return a string.
@@@

### Let's Develop It!

```python
def numberOfPets(owner, cats, dogs, birds):
    numPets = cats + dogs + birds
    return owner, "has", numPets, "pets"
```
@@@

###Functions with no arguments

A function does not have to take arguments, as in the following example:

```python
def newline():
    print ''

newline()
# prints an empty line. Nothing is returned
```

This is useful when the function does some work but doesn't need any parameters. i.e. The function is intended to always do the same thing
@@@

###Functions with more than one argument

A function can also take more than one argument separated by commas. For example:

```python
def get_birthday_greeting(name, age):
    return "Happy birthday to " + name + " who just turned " + str(age) + "!"

greeting = get_birthday_greeting("Virginia", 16)
print greeting
# Happy birthday to Virginia who just turned 16!
```
@@@

###Scope

The **scope** of a variable is the area of code in which a variable is still valid and can be used.

Variables defined within a function can not be used elsewhere.

```python
def get_average(a, b):
    total = a + b
    return total / 2.0

avg = get_average(10, 20)

print avg
# 15
print a
# NameError
print total
# NameError
```

Note: Draw a diagram with bubbles
@@@

###Import statements

The **import** statement allows us to use Python code that is defined in one file in a different file, or inside of the shell.

The **from** keyword allows us to only import parts of a Python file

```python
# In knights.py
def shrubbery():
    print "I am a shrubber"

def ni(number):
    print "Ni!" * 3
```

```python
# Run a Python shell in the same directory as knights.py and enter the following
import knights

knights.shrubbery()
knights.ni()

# or
from knights import shrubbery, ni
shrubbery()
ni()
```
@@@

###Let's Develop It
* Write a game that displays a board and allows a player to move on the board.

* The beginning of this program has been started and is available here as
[game1.py](http://calebsmith.github.io/gdi-intro-python/examples/game1.py)

* More instructions can be found in the game1.py file

* You'll also need to download the board.dat file to the same folder.
 [board.dat](http://calebsmith.github.io/gdi-intro-python/examples/board.dat)

* If you are stuck ask the teacher or a TA for help.

Note: Let's Develop It 25 minutes
@@@


###Let's Develop It
* Improve our adventure game by preventing the player from walking through
walls

* The beginning of this program has been started and is available here as
[game2.py](http://calebsmith.github.io/gdi-intro-python/examples/game2.py)

* You'll also need to download the board.dat file to the same folder.
 [board.dat](http://calebsmith.github.io/gdi-intro-python/examples/board.dat)

* If you are stuck ask the teacher or a TA for help.

* If you finish early, consider adding a feature of your own or helping your
 neighbor

Note: Let's Develop It 30 minutes
@@@

###Questions?
