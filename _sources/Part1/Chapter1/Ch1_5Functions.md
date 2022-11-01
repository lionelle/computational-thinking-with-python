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
    def double_it(value):
      """Doubles a string value
        
        :param value: the string you want doubled to be separated by new line character
        :type value: Any
        :return: a doubled string of the format "{value}\n{value}"
        :rtype: str
      """
      return f"{value}\n{value}"

    def dsays(animal, sound):
      """Builds a doubled string of what the animal says, and doubles it before return
      
        :param animal: The type of animal
        :type animal: str
        :param sound: The sound the animal makes
        :type sound: str
        :return: string of format "The {animal} says {sound}.\\nThe {animal} says {sound}."
        :rtype: str
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


<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20double_it%28value%29%3A%0A%20%20%22%22%22Doubles%20a%20string%20value%0A%20%20%20%20%0A%20%20%20%20%3Aparam%20value%3A%20the%20string%20you%20want%20doubled%20to%20be%20separated%20by%20new%20line%20character%0A%20%20%20%20%3Atype%20value%3A%20Any%0A%20%20%20%20%3Areturn%3A%20a%20doubled%20string%20of%20the%20format%20%22%7Bvalue%7D%5Cn%7Bvalue%7D%22%0A%20%20%20%20%3Artype%3A%20str%0A%20%20%22%22%22%0A%20%20return%20f%22%7Bvalue%7D%5Cn%7Bvalue%7D%22%0A%0Adef%20dsays%28animal,%20sound%29%3A%0A%20%20%22%22%22Builds%20a%20doubled%20string%20of%20what%20the%20animal%20says,%20and%20doubles%20it%20before%20return%0A%20%20%0A%20%20%20%20%3Aparam%20animal%3A%20The%20type%20of%20animal%0A%20%20%20%20%3Atype%20animal%3A%20str%0A%20%20%20%20%3Aparam%20sound%3A%20The%20sound%20the%20animal%20makes%0A%20%20%20%20%3Atype%20sound%3A%20str%0A%20%20%20%20%3Areturn%3A%20string%20of%20format%20%22The%20%7Banimal%7D%20says%20%7Bsound%7D.%5CnThe%20%7Banimal%7D%20says%20%7Bsound%7D.%22%0A%20%20%20%20%3Artype%3A%20str%0A%20%20%22%22%22%0A%20%20double%20%3D%20double_it%28f%22The%20%7Banimal%7D%20says%20%7Bsound%7D.%22%29%20%0A%20%20return%20double%0A%0Acat_says%20%3D%20dsays%28%22cat%22,%20%22meow%22%29%0Adog_says%20%3D%20dsays%28%22dog%22,%20%22woof%22%29%0Aprint%28cat_says%29%0Aprint%28dog_says%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


## Docstring

````{margin}
  ```{admonition} reStructuredText
    :class: tip
    In this book we will use the [reStructuredText](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html) format for docstrings encouraged as the default for Sphinx.autodoc. Sphinx is a common documentation generator in industry,
    and reST is common. It is simply a way to format your files, so another program can read it to generate webpages or other documentation.  If you are using [VSCode](https://code.visualstudio.com/) there is an [extension](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) for docstrings. If you are using [PyCharm](https://www.jetbrains.com/pycharm/) it
    is the default documentation syntax for python. 

    In both cases, you just simply define your function, type return/enter, and then three three quotation marks and enter. This will
    automatically generate the base docstring formatting!
````
In the above example, we gave an extensive {term}`docstring` which is short for documentation string. It is a special formatted string using three quotes or three double quotes immediately below the function definition. It is broken up into the various parts.

```python
"""[SUMMARY]

----
[Expected input and output] 
----

:param parameter1: Description of parameter
:type parameter1: Optional, but clear definition of expected value type
... 

:return: Description of what is returned
:rtype: description of the return type
"""
```
The summary should provide what the function does in simple terms. It can be detailed and even highlight some of the steps as part of the process. While not common, for this course, you will include a section that includes expected input and output for the function. This will be used to help you test and debug functions that we talk about in the next section. The param is needed for each parameter, but the type is optional. However, it helps you clearly see what you expect. The return is important, so you know what is being returned. The rtype is also optional, but it helps you know more about what is being returned. 

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