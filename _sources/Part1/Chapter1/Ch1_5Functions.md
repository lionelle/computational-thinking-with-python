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

# 1.5 Functions

Writing code line by line is fine, but wouldn't it be a pain to always have to redo/retype stuff that is done? Also, it makes it difficult to isolate and test various tasks. Let's take the name example. Instead of just asking one person's age, maybe I am building a two player game that needs to ask all that four times. As such the code could be. 

```{code-block}
print("Player 1")
born_year_str = input("What year were you born in? ")
born_year = int(born_year_str)
current_year_str = input("What year is it currently? ")
current_year = int(current_year_str)
age = current_year - born_year
print(f"My age in {current_year} is {age}.")

print("Player 2")
born_year_str = input("What year were you born in? ")
born_year = int(born_year_str)
current_year_str = input("What year is it currently? ")
current_year = int(current_year_str)
age = current_year - born_year
print(f"My age in {current_year} is {age}.")
```

Wait, I meant to say "Player age". Ok, I only need to change that twice. What if we made it a four player game? What if we wanted it optional on the number of players? Now it starts getting complicated. 

Enter the generation of reusable code of using a {term}`Function`. While the use of reusable code was built up through multiple groups, we often thank the ENIAC Women [ref](https://spectrum.ieee.org/untold-history-of-ai-invisible-woman-programmed-americas-first-electronic-computer), [ref2](https://www.codecademy.com/resources/blog/eniac-six-women-programmed-computer/) who focused on developing reusable blocks that could be used on different projects. They also developed many of the sorts and algorithms we use today. However, [LISP](https://en.wikipedia.org/wiki/Lisp_(programming_language)) was the first functional programming language developed by [John McCarthy](https://en.wikipedia.org/wiki/John_McCarthy_(computer_scientist)) in 1958.

The idea behind functions is that you have a block of code, that 
1. Can be repeated
2. Can take in parameters 
3. Can return a value to be used

A {term}`Parameter` is a value that gets passed into the function. It ends up becoming a variable that can be used. A return value is a value that gets passed out of the function. You have already been using both!

## Built-In Functions 

You currently have already been using a few of Pythons built in functions. These functions someone else wrote, and you are given access to call the function (often called {term}`Invoke`) when you need to use its capabilities. We don't care how it works, just that it works as intended! Here are a few you have used.

````{margin} 
  ```{admonition} None
    :class: note
    None is a keyword/type in python that means nothing or not defined. We will end up using
    it a lot, but for now, just know, like everything in this book, we will come back to the concept.
  ```
````
`print(value) -> None`
  : You call this function to print the value to the screen. Value has been a variety of things, but every time you have "passed" in a value to the function. This value is the parameter for print to work. We say it returns `None` meaning there is nothing actually returned to store in a variable after the function is executed.

`input(value) -> str`
  : input function takes in an (optional) value, that prints to the screen you want the message to read. However, when you used input, you set it to a variable. When you did this, what you were really doing was setting the value **returned** to the variable. In the following example `quest` ends up being assigned the string value returned from the input function, which is the value someone types into the keyboard. 
    ```{code-block}
    quest = input("What is your quest? ")
    ```

`int(value) -> int`
  : the int function converts a string to an int value, so you can  perform mathematical operations. As such the parameter is a string, and it returns an int as long as the string matches a whole number style format. For example: `int("11")` would work, `int("11.5")` would cause an error.

`float(value) -> float`
  : A float is short for floating point number or decimal. The float function takes in a string that looks like a float, and converts it to a floating point value so you can perform mathematical functions. For float, *any* valid number  works fine, as you can also add a .0 to a whole number.  


All four of these functions were written by someone else, so you don't have to write the code yourself. However, the real power of programming comes down to the ability for you to write your *own* functions!

## Writing Functions

A function in python has various parts. The basic format of a function is as follows:

```python
def name(parameters):  
  """docstring"""
  #do something cool
  return value
```

For example:
```{code-cell}  
  def says(animal, sound):
    return f"The {animal} says {sound}."

  cat_says = says("cat", "meow")
  dog_says = says("dog", "woof")
  print(cat_says)
  print(dog_says)
```


def name
  : starting a line off with def, means define function. It tells the compiler the next block of code is going to be reusable. **Every** line after the def needs to be indented if it is part of the function as python uses indents to determine code blocks. The name is what you will call the function. It can be anything you want, as long as it starts with a letter, and isn't a reserved word. 

parameters
  : this is optional, but often you have one or more parameters. For every parameter named, it ends up being a variable with a value in it! In the example, `animal` is a parameter that I can use directly as a variable. `sound` is a parameter that I use directly as a variable. We will code trace this example below

return value
  : the return keyword says "give back this value". This is critical, and setting the returned value to a variable `cat_says = says("cat, "meow")` is critical!

docstring
  : we will explore this below, but it is important to document what the function is doing!

You have the basic parts, but let's trace the above function!

### Trace The Code

Following the code below, it is important to note that with the function call a new frame is created! This frame has a unique set of variables for that execution, and then it returns back to the global frame.

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20says%28animal,%20sound%29%3A%0A%20%20return%20f%22The%20%7Banimal%7D%20says%20%7Bsound%7D.%22%0A%0Acat_says%20%3D%20says%28%22cat%22,%20%22meow%22%29%0Adog_says%20%3D%20says%28%22dog%22,%20%22woof%22%29%0Aprint%28cat_says%29%0Aprint%28dog_says%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

### Practice
Now it is your turn to practice. 

```{admonition} Tasks
:class: tip
You will write a function and then call/invoke that function with different parameters.

- [ ] Write a function that takes in two dates, current_year and birth_year 
- [ ] Return the persons age based on current_year and birth_year (no need to worry about months)
- [ ] Call the function with the parameters 2022 and 1980, print out the result
- [ ] Call the function with the parameters of 2023 and 1989, print out the results
```


Use the 'click to show' to get a code editor below.


```{toggle} 
<iframe
 frameBorder="0"
 height="450px"  
 src="https://onecompiler.com/embed/python/3ym59u5qg?hideLanguageSelection=true&hideNewFileOption=true&hideTitle=true&hideNew=true&hideStdin=true" 
 width="100%"
 ></iframe>
```

#### Solution
```{code-cell}
:tags: [hide-cell]
def calc_age(current_year, birth_year):
  return current_year - birth_year

age1 = calc_age(2022, 1980)
age2 = calc_age(2023, 1989)

print(age1)
print(age2)
```


## Functions calling functions

It is also possible to have a function call another function inside of it! For example, let's modify the above code to be:

```{code-cell}
def double_it(value: str) -> str:
    """Doubles a string value

    Args:
        value (str): The string to be doubled with \\n between the string

    Returns:
        str: value twice with a new line between
    """
    return f"{value}\n{value}"

def dsays(animal : str, sound : str) -> str:
    """Takes and animal and sound, and returns a doubled version of the animal says.

    Args:
        animal (str): the animal
        sound (str): the sound they make

    Returns:
        str: A doubled version of the saying "The {animal} says {sound}."
    """
    double = double_it(f"The {animal} says {sound}.")
    return double

cat_says = dsays("cat", "meow")
dog_says = dsays("dog", "woof")
print(cat_says)
print(dog_says)
```


### Trace The Code
Trace the code above. Notice that the `dsays` frame is still open while `double_it()` is being called.


<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20double_it%28value%3A%20str%29%20-%3E%20str%3A%0A%20%20%20%20%22%22%22Doubles%20a%20string%20value%0A%0A%20%20%20%20Args%3A%0A%20%20%20%20%20%20%20%20value%20%28str%29%3A%20The%20string%20to%20be%20doubled%20with%20%5C%5Cn%20between%20the%20string%0A%0A%20%20%20%20Returns%3A%0A%20%20%20%20%20%20%20%20str%3A%20value%20twice%20with%20a%20new%20line%20between%0A%20%20%20%20%22%22%22%0A%20%20%20%20return%20f%22%7Bvalue%7D%5Cn%7Bvalue%7D%22%0A%0Adef%20dsays%28animal%20%3A%20str,%20sound%20%3A%20str%29%20-%3E%20str%3A%0A%20%20%20%20%22%22%22Takes%20and%20animal%20and%20sound,%20and%20returns%20a%20doubled%20version%20of%20the%20animal%20says.%0A%0A%20%20%20%20Args%3A%0A%20%20%20%20%20%20%20%20animal%20%28str%29%3A%20the%20animal%0A%20%20%20%20%20%20%20%20sound%20%28str%29%3A%20the%20sound%20they%20make%0A%0A%20%20%20%20Returns%3A%0A%20%20%20%20%20%20%20%20str%3A%20A%20doubled%20version%20of%20the%20saying%20%22The%20%7Banimal%7D%20says%20%7Bsound%7D.%22%0A%20%20%20%20%22%22%22%0A%20%20%20%20double%20%3D%20double_it%28f%22The%20%7Banimal%7D%20says%20%7Bsound%7D.%22%29%0A%20%20%20%20return%20double%0A%0Acat_says%20%3D%20dsays%28%22cat%22,%20%22meow%22%29%0Adog_says%20%3D%20dsays%28%22dog%22,%20%22woof%22%29%0Aprint%28cat_says%29%0Aprint%28dog_says%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

## Docstring

````{margin}
  ```{admonition} Google Style
    :class: tip
    In this book we will use the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) 
    format for docstrings. Eventually, you will learn about tools like Sphinx.autodoc that can generate webpages 
    based on your docstrings for others to use your code.  
    If you are using [VSCode](https://code.visualstudio.com/) there is an [extension](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) for docstrings that defaults to google format. If you are using [PyCharm](https://www.jetbrains.com/pycharm/) the 
    docstring formatter is included, but you may need to go into preferences to make sure it uses google. 

    In both cases, you just simply define your function, type return/enter, and then three three quotation marks and enter. This will
    automatically generate the base docstring formatting!
````
In the above example, we gave an extensive {term}`docstring` which is short for documentation string. It is a special formatted string using three double quotes immediately below the function definition. It is broken up into the various parts.

```python
"""Summary - can be multiple lines

Example: 
  >>> some examples of execution 
  result of execution
  >>> another example of execution
  result of example

Args:
  Variable Name (type): Why it is needed
  Variable Name (type): etc

Returns:
  (type): description about the value being returned. 
  You can have multiple lines explaining what to expect
"""
```
The summary should provide what the function does in simple terms. It can be detailed and even highlight some of the steps as part of the process. While not common, for this course, you will include a section that includes expected input and output for the function. This will be used to help you test and debug functions that we talk about in the next section. **Example**, you will be putting in examples of what happen when that function is called. These actually double up as tests to confirm the validity of what you wrote. In **Args** you put in the name and type (optional) for each of your parameters. This is also called function arguments, thus the term "Args". **Returns** The return is important, so you know what is being returned. The type is optional, but good to put in there, so the person calling your function knows the type to expect. This section can have multiple lines to provide more details of the returned value.  

Why is this formatting useful? It is actually possible to generate webpages, and this formatting is used on the [python language library](https://docs.python.org/3/library/index.html) to generate the entire website! Most importantly, you write docstrings so **you** know what you did (or least supposed to do) when you wrote the function and come back to it later!

```{epigraph}
Documenting functions is critical to programming, both on the job and in practice.
```

Additionally, if you put in the docstring, you can easily type to find out what a function does!

```{code-cell}
help(dsays)
```

We can also print the doc using `__doc__`

```{code-cell}
print(dsays.__doc__)
```

This also works for built in functions

```{code-cell}
help(print)
```

As such, if you are unsure what a function does, if it has a docstring, you can quickly check! 

## Next Steps

Between basic instructions and functions, you have a solid foundation to start writing simple programs. It will also help us start the major design thought for this class, **divide-conquer-glue**.


## Knowledge Checks

TO ADD