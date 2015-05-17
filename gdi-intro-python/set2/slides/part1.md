![Girl Develop It Logo](../images/gdi_logo_badge.png)

###Intro to Python
####Section 1
@@@

## Welcome
Girl Develop It is here to provide affordable and accessible programs to learn software through mentorship and hands-on instruction.

Some rules

* We are here for you
* Every question is important
* Help each other
* Have fun!
@@@


### About your instructor

Hi! My name is Marianna Budnikova

![Girl Develop It Logo](../images/marianna.jpeg) 

* Computer Science, B.S, Boise State University, 2013
* Computer Science, M.S, Boise State University, 2014
* Metageek Professional Hacker

![Girl Develop It Logo](../images/metageek.jpeg)

@@@

###What we will cover today

* Python? You mean a snake? <!-- .element: class="fragment" -->
* Why programming? <!-- .element: class="fragment" -->
* Variables and arithmetic <!-- .element: class="fragment" -->
* Statements and Error Messages <!-- .element: class="fragment" -->
* Development Environment Setup <!-- .element: class="fragment" -->
* Boolean Expressions and Conditionals <!-- .element: class="fragment" -->
* Loops <!-- .element: class="fragment" -->
@@@

###Python? A snake?

![Girl Develop It Logo](../images/slytherin.png)

* Suitable for beginners, yet used by professionals
* Readable, maintainable code
* Used by Disney, NASA, Google, Dropbox
Note: Block 1 begins - 25 minutes
@@@

###What is Python used for?

* System Administration (Fabric, Salt, Ansible)
* 3D animation and image editing (Maya, Blender, Gimp)
* Scientific computing (numpy, scipy)
* Web development (Django, Flask)
* Game Development (Civilization 4, EVE Online)
@@@


###Why programming?</h3>

* Need to tell computer what to do.

![Girl Develop It Logo](../images/nbody.jpeg) ![Girl Develop It Logo](../images/nbody_simulation.jpeg)

"Computer, simulate the motion of N heavenly bodies, subject to Newton's laws of motion and gravity."
@@@


###Let's Develop It

Let's setup our computer for Python programming

* Locate and run the terminal program. Type 'python' and hit enter.

![Girl Develop It Logo](../images/computer_kitten.jpeg)

@@@

###Working in the Python Shell

Open up your terminal and type 'python' <!-- .element class="left-align" -->

* Type 'python' to start the interpreter. <!-- .element class="fragment" -->
* Feel free to explore as well. <!-- .element class="fragment" -->
* Type exit() to leave python. <!-- .element class="fragment" -->

@@@

###Variables and Arithmetic
```python
>>> 3 + 4
7
>>> 2 * 4
8
>>> 6 - 2
4
>>> 4 / 2
2
```
```python
>>> a = 2
>>> print a
2
>>> b = 3
>>> c = a + b
>>> print c
5
```
```python
>>> a = 0
>>> a = a + .5
>>> print a
0.5
```
@@@

###Strings
```python
>>> a = "Hello "
>>> b = "World"
>>> c = a + b
>>> print c
'Hello World'
```
```python
>>> a = "Spam "
>>> b = a * 4
>>> print b
"Spam Spam Spam Spam"
```
@@@

###Data types
* Variables are names of objects <!-- .element class="fragment" -->
* Objects always have a "type" <!-- .element class="fragment" -->
* The type can be found using: type() <!-- .element class="fragment" -->

```python
>>> print type(4)
<type 'int'>
>>> a = 4
>>> print type(a)
<type 'int'>
>>> print type("But I don't like spam")
<type 'str'>
>>> print type(3.5)
<type 'float'>
```
@@@

###Data types - continued ...
* Objects can be used with a set of operators <!-- .element class="fragment" -->
* An int or float can be used with any of: +, -, *, / <!-- .element class="fragment" -->
* A string can be used with any of: +, * <!-- .element class="fragment" -->
* What happens if we try to use division or subtraction with a string? <!-- .element class="fragment" -->

```python
>>> print "Spam" / "eggs"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```
@@@


###Errors

* There are different kinds of errors that can occur. We've seen a few of these so far
* Some other examples are the TypeError and NameError exceptions. 

```python
# SyntaxError - Doesn't conform to the rules of Python.
# This statement isn't meaningful to the computer
>>> 4spam)eggs(garbage) + 10

# NameError - Using a name that hasn't been defined yet.
>>> a = 5
>>> print b

# TypeError - Using an object in a way that its type does not support
>>> 'string1' / 'string2'
```
@@@

###Let's Develop It
* We'll practice what we've learned in the shell
* Sam, Sally, Steve, Susan, Sarah are students. They are 19, 20, 25, 50, 15. Find the average age of the students. 

Note: Let's develop it: 30 minutes.
@@@

###Using the terminal
Try each of the following commands in turn:

Command | Windows Command        | Short for               | Description 
----------------|--------------|---------------|---------------------------------------
ls              | dir  |  List       | Displays the files and folders in the current folder
cd <folder>     | cd <folder> | Change Directory        | Change to another folder, where <folder> is the target
mkdir <folder> | mkdir <folder> | Create Directory | Create a new folder, where <folder> is the name
Note: Block 3 begins, 30 minutes
@@@

###Creating a folder
We need a folder to save and run our code from.

($ shows the shell prompt where commands are entered.)
```bash
$ mkdir gdipython
$ cd gdipython
```
@@@

