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
# 2.7 Algorithmic Design

For this design walk through, we are going to build a guessing game application. The goal is to help combine the elements for algorithmic thinking with decomposition and abstraction. We encourage you to follow along using your own {term}`IDE`. 

We will also introduce two new concepts in this section
* `randint()` - a way to generate random numbers [built into python](https://docs.python.org/3/library/random.html#random.randint)
* `if __name__ == "__main__":` a common block used in python code to make running programs easier

```{margin} Design Worksheet
TODO: add a downloadable worksheet to build through design process
```

```{margin} Programmers Notebook
   Are you using your programmers notebook? There is a worksheet that you can use above, or you can put it all in the notebook. 
```
Our client has presented the following request to us. 

```{admonition} Scenario
We would like you to build a guessing game. The player is asked the high end of range of possible numbers, and then a random number is generated between 1 and the number provided. They are meant to guess with being given feed back, high, low, or correct if they guess it correctly. If the client enters an 'x' the program ends early, sharing with them what the number. 

**Stretch / Bonus Goals** 
* Add the option to create a limited number of guesses

You have the freedom to determine the wording used in the application. 
```

## Design: Big View
We first start with high level design of the program. This is completely conceptional and separate from the code. Often called the 'big' view or high level view. Using the **Divide-Conquer-Glue** approach, this can be broken down as the following.

1. Brainstorm Program Steps / Client Perspective
2. Break Steps up into Logical Parts (divide)
3. Repeat 2 with until minimal 
4. Look for ideas that can be combined into similar concepts 
5. For each compo

### Brainstorm Steps Required

Write down the major tasks defined by the client.

1. Ask player to set the *max* range of the guess, giving  $ 1 <= n <= max $
2. Set a random number 
3. Start game
   1. Ask player to guess a number
      1. If high, respond to with 'High'
      2. If low, response with 'Low'
      3. If the number, respond with 'Correct'
   2. Repeat until 'Correct'
4. End game - report out that it is correct, and end the game
   1. Special condition, 'x' can end the game immediately, displaying the correct answer


### Decomposition 

````{grid}
:gutter: 3

```{grid-item-card} Start Game

Collect From client:
* max range
  * convert max to `int`
  * needs to be greater than 0

Background process:
* select random number based on range
```

```{grid-item-card} Play Game
* Get guess from client
  - convert guess to `int` 
    - check for 'x' before converting!
    - needs to be greater than 0

Test guess against actual number
* respond with, high, low, correct
* if correct - end game
* else - repeat


Needs: random number
Finishes with: True they won, 
or False they did not (aka they typed 'x').

```

```{grid-item-card} End Game
Report the correct number, and that they won or not

Needs: They won or not from Play game
Needs: The random number
```
````

### Look for Patterns, and Abstraction

Are there any tasks that are exactly the same between components?

```{epigraph}
Look for matching tasks! 
```

The getting client input and converting it into an `int` is a matching task. As such, if we look how to represent that abstractly, we can come up with a "utility function" that helps with both components. We can also further divide the program into components or functions at this stage.
````{margin} Time Management
```{note}
These components can help with time management. Let's say we have an assignment due in a week, if **on the day it is assigned** we break up the project into these components, we can then assign a day/time to work on each component. This helps from last minute scrambling, and provides time to modify and revamp. 

```
````

````{grid}
:gutter: 2

```{grid-item-card} get_positive_int(prompt : str) -> int
* get input from client
* check to see if input is x
* convert to int
* check to see if input > 0
* repeat until x or greater than 0

question: what value can I return that means they put in 'x'?
answer: -1 (since it has to be positive)

Note: further error checking could happen, but not required.

Dev Required:
* None
```


```{grid-item-card} main()
* max = get max from client
* correct_answer = $1 <= n <= max$ random
* victory = play_game(correct_answer)
* if victory is true: display congrats
* else display correct_answer

Dev. Required:  
* get_positive_int
* play_game
```
````


````{grid}
:gutter: 2

```{grid-item-card} play_game(correct: int) -> bool 

* guess = prompt for client input
* if value > -1
    response = check(guess, correct)
    if response == 'Correct' - return true
    else print(response)
* if value < 0 return False

Dev Required:  
* check
* get_positive_int
```


```{grid-item-card} check(guess : int, correct : int) -> str
* if guess == correct - return 'Correct'
* else if guess < correct - return 'Low'
* else return 'High'

Dev Required:
* None
```
````

```{admonition} STOP
:class: error

You have taken a moment to define your functions. You **DO NOT** have to stick to this plan 100%. Sometimes you come back to this stage, once you realize what you need to do to implement a function, or (more commonly) you realize one function should be broken up into even smaller parts. 

It is also good to think about it for a moment before moving forward. Does this cover the entire program? Are there things you may be missing? Critically evaluate and reflect.

```


## Writing Code: The Small View 

At this stage, you start thinking about the actual algorithm you want to build. It is essential to keep the task **small**, so your algorithm can remain simple. If you find your algorithm is getting too complex, then you may want to reevaluate what you are doing! At this stage, we are thinking more about the single repeatable algorithm for a single task.

```{epigraph}
Look at small tasks when writing code
```

Since we defined the various functions above, at this stage write each function. Which begs the question, where do we start?

First, check your dependencies - which function depends on others being completed (written as Dev Required above). Only two functions do not require others to be implemented, so that is a very good place to start. Out of the two, one requires both loops and conditions, while the other just requires conditions and similar to what we wrote before. As such, starting at `check(guess, correct)` is a good spot! 

### Focus on `check(guess: int, correct: int) -> str:`

From this point, the rest of the functions or the program doesn't matter. You have **ONE** task only, complete a function that takes in two values, and lets you know if the values are equal, or if one is lower or higher than the other. That is it! A very common mistake with programming is trying to think of all the things you need to do, when really, you are switching your focus to the one small thing you need to do. 

```{important}
Remember the **Steps for Writing a Function**

1. Define the function
2. Document the function - with expected input and output
3. Write the function incrementally
    * You can test as you write - run snippets to see what is happening, etc
4. Test the function with full black box testing

```

A function isn't completed until all the steps above are completed. After it is completed, you can just *use* the function without having to worry about it again (mostly).

#### Step One: Define The Function
Mostly done in the card above, though writing additional implementation notes or doing flow diagrams often happens at this stage. 
Code wise, we end up with

```python
    def check(guess : int, correct : int) -> str:
        # in progress
```

#### Step Two: Document

Write the *docstring* and follow the full documentation pattern defined in {doc}`../Chapter1/Ch1_5Functions`. We want to make sure we include tests by way of sample input and output as part of the docstring. For this function, it could look like.

```python
def check(guess : int, correct : int) -> str:
    """Checks to see if guess is equal to, higher or lower than correct. Returns
    'Correct', 'High', 'Low' respectively.

    Examples:
        >>> check(10, 10)
        'Correct'
        >>> check(3, 5)
        'Low'
        >>> check(5, 3)
        'High'

    Args:
        guess (int): the value they are guessing
        correct (int): a value that is to be tested against

    Returns:
        str:  'Correct', 'High',  or 'Low'
    """
```


#### Step Three: Write the function incrementally

This is where you write code. You may also want to write a flowchart to see the logic, as it is an if statement with a nested if statement.

```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart TD
    s([Start]) --> setResponse["response = ''"]
    setResponse --> if{"guess == correct"}

    if -- True --> setC{"response = 'Correct'"}
    if -- False --> if2{"guess < correct"}

    if2 -- True --> setL{"response = 'Low'"}
    if2 -- False --> setH{"response = 'High'"}

    setC --> e(["End(return response)"])
    setL --> e
    setH --> e
```

Now in code form.
```{code-cell}
def check(guess : int, correct : int) -> str:
    """Checks to see if guess is equal to, higher or lower than correct. Returns
    'Correct', 'High', 'Low' respectively.

    Examples:
        >>> check(10, 10)
        'Correct'
        >>> check(3, 5)
        'Low'
        >>> check(5, 3)
        'High'

    Args:
        guess (int): the value they are guessing
        correct (int): a value that is to be tested against

    Returns:
        str:  'Correct', 'High',  or 'Low'
    """
    response = ''
    if guess == correct:
        response = 'Correct'
    else:
        if guess < correct:
            response = 'Low'
        else:
            response = 'High'
    return response
```


#### Step Four: Test!
Now, you write tests to test your function. You always do this before moving on, as it becomes *exponentially* harder to find errors later as you write more functions!


```{code-cell}
### Tests comment out when done
print("TESTING: check(guess, correct)")
val1 = check(10, 10)
print(f"TEST: check(10, 10) should return 'Correct', it returned: {val1}")
val2 = check(3, 5)
print(f"TEST: check(3, 5) should return 'Low', it returned: {val2}")
val3 = check(5, 3)
print(f"TEST: check(5, 3) should return 'High', it returned: {val3}")
```

The function now works and has been verified. You shouldn't have to go back to the function unless you figure out an error in your design later in the process. 

###  Your Turn!
```{margin} Instructor Note:
Walking through one of these functions would be a good lab activity!
```


Implement:
1. get_positive_int(prompt) 
2. play_game(correct)

Make sure to complete all four steps for each before you move onto the next! The logic for both is a bit harder, as it will require repetition. You will definitely want to work out the flowchart, and test as you develop!

#### Solution

This is one possible solution. Your wording may be different, and your structure may be slightly different. The main question, did you test and make sure your solution worked!

````{toggle}
```python
def get_positive_int(prompt : str) -> int:
    """Asks the user based on the prompt to enter a number. The
    number has to be either a number greater than 0 or an 'x'.
    If 'x' is entered, -1 is returned. Will continue to prompt if 0 or lower
    numbers are entered. :Does not do any error checking if non-digits are entered.:
    
    Examples:
        Assume client enters 10
        >>> get_positive_int("Enter the max number in your range: ") # doctest: +NORMALIZE_WHITESPACE
        Enter the max number in your range: 
        10

        Assume client enters x
        >>> get_positive_int("Enter a guess: ") # doctest: +NORMALIZE_WHITESPACE
        Enter a guess: 
        -1

        Assume client enters 0 followed by 2
        >>> get_positive_int("Enter a guess: ") # doctest: +NORMALIZE_WHITESPACE
        Enter a guess: 
        Invalid Number, try again (must be greater than 0): 
        2

    Args:
        prompt (str): A string to prompt the client

    Returns:
        int: either a number > 0, or -1 if client enters x
    """
    val = input(prompt)
    if val == 'x':
        return -1
    num = int(val)
    while num < 1:
        val = input("Invalid Number, try again (must be greater than 0): ")
        if val == 'x':
            return -1
        num = int(val)
    return num

def play_game(correct : int) -> bool:
    """Runs a guessing game in which the client guesses numbers greater than 0 until they guess the number. 
       They will be given feedback based on high, low, or correct using `check(guess, correct)`. They 
       can end the game early at any point returning False. 
    
    Example:
        Sample of game play. Assume the client enters 20, 5, 9, 10
        >>> play_game(10)  # doctest: +NORMALIZE_WHITESPACE
        Guess a number: 
        You guessed 20, that is High.
        Guess a number:
        You guessed 5, that is Low.
        Guess a number:
        You guessed 9, that is Low.
        Guess a number:
        You guessed 10, that is Correct.
        True

        Sample of game play. Assume the client enters 20, x
        >>> play_game(10)  # doctest: +NORMALIZE_WHITESPACE
        Guess a number:
        You guessed 20, that is High.
        Guess a number: 
        False

    Args:
        correct (int): the correct value

    Returns:
        bool: True if they found the value, False if they failed to find it.
    """
    result = None
    while result != 'Correct':
        guess = get_positive_int("Guess a number: ")
        if guess == -1:
            return False  ## early exit
        result = check(guess, correct)
        print(f"You guessed {guess}, that is {result}.")
    return True
```
````

### Focus on main()

When looking at `main()` there are two things that stood out. 

1. We never talked about giving the client instructions!
2. How do we handle a random number?

```{margin} Splash?
When you open an application and there is an image while it loads, that is called a splash screen. This was originally done in ascii art, and  it allowed the program to load information in the background while the client waited. It is even more common with applications with a lot of graphics, as it can take a bit to load those images into memory. 
```

For the first part, that is easy. We said above that you may come across additional functions as you develop, and having a function that prints out the instructions is one! We can even include a quick game welcome, so essentially a splash screen.

* Add to the process - printInstructions or `splash()` function. 
  * It will consist of just a series of print statements, and called first in `main()`
* Research random???

````{admonition} Random Numbers
:class: note
Random is actually pretty hard to generate with computers, and most languages have a built in way to find random. Searching online, we will find a reference to the python [random module](https://docs.python.org/3/library/random.html). Python has a **rich** library of created modules, that others wrote that can help you out. This is a common one. In our case, we need to find a function that generates a random `int` between the range of 1 and max. Scrolling through, there is a section 'Functions for integers' this looks promising! 

There are a couple function to use, but one function generates exactly what we need. 
```
random.randint(a, b)
    Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
```

So how does that look in python.
```python
from random import randint   ## place this at the top of your file!


def main():
    mx = 10 # this will change
    correct = randint(1, mx)
```

Since I imported the function `randint` I can use it directly in my code just like `print` or `input`. We will deal more with imports later, as there are different ways to import things. However, for now, you now have the ability to generate a random number!
````

```{epigraph}
Often programming is research - finding the right library or module you can use in your code!
```

#### Your Turn!
Given that information, go ahead and work in implementing main. 

#### Solution
Here is one possible solution for `main()` and `splash()`

````{toggle}

```python
def splash():
    """Prints a how to play dialog and welcome screen"""
    print("Welcome to the guessing game.")
    print("=============================")
    print("You will set the max value, and a random number will be selected.")
    print("You can then guess numbers. At any point, type x to end the game early.")
    print("=============================")

def main():
    """Main driver of the program"""
    splash()
    mx = get_positive_int("Enter the max for the range: ")
    if mx < 1:
        print("Invalid max, thank you for not playing.")
    else:
        correct = randint(1, mx)
        print("Random is set, good luck!")
        result = play_game(correct)
        if result:
            print("Congratulations! You won!")
        else:
            print(f"Sorry you didn't find the number, it was {correct}.")
```
````

#### Adding `__main__`

Right now, we have been adding the `main()` at the bottom of our file to launch our final program. However, that is not the traditional way to do it. In python, it is common to use this code at the bottom of the file.

```python
if __name__ == "__main__":
    main()
```

What that says is "if you are loading this file as the first file in your program, run this block of code". This gives me the ability to run the program, or just use the functions separately as needed. You can indeed include any code under the if statement, but for now, we will often just call the main driver for our program. 

```{margin} Solution Code
You will find solutions for a walk-through like this are in the [github repository](https://github.com/lionelle/computational-thinking-with-python). You are encouraged to download them and run them on your local computer, including the line that talks about running the built in tests. You can even clone the entire repository, and have it all on your computer. Explore! 
```

## Summary

For this program, we looked at the following.

1. The Big View - we broke the problem up into smaller parts
2. The Small View - we wrote the code for the smaller parts individually 

For every function, we
* define
* document
* implement
* test

Always before moving on. 

This process is one you should follow even for small programs, as you are learning the process of how to look at  programming. That process is known as **computational thinking**, and it takes practice. Above all, explore, struggle, and learn. 


## Play the game
Don't forget to play the game when you are done, and let others play it.

```{epigraph}
Can you come up with an algorithm that is quick at finding the answer?
```

1. maybe for one 1 - 10, you just start guessing numbers in order. Bad idea as with 1-100 that would take a while!
2. What if you instead divided by 2 each time, and guessed that?
   * 1 - 100 is range, you guess 50, the answer is high
   * your new range is 1-50, you guess 25, the answer is low
   * new range is 26-50
   * Until you narrow down the answer?

Algorithm 2 is a binary search! It is naturally **divide-conquer-glue**, and it dates back to roman times as a very fast algorithm for searching items that are in order.  The next chapter we will explore having more than one item or a list of items.


## Reflection

Take time to reflect. Reflection is one of five principles of recall, and is an *evidence based* practice on improving your understanding of material {cite:p}`roediger2012inexpensive`,{cite:p}`brown2014make`,{cite:p}`roediger2013applying`! It has been directly linked towards programming success {cite:p}`VanDeGrift2011`, {cite:p}`Stone2007`. As such, before you move onto the next chapter, we encourage you to write out in a journal/notebook/etc the following.

* What are concepts you understand the most? Can you imagine ways to use them in the future.
* What are concepts you find yourself struggling with? What are some resources that will help you understand them? See if you can come up with code examples of these concepts. 
* Reflect on the process of what you are learning, and how it applies not only to programming but problems around you on a day to day basis. 
* Reflect on items in your life that could benefit from a program to help with the task. Whether you know how to write it not, just think of solutions to things that could be improved with software.

