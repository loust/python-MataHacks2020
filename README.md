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

* [Intermediate](#Intermediate)
1. [Library Project Structure](#library-project-structure)
2. [GET and POST requests for API connections](#get-and-post-requests-for-api-connections)
3. [sqlite3 connections and integration](#sqlite3-connections-and-integration)

* [Advanced](#advanced)
1. [Multithreading](#multithreading)
2. [Multiprocessing](#multiprocessing)
3. [Exception Management](#exception-management)

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

# Intermediate

## Library Project Structure
Usually, when you write a simple script, it's just your python file that does the job, you're going to be running it as follows:
```bash
python3 ./myscript.py
```

And in a lot of times, you will see yourself re-writing your scripts all over again. Instead, you can make your own library of most-used functions and scripts to reuse them in other places as well. This will go over the basic sctructure of a Python class and a custom library.

The types of files and folders that you will find in a python library will be similar to this:

```
<Project_name>
    - __init__.py
    - __main__.py
    - project_name.py
    - custom_lib_1.py
    - custom_lib_2.py
```

So, this is a VERY basic class structure. It does not have any folders, but you can add them on later. Though, in this case, we have files like __init__ and __main__ that can be left blank for now.
The `project_name.py` is the one you will use as the main interface for your two custom libraries on the side.

Look at the folder `Project_name` in this repo to see the simple structure of it.

Now, we can run the following to see where python is installed

```python
import sys
print(sys.path)
```

Run the above command to see where you should put that project directory that you created. Then, this will allow you to use this library of functions in any other codebase.

Usually, it's in the user's home directory in .local: `~/.local/lib/python3.X/site-packages` This directory is good enough for debugging. After your library is ready for release, you can package it with pip after approval, but this workshop will not cover that.

# GET and POST requests for API connections
Doing GET and POST requests are very conventional, though, there are two ways of doing it. One is just directly calling a GET function with the `requests` library, and the other is to create a session with the `requests` library. To keep it more convenient, this workshop will only show the session creation to keep things stable.

NOTE: You can get every information about `requests` from their documentation: https://requests.readthedocs.io/en/master/user/advanced/

Here are the quick and dirty noites on how to get a session up and maintain it:

```python
import getpass
s = requests.Session() # Create a session

# The headers will be updated. Let's say an API requires that you send them a specific header value,
# This is used there.
s.headers.update(
    {
            "Content-Type": "text/html"
    }
)

username = input("Enter your username: ")
password = getpass.getpass(prompt="Enter the Password: ")

s.auth = (username, password) # Remember to always hide the password, and make it an input

# Note, if you need to save the password somewhere, the best place to put it is outside of the script itself,
a database would be good. Encrypted databases would be better. API Integration in the OS itself would be ideal.

result = s.get("https://contenthere")
```

The same thing can be said for POST requests. Instead of .get() you can use .post(), but for POST, you need to send in data, and the way you do this is to append data as you did to headers

From an example from

```python
from requests import Request, Session

s = Session()

req = Request('POST', url, data=data, headers=headers)
prepped = req.prepare()

# do something with prepped.body
prepped.body = 'No, I want exactly this as the body.'

# do something with prepped.headers
del prepped.headers['Content-Type']

resp = s.send(prepped,
    stream=stream,
    verify=verify,
    proxies=proxies,
    cert=cert,
    timeout=timeout
)

print(resp.status_code)
```


Let's head to http://dummy.restapiexample.com/ and try to grab some data from there.

Try to do GET requests of this URL: http://dummy.restapiexample.com/api/v1/employee/1
You may get 429, but you can keep trying.
You will get the following:
```json
{"status":"success","data":{"id":1,"employee_name":"Tiger Nixon","employee_salary":320800,"employee_age":61,"profile_image":""},"message":"Successfully! Record has been fetched."}
```

Now, to move on to the following, let's add these values to a SQL database using `sqlite3`

# sqlite3 connections and integration
You can view my other repository, which includes some sample SQL commands, but regardless, here is a quick note on how to connect to the sqlite3 engine from Python to add or get information:

```python
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

with sqlite3.connect('database.db') as con:
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute("SELECT * FROM tablename")
    cur.commit() # Commit is mostly used when you change something in the Database, not SELECT
    item = cur.fetchone() # You can also use fetchall()
```
Notice the dict_factory, this function overwrites how the sqlite3 outputs data. Instead of outputting it as a list without any keys, it converts it to a dictionary, making it easier to get items if you are dealing with a lot of data.

Note that, alternatively, you can leave things in the memory instead of creating a file for the database. This is done via:

```python
import sqlite3

with sqlite3.connect(':memory:') as con:
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute("SELECT * FROM tablename")
    item = cur.fetchone() # You can also use fetchall()
```
# Advanced

## Multithreading
This is related to functions that are network based. So, when you are developing some application that is a downloader, which downloads images from several URLs, using threading would download things in parallel theoretically.

We will discus the concurrent futures ThreadPoolExecutor features instead of using the threading library itself. This is simpler to visualize and organize.

Here is a snippet from the documentation found here: https://docs.python.org/3/library/concurrent.futures.html

```python
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
```

The most important thing to take out of this is the following:
```python
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
```
The above line creates a threading pool. Think about it as a controller that rallies "workers" by assigning them your function
Notice above that the function `def load_url` is loading a URL with a variable integer of a timeout. This is passed by in the threading area.

Notice that the example is a bit confusing if you have not done single line for loops. Single line for loops look like this:

```python
variable = [item for item in items]
```
This is similar to doing the following:
```python
variable = []
for item in items:
    variable.append(item)
```

Notice the `[]` brackets outside of the single line for loop after the equation.
Now, in this example, they assign the function of `load_url` directly with a single line loop as follows:
```python
future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
```
Another thing to mention is the `executor.submit` function. There is an `executor.map` as well. The difference is that, `submit` schedules the callable function to be executed, and returns a __Futures__ object. The `map` collects the iterables immediately in addition to the function being executed asynchronously.

In another way, you could have done it this way:
```python
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url_1 = executor.submit(load_url, 'https://google.com/', 60)
    future_to_url_2 = executor.submit(load_url, 'https://yahoo.com/', 60)
```

Notice how the function `load_url` has two parameters as `URL and TIMEOUT`. When you call the function `executor.submit` you are passing the function `load_url` without the `()`s thus, you need to put the function's parameteres right next to it.


So, the idea of multithreading and processing is that, you create a function to do your job, you pass it to the PoolExecutor, which assigns workers and then, runs them in parallel.

To debug your program and see if your process is saving time, you can do the following before and after you run your code:

```python
import time

t1 = time.perf_counter()

# ... Do some work here

t2 = time.perf_counter()

print(f"Finished! Time took: {t2-t1}")
```
Note, alternatively, there is another library called threading, you can see an example here from this stackoverflow: https://stackoverflow.com/questions/47995566/threadpoolexecutor-vs-threading-thread
It is a bit similar in ideology, but the PoolExecutor version does this in less lines of code.

## Multiprocessing
This is related to functions that are CPU based. Note, that we will be using the same futures' technique, which means it's in the same documentation: https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor

This means that, the code will look very similar, you do not need to learn two different libraries. The ProcessPoolExecutor utilizes the `multiprocessing` module and simplifies the writing and creating parallel processing scripts.

Remember, multi processing is for, for example, copying mass amount of files, calculating primes, doing complex jobs that requires CPU

As a side note, if you want to do things via GPU, you cannot run these multiprocessing methods using GPU code. In this case, you will need to look into this: https://documen.tician.de/pycuda/

Regardless, let's get into multiprocessing with a simple example, and examine how similar the structure is:

```python
import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main()
```
Now, we don't really mind the function itself, but in this case, it's a prime function. So, what the important part here is this line:
```python
with concurrent.futures.ProcessPoolExecutor() as executor:
```
This line utilizes the `ProcessPoolExecutor` with no workers. However, you can give workers as follows:
```python
ProcessPoolExecutor(max_workers=3)
```

Now, if we look into the following for loop that they create, we see that they use the `zip()` function in the loop.
The `zip()` function is used for parallel iteration, so, it will go through both objects in parallel (at the same time)

The way this happens, is that, your CPU cannot operate in parallel technically. So, in computers, parallel means that it executes one thing, then moves to another function, executes that, then comes back to the original function. This continues on, and visually, we see them working in parallel together. This is generally what multiprocessing and multithreading does.


Notice how the `executor.map` is being called instead of `executor.submit` As a challenge, you should change this to `executor.submit` and see what the differences are by using the time calculations. However, as stated in the documentation and above, the `executor.map` is for asynchronous execution.

## Exception management
So, let's head over to this website: https://www.programiz.com/python-programming/exceptions

Scroll down a bit, and you will see the bolded title called __Python Built-in Exceptions__ We are just looking at this for now. You can read the entire thing and learn from there, but I will summarize most of the exception handling here:

Exceptions are basically the "catching" of errors instead of getting your program to crash. We can do this using the `try` and `except` feature in Python.

```python
try:
    # Some code here that is bound to break
except:
    # error message output
```
Now, you can customize the error output message, which is the goal of this topic, for example:
```python
try:
    # Some bad workarounds here
except as e:
    print(e"The error was due to {e}")
```


Now, if you look at the article, we can see that there are some more exception values. We used `e` earlier as a parameter for the error passing in. This means, there are different types of errors in Python, and you can catch all of them. Even custom error exceptions in custom libraries.

Let's go over the `KeyboardInterrupt` exception handler and catch the Ctrl+C.

```python
import time
a = [1,2,3,4,5,6,7,8,9]
for item in a:
    try:
        print(item)
        time.sleep(5)
    except KeyboardInterrupt as e:
        print(f"skipped {e}")
```

This will continue on the for loop, but whenever you hit the Ctrl+C, it will NOT kill the entire program! It will ONLY skip the current number in the loop as you see it for yourself. Run this and try it ou!

In addition to exceptions, you can use multiple exception handlers. You can use another `except` under another. And you can end it with `else` for the final

For example, you can do something like this. Let's say you're downloading something and saving it to a file.

```python
try:
    # code to download something
    # code to save something to a file
except (URLError, ValueError):
    # handle it here
except SocketTimeout:
    # Upon a socket timeout, what should we do?
except OSError:
    # OS related error. Is the file not found? Not created?
else:
    In the end, something else happened. What do we do here?
```


There are several other ways to stop or ignore exceptions, such as:
```python
try:
    # go through a look, I don't care if it misses anything or errors out
except:
    pass
```

`pass` is used to not output anything and continue. Similar to `conitnue` or `break`, but it basically follows the process normally, ignoring the exception text output without leaving the `except` blank, since t hat will result in an error.

These were built-in exceptions from Python. Let's say you're using the `reuests` module, and want to see what they exceptions are:
Let's check out their documentation: https://requests.readthedocs.io/en/master/_modules/requests/exceptions/

Let's say there's a requests exception, you can use it as follows:
```python
import requests
try:
    # Do something with requests
except requests.RequestsException as e:
    # Output a message
```