###The Text Editor
Open sublime text.

* Click File, then Open folder. Navigate to the gdipython folder we created and click "open"
* In the text editor, enter the following:

```python
print 'This is a Python program'
```

* Click file, save as. Type 'program.py' . Select the gdipython directory you just created. Click ok.

Open a terminal and type

```bash
$ cd gdipython
$ python program.py
```

You should see the terminal print:

`This is a Python program`
@@@

###Dessert Item
![Girl Develop It Logo](../images/cat_cake.jpeg)

@@@

###Dessert Item: User Input

To obtain user input, use 'raw_input()'. This will become a string

We use float() to make it a number

Change the program.py text to the following and run it again

```python
input_value = raw_input("Enter a radius:")
radius = float(input_value)
area = 3.14159 * radius * radius
print "The area of a circle with radius", input_value, "is", area
```
@@@

###Let's Develop It
On average, water accounts for 54% of the weight of a person. Write a program which takes a person's weight as an input and calculates how much of that weight is from water. 
 

You can use float() or int() to treat the input as a number if you need a number, or you can use the input directly if you need a string

Note: Let's develop it: 15 minutes
@@@


###Boolean Expressions
We can tell the computer to compare values and return True or False. These are called *Boolean expressions*

* Test for equality by using ==. (This is not the same as using =)
* Test for greater than and less than using > and <

```python
>>> a = 5
>>> b = 5
>>> print a == b
True
>>> print a < 3
False
>>> # Combine comparison and assignment
>>> c = a == b
>>> print c
True
```

Note: Block 1 - 25 Minutes
@@@

###Boolean Expressions continued

Expression | Tests
-----------|-----------------
a == b     | a is equal to b
a != b     | a does not equal b
a < b      | a is less than b
a > b      | a is greater than b
a <= b     | a is less than or equal to b
a >= b     | a is greater than or equal to b

@@@

###Boolean Expressions continued

```python
>>> a = 3
>>> b = 4
>>> print a != b
True
>>> print a <= 3
True
>>> print a >= 4
False
```
@@@

###Conditionals

When we want different code to execute dependending on certain criteria, we use a **conditional**
We achieve this using **if** statements

```python
age = 25
if age == 25:
    print "Marianna's age is equal to 25"
```
We often want a different block to execute if the statement is false. This can be accomplished using **else*

```python
age = 25
if age == 25:
    print "Marianna's age is equal to 25"
else:
    print "Marianna's age is not equal to 25"
```
@@@

###Indentation

In Python, **blocks** begin when text is indented and ends when it returns to the previous indentation level.

```python
age = 25
if age == 25:
    print "Marianna's age is equal to 25"
    a = 1
    print "Still in the age == 25 block"
else:
    print "Marianna's age is not equal to 25"
    a = 2
print 'Outside of the if or else blocks. This will run regardless of the value of x'
print "Value of a is ", a
```
@@@

###Chained conditionals
Conditionals can also be **chained**

Chained conditionals use **elif** as an additonal check after the preceeding `if` predicate was False.

```python
age = 25
if age > 25:
    print "Marianna's age is greater than 25"
elif age < 25:
    print "Marianna's age is less than 25"
else:
    print "Marianna's age is equal to 25"
```
@@@

###Let's Develop It
Write a program that uses if statements to determine what to do given some user input

The code below is an example:

```python
health = 100
print "A vicious wolf is chasing you."
print "Options:"
print "1 - Hide in the cave."
print "2 - Climb a tree."
input_value = raw_input("Enter choice:")
if input_value == '1':
    print 'You hide in a cave.'
    print 'The wolf finds you and injures your leg with its claws'
    health = health - 10
elif input_value == '2':
    print 'You climb a tree.'
    print 'The wolf eventually looses interest and wanders off'
print "Game under construction. Come back later"
```
Note: Let's develop it: 15 minutes
@@@

###Making a sign-up sheet
![Girl Develop It Logo](../images/sign-up-sheet.jpg)

```python
print "1"
print "2"
...
print "10"
```

@@@

###Making a sign-up sheet - now do this for 100!

```python
print "1"
print "2"
...
print "99"
print "100"
```

@@@

###Making a sign up sheet: Iteration

```python
num = 1
while num <= 10:
    print num
    num = num + 1
print 'Done'
```

@@@

###While loops continued 

A loop can also terminate at any point with a **break** statement

An infinite loop can be created using an expression that is always True.

```python
while True:
    name = raw_input("What is your name (type 'quit' to quit)? ")
    if name == 'quit':
        break
    print "Hello,", name
```
@@@


###Dessert Item
![Girl Develop It Logo](../images/cat_cake.jpeg)

@@@

###Dessert Item: ATM
* Develop a program for a bank ATM. An ATM can have three options: (1) deposit, (2) withdraw, (3) quit.
* Deposit option takes in a number from a user using raw_input() and adds it to the current balance.
* Withdraw option takes in a number from a user using raw_input() and subtracts it from the current balance.
* Quit option exits the program.

* Hint:

```python
balance = 0
while True:
    prompt = "Enter a number for one of options: (1) deposit, (2) withdraw, (3) quit"
    input_value = raw_input(prompt)
    option = int(input_value)
    if (option == 1):
    ... (put more code here) ...
print "Your final balance is", balance
```

Note: Let's Develop It - 15 minutes
@@@

###Questions?
