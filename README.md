![logo](res/python1_MATAHACK.png)

# Beginner Python MataHacks
This workshop will go over the basics of python showing the syntax by utilizing the ideas of general programming.

# Content

* [Beginner](#Beginner)
0. [Setup and Requirements](#setup-and-requirements)
    * [Linux / Mac](#linux-mac)
1. [The Syntax](#the-syntax)
    * [Comments](#comments)
    * [Basic Hello World](#basic-hello-world)
2. [Data Types and Conditional Statements](#data-types-and-conditional-statements)
3. [Loops and Iterations](#loops-and-iterations)
4. [File Read and Write](#file-read-and-write)

# Beginner

# Setup and Requirements
## Windows
For Windows, it is suggested to use Anaconda to keep things easier. Anaconda manages to keep your python installs in different environments, thus, you can control several python versions at once without the hassle. https://www.anaconda.com/products/individual

After installation, you can open Anaconda, head to __Environments__ and create a new environment by clicking the [+] button called __Create__. Then, you can specify what version of Python you want to use. Afterwards, you can select that environment that you created and launch it by pressing the green play button next to its name, thus, launching a command prompt, giving you access to a fresh installation of Python3. If you have installed other libraries, it will not show up here.

## Linux / Mac
The *nix based python management is simpler, as you only need to install the package from the package management system, and then creating environments from there, though, we do not care about creating environments in this workshop. But, if you wish to creat environemtns in Linux, you can install `virtualenv`

```bash
python3 -m pip install --user virtualenv
```
Then, you can create new environments:
```bash
python3 -m venv new_environment_name
```

And, to activate it, you need to use the `source` command. What the previous command did was, it created a new directory called `new_environment_name` and it has sub directories inside of it. One of which is called /bin, which is where the activation binaries are located. This basically acts like a new instance of python, so it will not touch your already-existing libraries.

```bash
source new_environment_name/bin/activate
```

Now, you will see the environment name show up in parentheses on the left side of your shell.

For Macs, it should be similar, but if you want, you can also download Anaconda for Macs, to make the job easier.

# The Syntax
There are several things to keep in mind when you are working with Python. First, is the fact that you are using Python3, and not Python2, since Python2 is considered old by now. Some applications still use Python2, and there has not been any transfers yet. You probably will have Python2 installed under "python" and Python3 under "python3"

Before we begin, to avoid writing messy code, you should skim through, or read the Python PEP8: https://www.python.org/dev/peps/pep-0008/ this will ensure that you do not mess up the beauty if your code. It will lessen the amount of comments you use as your code becomes more readable.

As we observe the document, they state that spaces are preferred method. You need to use a text editor that does the indentation automatically to avoid manual entry of spaces or tabs to indent, which will cause errors to occur.

## Comments
Comments are done using the pound sign `#` and tripple double quotes: `"""` For example:
```python
# This is a comment

"""
This is a longer
Comment
"""
```
## Basic Hello World
Let's go over basic hello world examples and end up with string manipulations:

```python
print("Hello World!")
```
Outputs:
```bash
Hello World
```

```python
variable1 = "Hello"
variable2 = "World!"

print(variable1 + " " + variable2)
```

Output:
```bash
Hello World!
```
The above is the old way of appending strings together

```python
var1 = "Hello"
var2 = "World!"

print(var1, " ", var2)
```
Output:
```bash
Hello   World!
```
Note that, the comma `,` separations will add spaces.

```python
var1 = "Hello"
var2 = "World!"

print("{first} {second}".format(
        first=var1,
        second=var2
))

print("{} {}".format(
        var1,
        var2
))

print(f"{var1} {var2}")
```

Output:
```bash
Hello World!
Hello World!
Hello World!
```

# Data Types and Conditional StatementsG
Everything in Python are objects, so, if an object is empty, it contains the "object" __None__. None, is very important in conditionals, making things simpler when you are checking for passed objects from another function.

To show this example, let us introduce lists. Lists are like Arrays, but in Python it is called a __List__. It starts with brackets: `[]` and contains integers or strings or other objects:
```
[1, 2, 3]
["1", "2", "3"]
[object1, object2, object3]
[{},{},{}]
```

Oh, and there are also dictionaries. Dictionaries are encapsulated with braces `{}` this is similar to a JSON object, but it is called a list. There is no restriction in using single quotes or double quotes, as JSON requires double quotes.

```python
{
    "name":"yourname here",
    "age": 51,
    "school": "CSUN",
    "items": [1,2,3,4,5],
    "another_object":[
        {
            "liked":234,
            "name":"Heavenly item"
        },
        {
            "liked":255,
            "name":"Limited burger"
        }
    ]
}
```

```python
some_object = [1,2,3]
some_other_object = []

if some_object:
    print("This will show")

if some_other_object:
    print("This will NOT show")
```

Output:
```
This will show
```

The reason the one called "This will NOT show" did not display is because we checked if the item was empty or not. This is the correct way to check if an item is empty or not. By checking if it is __None__ or has items in it.

Let's see what these items are:
```python
some_object = [1,2,3]
some_other_object = []

print(type(some_object))
print(type(some_other_object))
```
Output:
```bash
<class 'list'>
<class 'list'>
```

Note, that it will show up as a list and not as __None__ is because the type is a list, but since it is empty, it is considered a __None__

If you set
```python
testing = None

print(type(testing))
```
Output:
```
<class 'NoneType'>
```

More on conditionals, we can use negated statements, such as "if not this"
```python
mandatory_list = []

if not mandatory_list:
    print("Ready and empty")
```
Output:
```
Ready and empty
```

The reason this worked is because the list returned true on the fact that it is a None. Since we negatively checked a None objected list, it matched and returned.
Let's dive into and and or statements in conditional if statements:

```python
var1 = []
var2 = [1,2,3]
var3 = [2,3,4]

if var1 and var2 and var3:
    print("all variables have contents")

if var1 or var2 or var3:
    print("some variables have contents")
```

You should run this and see what happens

Equalities are matched with `is`, `in` or `==`. The latter is used if the equation is being matched with a string specifically

```python
var1 = 1
var2 = 2
var11 = 1

if var1 is var11:
    print(1)

if var1 == var11:
    print(1)

if var1 in var11:
    print(1)
```

Now, run this and see what happens? When does the error happen and what does it mean?o

Let's move on to Loops and iterations, hence the error is related.

# Loops and Iterations
The error above mentions that the type `int` is not __iterable__, now this occurs because iteration means that you are looping through a certain type of data, for example ,we looked over lists. Lists can have multiple lists inside of them, or multiple dictionaries inside of them as well. So, for example, if let's say you have a list of numbers and you want to go through them one by one to make sure they are all accounted for, you would do something like this:

```python
my_list = [1,4,65,2,234,5,234,234,32]

for item in my_list:
    print(f"my current number is {item}\n")
```

Run this and see what happens. Now, you'd raise a question, if you know languages like C, they use indexes. Python does not really require indexes, however, you CAN enable it by doing so:

```python
my_list = [1,4,65,2,234,5,234,234,32]

for id,dx in enumerate(my_list):
    print(f"Current item: {id} has the value of {dx}")
```

Run this and see what returns


Now, let's do something odd and stop the loop in the middle as it finds a specific value:

```python
my_list = [1,4,65,2,234,5,234,234,32]

for item in my_list:
    if item is 234:
        print("Found!")
        break
```

There are more things like this, `continue` will not END the function but will stop the loop for example, however, `return` will END your function. Speaking of functions, we will cover it after the while loop.

Note that, we do not have switch / cases in Python.

```python
my_list = [1,2,3,4,5,6,7,8,9]

while(True):
    for item in my_list:
        if item is 7:
            return
```

Run this and see what happens.

Finally, let's do some text animation!
```python
import itertools
import sys
anim = ['-','\\','|','/']
rr = itertools.cycle(anim)

my_list = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]

for item in my_list:
    sys.stdout.write("[{anim}] Some nice text animation    \t\r".format(
        anim=next(rr)
    ))
    sys.stdout.flush()
```

Looping through a dictionary is the same thing, but you will now need to utilize the names of the dictionary keys to get their values.
Dictionaries are of the following sort:
```json
{
    "key":"value"
}
```

In python, there's a .keys() function that can be used against dictionary objects and .values() function.
In this case, let's look at the dat aprovided below:

```python
{
    "name":"yourname here",
    "age": 51,
    "school": "CSUN",
    "items": [1,2,3,4,5],
    "another_object":[
        {
            "liked":234,
            "name":"Heavenly item"
        },
        {
            "liked":255,
            "name":"Limited burger"
        }
    ]
}
```

For example, if we wish to grab the liked names from the object "another_object" which is a list that contains two dictionaries, we would do the following:

```python
for item in mydict.get('another_object'):
    print(item.get('liked'))
```

NOTE: You can also do this as the following:
```python
for item in mydict.['another_object']:
    print(item['liked'])
```
It's just that, if you are looping throuhg some data, and some data has the key "another_object" and some does not have the key "another_object" your program will crash. Thus, using .get() will return a None object in the case that some data does not exist that you are trying to get something from.

You can read the documentation on itertools and discover newer things! https://docs.python.org/3/library/itertools.html
Reading documentation is very important and the best thing you can do to figure out how to utilize the library you imported fully. We will talk about more about this in the Intermediate section.

# File Read and Write
I will go over this very simply, you can read files and write to files with simple commands, but the most easy way to do this (without closing the file) is using the `with` functionality

```python
with open("filename.txt", 'r') as f:
    temporaryvar = f.readlines()
```

This will read ALL the lines, it will include `\n\r` as well. We do not need that, so instead, we can use the following function:

You can do
```python
temporaryvar = f.read().splitlines()
```

This will read the lines, but without the newlines `\n\r`

To write to a file, we need to __Append__, so we use the `a` instead of `r` (for Read)

```python
with open("newfile.txt", 'a') as f:
    f.write("your text here :) \n")
```

Remember to have a new line character `\n` at the end of your written string though.


Note, the beginner part is missing functions. We will talk about them in the intermediate area.
