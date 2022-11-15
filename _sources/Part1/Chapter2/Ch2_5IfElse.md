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

# 2.5 if / else statements

With programming, it is very common to only have code that runs **conditionally** meaning if a statement is true, we run that block of code. We do that in life pretty regularity. If something is true, we do it. If it isn't true (or false), we don't do it. Are we hungry? True or False, if True, we eat, if False we don't eat. In programming, we have commands built into the language - `if` being the command.

## if statement syntax

The syntax of an `if` statement is:

```text
if condition:
   block of code
   more code
Outside of if
```

Let's view that in code

```{code-cell}
if 10 > 5:
    print("inside if block")
print("This will get executed no matter what")
```

And if the conditional statement is False.
```{code-cell}
if 0 > 5: #notice value change
    print(">>inside if block<<")
print("This will get executed no matter what")
```
Let's try it with code tracing

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20comparison_check%28value%29%3A%0A%20%20%20%20if%20value%20%3E%3D%205%3A%0A%20%20%20%20%20%20%20%20print%28f%22%7Bvalue%7D%20is%20greater%20than%20equal%20to%20five%22%29%0A%20%20%20%20print%28%22End%20of%20function%22%29%0A%0A%0Acomparison_check%286%29%0Aprint%28%29%20%23%20to%20add%20an%20empty%20line%0Acomparison_check%285%29%0Aprint%28%29%0Acomparison_check%284%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Pay special attention step 18. 

```{Note}
Anytime you indent in python, you are looking at a code block. A function is a code block where all that code belongs to the `def` for your function. An if block is your indented code that follows the `if` statement. Notice the colon is used before each block, and the indentation matters! 
```


### Practice

Let's practice writing simple `if` statements.

```{admonition} Tasks
:class: important

You task is to write a program that takes client input, and their goal is guess a number. They get one guess, and they get told 'Correct', 'Low', or 'High'.  For now, you can pick `3` for the number they are to guess.

- [ ] Divide the problem up into smaller parts
- [ ] **important!** Draw a flowchart for the function that includes the if statements (called check_guess) 
- [ ] Write function for testing the value, it should return the string value!
- [ ] Test the function
- [ ] Write function for getting client input (similar to the get_year() you did before...)
- [ ] Test the final program

Don't forget to document using docstring. We will also come back to the flowchart throughout this section.s

HINT: You can have (and need) three seperate `if` statements. 
```

#### Programming Window

{{empty_code_window}}

#### Solution

````{toggle}
```python
def check_guess(value : int) -> str:
    """Informs the client if their value is greater than, less than, or
        equal to 3. Returns the string value based on Correct, Low, or High
    
    Examples:
        >>> check_guess(3)
        'Correct'
        >>> check_guess(2)
        'Low'
        >>> check_guess(4)
        'High'

    Args:
        value (int): The value to be guessed, already assumed to be an int

    Returns:
        str: The values Correct, High or Low 
    """
    response = ""
    if value == 3:
        response = "Correct"
    if value > 3:
        response = "High"
    if value < 3:
        response = "Low"
    return response

def get_guess():
    """Gets a number from the client. Does not currently handle error checking.
    
    Examples:
        Client enters 2
        >>> get_guess()  # doctest: +NORMALIZE_WHITESPACE
        Guess a whole number:
        2
        
        Client enters 3
        >>> get_guess()  # doctest: +NORMALIZE_WHITESPACE
        Guess a whole number:
        3

    Returns:
        int: a whole number value for their guess
    """
    guess_str = input("Guess a whole number: ")
    return int(guess_str)

main() # run it!
```
Your solution may have different comment, especially on the built in tests. **If you didn't include them, you should get into the 
practice of including the full docstrings. **

```{note}
What is this `# doctest: +NORMALIZE_WHITESPACE` in the docstring? This is commonly used when dealing with client input. It allows
the test to show up on multiple lines without it erroring.
```
````

##### Solution Flowchart for check_guess(value)
````{toggle}
```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart TD
    s([Start]) -- value --> cg["check_guess(value)"]
    cg --> set["set response = ''"]
    set -->  if1{"value equals 3?"}
    if1 -- True --> set1["response = 'Correct'"]
    if1 -- False --> if2{"value greater than 3?"}
    set1 --> if2

    if2 -- True --> set2["response = 'High'"]
    if2 -- False --> if3{"values less than 3"}
    set2 --> if3

    if3 -- True --> set3["response = 'Low'"]
    if3 -- False --> rtn["return response"]
    set3 --> rtn
    rtn --> e([End])
      
