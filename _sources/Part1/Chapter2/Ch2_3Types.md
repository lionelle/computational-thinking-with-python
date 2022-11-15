---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# 2.3 Types

In programming, data has types, and that is because data to the computer is all numbers (ones and zeros). A type helps the computer determine how to handle the data, and helps your program use predefined concepts about that information.  

## Types

In the first chapter, we introduced three types of data that you will work with in your programs. Two of the types are numerical fixed values, while the third type is string sequential value. They are `int`, `float`, and `str`. What does that exactly mean for each?

* **int**: A whole number (no decimal)  
* **float**: a floating point number (has a decimal)
* **str**: a sequence of characters in order - essentially words but also includes special characters, numbers, etc

```{note}
You can use the `type()` function to see the type.
```

```{code-cell}
x = 11  
print(x)
print(type(x))
```
```{margin} Class?
You may be wonder what the `<class>` part is about. They are covered in part 2 of this book, and are a way for someone to define their own types. 
```

Adding a .0 to the 11 would make it a `float`
 

```{code-cell}
x = 11.0
print(x)
print(type(x))
```

Also, if you perform a division operation, and int will become a float!

```{code-cell}
x = 10
print(type(x))
z = x / 2
print(type(z))
print(z)
```

While this isn't a case to require an int, you could convert it back to int by using the `int()`.

```{code-cell}
x = 10
print(type(x))
z = int(x / 2)
print(type(z))
print(z) 
```
Notice the 5.0 turned to 5!

What would happen do you think if we did all the above, but with x put to 11?

```{code-cell}
x = 11
print(type(x))
z = int(x / 2)
print(type(z))
print(z) 
```
It *truncates* the value, meaning whatever is after the decimal point is removed. 

```{admonition} This is nice but...
:class: important
This is nice, but you may be thinking where will this matter. We will get to that, as with many algorithms we want whole numbers specifically. 
```

## Introducing Boolean (bool)

Computers are binary machines, meaning they "yes" or "no", "on" or "off", or more commonly stated as "1" or "0". This is called a {term}`Boolean` value. In python, we use boolean values all the time, as the words `True` and `False`.

For example:

```{code-cell}
value = True
print(value)

value = False
print(value)
```

````{important}
Case matters! `True` is valid, true is a variable name in python, so if you write the following code you would get an error
```python
value = true
print(true)
```

This is an extremely common error when you were working with multiple languages, as in other languages it can be lowercase true. 
````

This type in python is called the `bool` type, and like `int` and `float` you can convert a string or other value to a boolean. 

```{code-cell}
value = bool("True")
print(value)

value = bool(0)
print(value)
```
However, for the most part you rarely need to convert except for reading in data from a file or client. Instead, you either simply type True or False or you end up using conditional operators, covered in the next section!

### Types Covered Review

As a reminder, here are the various types we have covered.

| Type | Name | Description |  Example Code |
| :-- | :-- | :-- |  :--: |
| int | Integer | Whole number values (no decimal) |  `x = 10` |
| float | Float | Floating point numbers (has decimal) | `x = 2.5` |
| str | String | Sequence series of characters | `name = "Ada"` |
| bool | Boolean | Binary type, of True and False | `answer = True` |




## Type Hints for Functions

While including the type of the value is not required in python, it is industry standard to include "type hints" when dealing with functions. These hints are written in the format

```text
parameter: type
```

For example, If we had a function that needs an int to work, we would write

```python
def my_func(value : int):
    # do something
    # returns nothing
```

You can also add a return value by adding the `-> type` before the colon at the end 

```python
def my_fund2(value : int, pi : float, name : str) -> str:
    #takes in three arguments
    #returns a string
```

This does multiple things.

1. Follows industry standard
2. Allows type checking programs to double check your code for you
3. Allows auto code completion utilities to help with docstring
4. Most importantly, helps you to see exactly what is needed for each function without reading the full details!


````{note}
You can also use `None` to indicate nothing is being returned. For example
```python
def my_func(value : int) -> None:
    # do something
    # returns nothing
```
````

Whenever you write a function, you should follow these four steps:

* define
* document
* implement
* test

In the **define** stage, if we set our types for the function, we will have a clearer image going into all stages! For the rest of this book, we will include type hints in our example code. 

````{admonition} Thinking Deeper - Statically Typed vs. Dynamically Typed
:class: Note

Sometimes these types are explicit in languages such as java, c, c++, and these are called {term}`Statically Typed` languages. Meaning your code must only store that specific type in a variable. 

In java for example 
```java
int x = 10;
x = "Hello";
```
The code above is invalid, it would throw a syntax error when you compiled the program (even before you ran it!). 

However, python is a {term}`Dynamically Typed` which means the variable types are determined at run time, and they may even change during the execution of program.  

In python, this is valid code
```python
x = 10
x = "Hello"
```

The variable x is first a number and then it is a string! This has advantages and disadvantages. To the programmer, we don't have to worry about adding types for every line of our program. It, however, can introduce runtime errors! 

While Dynamic vs Static typing is a common argument among language designers, what you need need to know now is **be careful**. Make sure you document, and define exactly what is expected and going on. This is especially true when dealing with function parameters. Identify what they are, so you know when you call the function both what it needs to work and what to expect on the return. 

````

Now having a better understanding of types, and having introduced the Boolean type, we can talk about Conditional Statements!