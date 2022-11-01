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

# 1.4 Basic Operators and Expressions

Growing up we learn basic mathematical operations like addition, subtraction, multiplication, and division. For example, using basic math, we would look at the following statement:

$ 40 + 2 $

And say the answer is `42`. With computers, we need to store that answer in memory, so we are given the {term}`Assignment Operator`, the `=` sign! As such, if I want to store that value, I use the following

```{code-block}
meaning = 40+2
```

what we have is is the Expression 40+2, using the addition `+` operator, and then using the `=` we assign value to the variable `meaning`. Programming has the basic operators we learn growing up.

| Operator | Name |
| -- | -- |
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| = | Assignment |

You will note that `*` is multiplication, and not x that is because how would one distinguish a variable x from the operator x? As such, we have to use unique characters. 

```{note}
Python uses {term}`PEMDAS` for order of evaluation.   
  **P** - Parentheses  
  **E** - Exponentiation  
  **M** - Multiplication  
  **D** - Division   
  **A** - Addition  
  **S** - Subtraction 

So parentheses get evaluated first, and so on down the line. Another way to remember is the mnemonic, "Please Excuse My Dear Aunt Sally".  With that said, if you are trying to figure out the order of evaluation for an expression, the simple answer is you probably
can write it better by using parentheses. Always remember, clarity before brevity. 
```

```{epigraph}
Use parentheses when dealing with order of evaluation. Clarity before brevity!
```

````{margin}
```{admonition} Naming Variables
  :class: note
 You can name a variable whatever you want, as long as you follow these rules
 1. A variable name must start with a letter or the underscore character. 
 2. A variable name can only contain alpha-number characters and underscores.
 3. Names are case sensitive (Name and name are two different variables)
 4. You may not use any of the reserved words. These are commands in python, and they are as follows.  
  
  |  |  |  |
  |---|---|---|
  | False | def | if | 
  |raise | None | del | 
  | import | return | True | 
  | elif | in | try |
  | and | else | is | 
  | while | as | except | 
  | lambda | with | assert | 
  | finally | nonlocal | yield |
  | break | for | not | 
  | class | from | or | 
  |continue | global | pass |

````

## Practice
```{admonition} Tasks
:class: tip
Using the following programming window try the following. You should run after each task, not after all the lines!

- [ ] Write a statement that assigns your name to the variable `name`. 
- [ ] Print out the your name as "Hello, name". With name using the variable. 
- [ ] Write a statement that assigns your age to the variable `age`. 
- [ ] Modify the previous print statement to say using the variables, "I am name, and I am age years old.".   
      You may need to move the print statement, remember things are executed in order!
- [ ] Modify the age assignment to be calculated by the current year, minus the year you were born, and then assign the answer to `age`.
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

### Solution
```{code-cell}
:tags: [hide-cell]
name = "Trillian Astra"
age = 2022 - 1980
print(f"I am {name}, and I am {age} years old.") # remember last section on f-string
```

## Types

Without knowing it, we have looked at **numeric** types and the **string** type. Anytime, you type in a number without quotes, you end up with a numeric. Let's look at string more. 

### String 
A string can be any sequence of characters (look at your keyboard, those are all characters). However, given that programming using a set syntax/grammar how would I know the variable `meaning` as compared to a string `meaning`? As such, most languages define using the quote or double character as defining a string. For example:

```{code-cell}
meaning = 42
a_string = "meaning"

print(meaning)
print(a_string)
```

In python, you can use *either* the single quote `'` or the double quote `"` to define a string, as long as you start and end with the same one! This helps us in cases like the following:

```{code-cell}
quote = 'And he replied, "As you wish."'
conjunc = "Isn't python cool?"

print(quote)
print(conjunc)
```