```
````

In the flowchart above, we notice that every if condition gets checked, no matter the result of the previous condition. That seems like a waste if we already know the one before that is free. As such, let's as the `else` statement.

## Else

We are interested in running code if a condition is True, but we are also interested in **only** running code if the condition is False. In english, we would say, "If we are hungry, we eat, else we go play." Represented in a flowchart, that is:

```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart TD
    s([Start]) -->if{"I am hungry"}
    if -- True --> eat["Let's eat"]
    if -- False --> play["Let's play"]
    eat --> e([End])
    play --> e
```

From a python perspetive, the syntax would be the following

```python
status = input("Are you hungry (y/n)? ")
if status == 'y':
    print("I hungry")
    eat()
else:
    print("not hungry!")
    play()
```

Notice the if has a block of code under it (which in this case is printing and then invoking a method), and else has a block of code. You can tell by the indentations that block 'belongs' to the line above it.  

### Visualize
See the above example ran with both 'y' and 'n' entered!
<iframe width="800" height="600" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20eat%28%29%3A%0A%20%20%20%20print%28%22Nom%20nom%22%29%0A%20%20%20%20%0Adef%20play%28%29%3A%0A%20%20%20%20print%28%22Would%20you%20like%20to%20play%20a%20game%3F%20%22%29%0A%0A%0Adef%20need_to_eat%28%29%3A%0A%20%20%20%20status%20%3D%20input%28%22Are%20you%20hungry%20%28y/n%29%3F%20%22%29%0A%20%20%20%20if%20status%20%3D%3D%20'y'%3A%0A%20%20%20%20%20%20%20%20print%28%22I%20hungry%22%29%0A%20%20%20%20%20%20%20%20eat%28%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22not%20hungry!%22%29%0A%20%20%20%20%20%20%20%20play%28%29%0A%20%20%20%20%20%20%20%20%0Aneed_to_eat%28%29%20%23%23%20entered%20'y'%0Aneed_to_eat%28%29%20%23%23%20entered%20'n'&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%22y%22,%22n%22%5D&textReferences=false"> </iframe>



[Run it yourself](https://pythontutor.com/render.html#code=def%20eat%28%29%3A%0A%20%20%20%20print%28%22Nom%20nom%22%29%0A%20%20%20%20%0Adef%20play%28%29%3A%0A%20%20%20%20print%28%22Would%20you%20like%20to%20play%20a%20game%3F%20%22%29%0A%0A%0Adef%20need_to_eat%28%29%3A%0A%20%20%20%20status%20%3D%20input%28%22Are%20you%20hungry%20%28y/n%29%3F%20%22%29%0A%20%20%20%20if%20status%20%3D%3D%20'y'%3A%0A%20%20%20%20%20%20%20%20print%28%22I%20hungry%22%29%0A%20%20%20%20%20%20%20%20eat%28%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22not%20hungry!%22%29%0A%20%20%20%20%20%20%20%20play%28%29%0A%20%20%20%20%20%20%20%20%0Aneed_to_eat%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

### Nesting Statements

Because you can have blocks within blocks, it is possible and common to nest if statements. For example:

```{code-cell}
value = 2
if value < 3:
    if value > 0:
        print("value is possitive, but less than 3")
    else:
        print("value is negative or 0")
else:
    if value < 10:
        print("value is 3-9")
    else:
        print("value is possitive, 10 or higher")
```
#### Nested Statement Flowchart
The flowchart for the above code is also direct.
```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart TD
    s([Start]) --> set["set value to 3"]
    set --> if1{"value < 3"}
    if1 -- True --> if1_2{"value > 0"}
    if1 -- False --> else1_2{"value < 10"}

    if1_2 -- True --> p1["print is possitive,<br> but less than 3"]
    if1_2 -- False --> p2["print value is<br> negative or 0"]

    else1_2 -- True --> p3["value is 3-9"]
    else1_2 -- False --> p4["value is possitive,<br> 10 or higher"]

    p1 --> e([End])
    p2 --> e
    p3 --> e
    p4 --> e

```

```{important}
Drawing the tree / flowchart like the one above makes understanding nested if-statements *much* easier. Given the above example, we know the moment a value tests as true, we can never *jump* to another side of the tree. Or another way to say it, draw a line down the middle, and you will never pass that line. Once this drawn, we can feed any series of numbers, and we can easily trace to the answer. Can be much easier than reading the code on complex nesting statements!

```

Between if statements and conditions, you have the basics of controlling the flow of which of your operations get executed. With that said, using just the tools we have, how would we repeat an action until a certain condition is met? Let's look at that!

```{note}
When you look up if-statements in python, you will see a number of commands we don't cover here. `elif`, `and`, `or`, `not` for the primary ones. The reason these are omitted is becuase we will come back to this topic in a couple chapters. While traditional programming teaches you everything at once, research shows it is better to learn in stages, and return to topics. For now, you can safely ignore such references online, and focus only on understanding the fundamental structure of if/else.
```

## Knowledge Check