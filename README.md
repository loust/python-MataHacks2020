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
2. [Conditional Statements](#conditional-statements)
3. [Loops](#loops)
4. [String Manipulation and Output](#string-manipulation-and-output)
5. [File read and write](#file-read-and-write)
6. [Reading Error Messages](#reading-error-messages)

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

## Conditional Statements
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