In this book, we will most often use double quotes for strings with more than one character, and single quote for single character strings. While there are [style conventions](https://pep8.org/) for python, which type of quote to use is intentionally not defined in the style convention, other than pick one style and stick to it.

#### Adding Strings - Concatenation  

You can also add strings together called Concatenation. For example, let's take two strings.

```{code-cell}
first = "Trillian"
last = "Astra"
```

If I wanted to make a single variable I could do the following.

```{code-cell}
name = first + last
print(name)
```

```{error}
Wait! That didn't work how I wanted!!
```
Did I specify a space between the two strings? No, I didn't, and  computer wouldn't know unless I am exact! As such to do the above properly, I should do the following.

```{code-cell}
name = first + ' ' + last  # the space is a single character string
print(name)
```

##### Alternative to String Concatenation  - f-String

You can use the format string (f-string) as a way to concatenate, especially if you know the exact pattern you want your string to look like.

```{code-cell}
name2 = f"{first} {last}"
print(name2)
```

#### Special Characters
````{margin} 
  ```{admonition} ASCII-Art   
    ASCII-Art is has a long tradition in computer science, and even before dating back to the original printing presses. It is the art of using characters to build full pictures, and the modern emote is based off the same idea. ASCII is a standard used to convert numbers to characters for display on your screen. To see some examples of ascii-art, visit the [ASCII Art Archive](https://www.asciiart.eu/).
  ```
````

There are a number of special hidden characters you use all the time. Tab and the newline character being the most common. In most languages, including python, they are represented by the `\t` for tab, and `\n` for the new line. This also means to represent the backslash, you have use `\\`. For example:

```{code-cell}
line1 = "hello\n"
line2 = "\tworld\n¯\\_(ツ)_/¯"

print(line1 + line2)
```

> Thinking deeper, the `print()` function adds `\n` to the end of all your strings!



#### Trace the Code Execution
Use the toggle below to see the full code execution step by step. 

```{toggle} 
<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=first%20%3D%20%22Trillian%22%0Alast%20%3D%20%22Astra%22%0A%0Aname%20%3D%20first%20%2B%20last%0Aprint%28name%29%0A%0Aname%20%3D%20first%20%2B%20'%20'%20%2B%20last%0Aprint%28name%29%0A%0Aname2%20%3D%20f%22%7Bfirst%7D%20%7Blast%7D%22%0Aprint%28name2%29%0A%0Aline1%20%3D%20%22hello%5Cn%22%0Aline2%20%3D%20%22%5Ctworld%5Cn%C2%AF%5C%5C_%28%E3%83%84%29_/%C2%AF%22%0A%0Aprint%28line1%20%2B%20line2%29&codeDivHeight=400&codeDivWidth=350&cumulative=true&curInstr=0&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D"> </iframe>

```

## Introducing input()

We have already given you function, the `print()` function, which displays text output onto the console/screen. However, what if we wanted to get information from our client, most notably, values from what they type on a keyboard? Python has the `input()` function. By default, it takes a message you want to display as a {term}`Parameter`, and it first calls `print()` with that message, and then waits for the client to type. When the client hits enter, the value is returned to your code so you can **store** it in a variable.  For example:

```{code-block}
name = input("What is your name? ")
print("Nice to meet you, {name}.")
```
 
Now run the code yourself! Change Ada Lovelace to your name in the STDIN block before clicking run.
<iframe
 frameBorder="0"
 height="450px"  
 src="https://onecompiler.com/embed/python/3ym26kn3u?hideLanguageSelection=true&hideNewFileOption=true&hideTitle=true&hideNew=true" 
 width="100%"
 ></iframe>

```{admonition} Show Run Example:
:class: tip
:class: toggle

![Run Greeting Example](../../fig/run_greeting.gif)
```

 ```{warning}
 When looking at code through the browser based code window, newline returns end up getting removed. The above example may be better written it in an IDE or directly in the python interpreter to have a more interactive experience. 
 ```

## input() with numbers
As a reminder, input returns a **string** which is not the same as a numeric type. So let's assume for the following input, someone enters $1980$ in the input below.

```{code-block}
born_year = input("What year were you born in? ")
current_year = input("What year is it currently? ")
```

```{code-cell}
:tags: [remove-cell]
born_year  = "1980"
current_year = "2022"
```

```{code-cell}
age = current_year - born_year
print(f"My age in {current_year} is {age}.")
```

The error above is generated! This is because it doesn't make sense to subtract a string from a string, and `input()` always provides strings! For now we will learn to cast the string to `int()` if the input is supposed to be a whole number (no decimal places) or a `float()` for numbers with decimal places. As such, code above would be converted to the following:

```{code-block}
born_year_str = input("What year were you born in? ")
born_year = int(born_year_str)
current_year_str = input("What year is it currently? ")
current_year = int(current_year_str)

age = current_year - born_year
print(f"My age in {current_year} is {age}.")
```

### Visualization
<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=born_year_str%20%3D%20input%28%22What%20year%20were%20you%20born%20in%3F%20%22%29%0Aborn_year%20%3D%20int%28born_year_str%29%0Acurrent_year_str%20%3D%20input%28%22What%20year%20is%20it%20currently%3F%20%22%29%0Acurrent_year%20%3D%20int%28current_year_str%29%0A%0Aage%20%3D%20current_year%20-%20born_year%0Aprint%28f%22My%20age%20in%20%7Bcurrent_year%7D%20is%20%7Bage%7D.%22%29&codeDivHeight=400&codeDivWidth=350&cumulative=true&curInstr=0&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%221980%22,%222022%22%5D"> </iframe>

For this visualization, the inputs are fixed to 1980 and 2022. If you wish to modify the input, you will need to open it up directly in [Python Tutor](https://pythontutor.com/render.html#code=born_year_str%20%3D%20input%28%22What%20year%20were%20you%20born%20in%3F%20%22%29%0Aborn_year%20%3D%20int%28born_year_str%29%0Acurrent_year_str%20%3D%20input%28%22What%20year%20is%20it%20currently%3F%20%22%29%0Acurrent_year%20%3D%20int%28current_year_str%29%0A%0Aage%20%3D%20current_year%20-%20born_year%0Aprint%28f%22My%20age%20in%20%7Bcurrent_year%7D%20is%20%7Bage%7D.%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).  

### You Got This
This is a lot! However, the more your practice, the better you will become. It is also important to think about dividing these problems into smaller chunks, which is why writing your own functions becomes fundamental!

## Knowledge Checks 

TO ADD