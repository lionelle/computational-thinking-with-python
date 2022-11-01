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

# 1.6 Divide-Conquer-Glue (aka Designing Programs)

You are learning some of the basic syntax of programming, but what is more important is how you look at he problems, break them down, and solve them. Problems itself is problematic, as while programmers are technically problem solvers, they don't often view everything they are doing is a problem! Don't get caught up on the word, and think of it as more of tasks and building. 

The primary means in which we look at problems is via **Divide-Conquer-Glue**. Let's take the following scenario, and break it down before we write code.  

```{admonition} Scenario
   
   Your client has a database of ages, and knows the current year. He wants to be able to type the name of the person, the year they were born, and the current year, and your program is to give them the age. (sound familiar?)
```

```{margin} Programmers Notebook
   Some programmers keep notebooks to help them with design, and instead of typing out the tasks, they sketch them in their notebook. You should try it out!
```
Now the question becomes, how do we take this idea, and break it up into a program. The first stage is **writing down** often as a comment in your file the various tasks you have to accomplish!

```python
# 1. Type name of client
# 2. Type year they were born
# 3. Type current year
# 4. Calculate age from born and current year
#    * Note: will need to convert from input to int
# 5. Print out the age 
#    * Probably should include name also, ask client on exact format 
#    * If this was an assignment, you should ask!
```
You should open up a file and type the stuff above. For clarity, displaying it as part of the page below. 

1. Type name of client
2. Type year they were born
3. Type current year
4. Calculate age from born and current year
   * Note: will need to convert from input to int
5. Print out the age 
   * Probably should include name also, ask client on exact format 
   * If this was an assignment, you should ask!

## Decomposition
Taking the tasks steps above, we can break the program up into three major components.

````{grid}
:gutter: 3

```{grid-item-card} Input
Collect Data From Client
* Name
* Current Year
* Birth Year

- Convert Years to `int`
- Needs: input from client
```

```{grid-item-card} Calculations
Take Current Year minus Birth year

- Needs: current_year as `int`
- Needs: birth_year as `int` 
```

```{grid-item-card} Output
Print out age and person's name


- Needs: age from Calculations
- Needs: name from Input
```
````

````{margin}
   ```{important}
   "This is a lot of work for a small program".
   
   Remember, you are training your mind to look at these problems. They 
   may start small now, but make sure to **practice the process**, for when 
   programs get very, very large!
   ```
````
### Evaluation and Repeat
For each of these stages in the program, we should be able to ask.

1. Are they sufficiently small that we can isolate the tasks?
   * If it isn't true, we take the stage and start the process again for that stage. 
   * This gives layers of decomposition. 
2. Can each stage be fully tested with mock (made-up) inputs without the other stage?
   * This condition isn't always true, but the closer we can make it, the better. 

For each stage, we can say, yes - though there may be way to break down stage one into two components. 

## Abstraction

Looking at the **Input** stage of this program, we start thinking about what parts are in common, and can we represent them more abstractly, in a more generalized manner. 

1. Getting the name requests input from the client and is going to need to set a `str` value. 
2. Getting the current year is going to need input from a client (that is a whole number) and return an `int`.
3. Getting the birth year is going to need input from a client (that is a whole number) and return an `int`.

Right there you see current year and birth year are performing the same task, the only difference is the prompt (string message) you use for the client. As such, we could further break that down into a component.

````{card} get_year
Prompts a user with a message, and returns an `int` value the represents a year. 

* Needs: `str` message for prompt
* Returns: `int` year
````

```{margin} Strange Syntax?
The *: type* and *-> return type* syntax is actually valid python syntax, but it is optional. Many industry standards require that programmers put them into their code. We will use it for descriptions at this point, but we won't put it in most of the code so it is easier to read. Later in this book, we will start including them in the code as the programs become more complex.
```

Combining it all together, I believe I have the following functions to write for the **Input** stage. Note
the *->* symbol reminds us of what it is going to return from the function, and the *: type* tells me
what I am expecting. We will explore this more in the future, but for now it is safe to use it
in your design.  

* `get_name() -> str` 
* `get_year(prompt: str) -> int`

### Repeating This Process
We should repeat this process for every stage defined. However, in the Calculations and Output stages,
we really only have one action each. Giving us the following functions

* `get_age(current_year: int, birth_year: int) -> int`
* `print_results(name: str, age: int)` 
  * Notice, this doesn't actually return anything. 

## Documenting
We are almost to writing code, in fact we can now write our method definitions and our docstring! This process is often called "stubbing" or "function stubs" your code. 

```{code-block}
def get_name():
   """ Prompts the client to enter name of the individual.
       For example,

        >>> get_name() # client enters Ada Lovelace
       Enter a name: 
       'Ada Lovelace'
       >>> get_name() # client enters Trillian Astra
       Enter a name: 
       'Trillian Astra'
      

      :return: The value returned by the input
      :rtype: str
   """

def get_year(prompt):
   """ Prompts the user with `prompt` requesting a year. For example:
       `get_year("What is the current year? ")` would print to the screen
       "What is the current year? " and wait for the client to enter
       a whole number. The whole number is converted to an int. For example,
      
        >>> get_year("Current Year ")  # client enters "2022" 
       Current Year 
       2022
       >>> get_year("Current Year ")  # client enters "2525" 
       Current Year 
       2525
       >>> get_year("Other Message ") # client enters "1979" 
       Other Message 
       1979
       >>> get_year("Birth Year ") # client enters "1224" 
       Birth Year 
       1224 

       :param prompt: Message to show to the user, make sure to include space at the end
       :type prompt: str

       :return: The whole number of the value entered
       :rtype: int  
   """
```
### Practice
Based on the examples above, complete the other function docstrings in the box below. 

```{important}
The docstrings should include some tests, with expected output. It is actually following the format if you typed out
the function call in the python interrupter directly. This format includes. `>>>` at the start of the function call, a space
and the function call with the parameter values you are testing it with. Then immediately on the next line, the expected value
to either be printed or returned. For values that require inputs, you write out the prompt to the screen and then on the
next line the returned value. If the returned value is a string use single quotes. 

While we are writing the tests ourselves for now, this type of format is common in python, and allows you to run
`doctests` on the file itself confirming validity. The solution file for this section is ran using doctests. 
```



<iframe
 frameBorder="0"
 height="450px"  
 src="https://onecompiler.com/embed/python/3ymmashx7?hideLanguageSelection=true&hideNewFileOption=true&hideTitle=true&hideNew=true" 
 width="100%"
 ></iframe>

## Writing Code

You now broken up your clients request into smaller parts, clearly defined what functions you are going to write, and even provided yourself with examples on how to confirm you wrote the function correctly. Let's start coding. We will work on one function together, and the rest you will do on your own.  The `get_age` function
we have completed in {doc}`Ch1_5Functions` in the check_age example. We will start with that one. Your docstring may differ. You should feel to write the code in the programming window above or in your own {term}`IDE`. 

```{code-cell}
def get_age(current_year, birth_year):
   """ Takes the current year minus the birth year, and returns the result.
       There is no error checking, it will return the value of whatever
       numbers are provided. For example,

      >>> get_age(2022, 1980) 
      42
      >>> get_age(2525, 1979) 
      546
      >>> get_age(2022, 2022) 
      0
      
      It currently does not factor invalid age ranges, as the the following 
      would be valid.
      >>> get_age(2022, 2023)
      -1
      

      :param current_year: the current year as a whole number
      :type current_year: int
      :param birth_year: the birth year as a whole number
      :type birth_year: int
      :return: the current_year - birth_year 
      :rtype: int
   """
   return current_year - birth_year

```

## Validate Code
**Before** we move onto my next function, we should write some tests. Right now, the tests seem simple, but eventually, it will be critical.  To write a test, add a function call at the bottom of your file. We also like to include a print line, so we can see what is going on!

```{code-cell}
print("------ TESTS -------")
is42 = get_age(2022, 1980)
print(f"`get_age(2022, 1980)` should return 42, returns: {is42}")
is546 = get_age(2525, 1979)
print(f"`get_age(2525, 1979)` should return 546, returns: {is546}")
is0 = get_age(2022, 2022)
print(f"`get_age(2022, 2022)` should return 0, returns: {is0}")
print() # just adds an empty line at the bottom of my output
```

```{important}
By following the tasks of design, document with tests defined, write code, and validate, We had everything laid out for us at each next step! These seems like a lot of steps now, but in the long run, you will end up writing much more efficiently in the future. 
```

We will explore how to come up with test cases in the future, but for now, just simply try to think through what is expected of each function you write. At this stage, we can say "get_age is done", and we no longer have to worry about it. We don't have to worry how it is implemented, we can just call it as we need in our code. Similar to how you call print in your code, you don't care how it works, just that it works. This is called *black box* testing. Once we know a function works, it is a black box that we no longer need to see the contents. 

```{epigraph}
Black box testing is essential to efficient software development. 
```

### Practice
Your turn! Go ahead and write each function, and make sure to write
tests at the bottom of the file after each function. 

Testing client input and output can be tricky, as you don't have set inputs and return types. Instead you may modify the test to be more interactive.

```{margin} Software Testing 
   Within computer science there is an entire field tied to software testing and validation. They have sophisticated techniques to make sure every line of  program is tested and meets validation. However, the problem is hard and expensive on companies, so it is an open field of research. 

   Why would it matter, other than we have all experienced a buggy program? Imagine if you were writing software for space shuttle launches or the next smart car. Testing and validation at every stage of the process is life critical for people!
```

```{code-block}
print("Test1: get_name(), entering 'Ada Lovelace'")
name = get_name()
print(f"Test1: returns {name}")
# probably add one more test as this is straight forward
print()

#now test for get_year()
cyear1 = get_year("T1: Enter Year: ')
print(f"Test1: get_year('Enter Year ') with 2022 entered returns {cyear1}")
byear1 = get_year("T1: Birth Year: ')
print(f"Test1: get_year('Birth Year ') with 0020 entered returns {byear1}")
## some other tests
print()

# tests for output
print("print_results('Ada Lovelace', 22) should print to the screen 'Ada Lovelace is 22.")
print_results('Ada Lovelace', 22)
## add more tests

```



## Glue
We have written our components, tested to make sure they work, but we have yet to build the full working program! To do that, this requires us either adding the lines to the file, or writing another function whose main purpose is to handle the *glue* of the program. We will use another function, in order to keep our code clean. 

```{code-block}
def main():  # this is the common name for the starting point of a program!
   """ A simple program that asks a client for a name, a current year,
       and the birth year of an individual. Will print out
       {name} is {age}.
   """
   name = get_name()
   current_year = get_year("What is the current year? ")
   birth_year = get_year("What is the birth year? ")
   age = get_age(current_year, birth_year)
   print_results(name, age)


## then before my tests, but at the end of my code we add
main()
```
```{tip}
Don't forget to comment out your tests! 
```
You will notice a few things about the  main() function. This function doesn't do any real work. Instead, it is calling other functions, and simply storing the returned result. Each function it calls is a very isolated task, that by itself may not make sense, but when put together in the main() we have a working program. 


Often times, you will multiple glue methods in your program, and it all depends on how many layers of decomposition was needed in the design. Each layer is often a point in which we need to bring concepts together. 

> View the [final solution with code tracing](https://pythontutor.com/render.html#code=def%20get_name%28%29%3A%0A%20%20%20%20%22%22%22%20Prompts%20the%20client%20to%20enter%20name%20of%20the%20individual.%0A%20%20%20%20%20%20%20For%20example,%0A%0A%20%20%20%20%20%20%20%3E%3E%3E%20get_name%28%29%20%23%20client%20enters%20Ada%20Lovelace%0A%20%20%20%20%20%20%20Enter%20a%20name%3A%20%0A%20%20%20%20%20%20%20'Ada%20Lovelace'%0A%20%20%20%20%20%20%20%3E%3E%3E%20get_name%28%29%20%23%20client%20enters%20Trillian%20Astra%0A%20%20%20%20%20%20%20Enter%20a%20name%3A%20%0A%20%20%20%20%20%20%20'Trillian%20Astra'%0A%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%3Areturn%3A%20The%20value%20returned%20by%20the%20input%0A%20%20%20%20%20%20%3Artype%3A%20str%0A%20%20%20%20%22%22%22%0A%20%20%20%20return%20input%28%22Enter%20a%20name%3A%20%22%29%0A%0A%0Adef%20get_year%28prompt%29%3A%0A%20%20%20%22%22%22%20Prompts%20the%20user%20with%20%60prompt%60%20requesting%20a%20year.%20For%20example%3A%0A%20%20%20%20%20%20%20%60get_year%28%22What%20is%20the%20current%20year%3F%20%22%29%60%20would%20print%20to%20the%20screen%0A%20%20%20%20%20%20%20%22What%20is%20the%20current%20year%3F%20%22%20and%20wait%20for%20the%20client%20to%20enter%0A%20%20%20%20%20%20%20a%20whole%20number.%20The%20whole%20number%20is%20converted%20to%20an%20int.%20For%20example,%0A%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%3E%3E%3E%20get_year%28%22Current%20Year%20%22%29%20%20%23%20client%20enters%20%222022%22%20%0A%20%20%20%20%20%20%20Current%20Year%20%0A%20%20%20%20%20%20%202022%0A%20%20%20%20%20%20%20%3E%3E%3E%20get_year%28%22Current%20Year%20%22%29%20%20%23%20client%20enters%20%222525%22%20%0A%20%20%20%20%20%20%20Current%20Year%20%0A%20%20%20%20%20%20%202525%0A%20%20%20%20%20%20%20%3E%3E%3E%20get_year%28%22Other%20Message%20%22%29%20%23%20client%20enters%20%221979%22%20%0A%20%20%20%20%20%20%20Other%20Message%20%0A%20%20%20%20%20%20%201979%0A%20%20%20%20%20%20%20%3E%3E%3E%20get_year%28%22Birth%20Year%20%22%29%20%23%20client%20enters%20%221224%22%20%0A%20%20%20%20%20%20%20Birth%20Year%20%0A%20%20%20%20%20%20%201224%20%0A%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%3Aparam%20prompt%3A%20Message%20to%20show%20to%20the%20user,%20make%20sure%20to%20include%20space%20at%20the%20end%0A%20%20%20%20%20%20%20%3Atype%20prompt%3A%20str%0A%0A%20%20%20%20%20%20%20%3Areturn%3A%20The%20whole%20number%20of%20the%20value%20entered%0A%20%20%20%20%20%20%20%3Artype%3A%20int%20%20%0A%20%20%20%22%22%22%0A%20%20%20return%20int%28input%28prompt%29%29%20%0A%0A%0Adef%20get_age%28current_year,%20birth_year%29%3A%0A%20%20%20%22%22%22%20Takes%20the%20current%20year%20minus%20the%20birth%20year,%20and%20returns%20the%20result.%0A%20%20%20%20%20%20%20There%20is%20no%20error%20checking,%20it%20will%20return%20the%20value%20of%20whatever%0A%20%20%20%20%20%20%20numbers%20are%20provided.%20For%20example,%0A%0A%20%20%20%20%20%20%3E%3E%3E%20get_age%282022,%201980%29%20%0A%20%20%20%20%20%2042%0A%20%20%20%20%20%20%3E%3E%3E%20get_age%282525,%201979%29%20%0A%20%20%20%20%20%20546%0A%20%20%20%20%20%0A%20%20%20%20%20%20It%20currently%20does%20not%20factor%20invalid%20age%20ranges%20%0A%20%20%20%20%20%20would%20be%20valid.%0A%20%20%20%20%20%20%3E%3E%3E%20get_age%282022,%202023%29%0A%20%20%20%20%20%20-1%0A%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%3Aparam%20current_year%3A%20the%20current%20year%20as%20a%20whole%20number%0A%20%20%20%20%20%20%3Atype%20current_year%3A%20int%0A%20%20%20%20%20%20%3Aparam%20birth_year%3A%20the%20birth%20year%20as%20a%20whole%20number%0A%20%20%20%20%20%20%3Atype%20birth_year%3A%20int%0A%20%20%20%20%20%20%3Areturn%3A%20the%20current_year%20-%20birth_year%20%0A%20%20%20%20%20%20%3Artype%3A%20int%0A%20%20%20%22%22%22%0A%20%20%20return%20current_year%20-%20birth_year%0A%0A%0Adef%20print_results%28name,%20age%29%3A%0A%20%20%20%22%22%22%20Prints%20to%20the%20screen%20%7Bname%7D%20is%20%7Bage%7D%20based%20on%20parameters.%20For%20example%3A%0A%20%20%20%20%20%20%0A%20%20%20%20%20%20%3E%3E%3E%20print_results%28'Ada%20Lovelace',%2022%29%20%0A%20%20%20%20%20%20Ada%20Lovelace%20is%2022.%20%20%20%0A%20%20%20%20%20%20%3E%3E%3E%20print_results%28'Trillian%20Astra',%2042%29%20%0A%20%20%20%20%20%20Trillian%20Astra%20is%2042.%0A%20%20%20%20%20%20%0A%20%20%20%20%20%20%3Aparam%20name%3A%20the%20name%20of%20the%20person%0A%20%20%20%20%20%20%3Atype%20name%3A%20str%0A%20%20%20%20%20%20%3Aparam%20age%3A%20the%20age%20of%20the%20person%0A%20%20%20%20%20%20%3Atype%20age%3A%20int%0A%20%20%20%22%22%22%0A%20%20%20print%28f%22%7Bname%7D%20is%20%7Bage%7D.%22%29%0A%0A%0Adef%20main%28%29%3A%20%20%23%20this%20is%20the%20common%20name%20for%20the%20starting%20point%20of%20a%20program!%0A%20%20%20%22%22%22%20A%20simple%20program%20that%20asks%20a%20client%20for%20a%20name,%20a%20current%20year,%0A%20%20%20%20%20%20%20and%20the%20birth%20year%20of%20an%20individual.%20Will%20print%20out%0A%20%20%20%20%20%20%20%7Bname%7D%20is%20%7Bage%7D.%0A%20%20%20%22%22%22%0A%20%20%20name%20%3D%20get_name%28%29%0A%20%20%20current_year%20%3D%20get_year%28%22What%20is%20the%20current%20year%3F%20%22%29%0A%20%20%20birth_year%20%3D%20get_year%28%22What%20is%20the%20birth%20year%3F%20%22%29%0A%20%20%20age%20%3D%20get_age%28current_year,%20birth_year%29%0A%20%20%20print_results%28name,%20age%29%0A%0A%0Amain%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).


````{margin}
   ```{important}
      When presented with solutions, you should try run them using code tracing. Ask yourself questions! 
      The arrow symbol next to the link encourages you to open it in a new tab by right clicking on it. 

      You can also find chapter solutions by going to the public GitHub repository linked to the top of each page.
   ```
````

## Designing with modification in mind
This program seems simple. However, what if instead of the person entering in the current year, you calculate it based off of information stored in the computer. Furthermore, since the database stores birth dates, you pull the birthday from the database? Another feature could be narrowing down birthday using the month and day, so it is exact.  Finally, a modification could be sending the person an email birthday card automatically.

What started off like a simple program grows *but* the key components still remain the same, and with every feature update, you end up updating only small portions of your code. This only works because we broken the problem up into smaller concepts, and wrote around those smaller concepts! 

Finally, what our program didn't include is error checking. For example, what if they entered "twenty-two" instead of "2022" for the current year, or just mistyped something. In the next chapter we will explore some error checking techniques, that will help our code be more robust. 

## A Word on Error Checking
You will have errors. Errors are often broken into three categories

* {term}`Syntax Errors` - these are caught before the program runs, everyone has them.
* {term}`Runtime Errors` - these errors crash a program while it runs, for example giving `int()` something like `int("hi")`. It will compile, but it will crash throwing a runtime error. You will learn to test with cases to generate these errors, so you can find them in your validation stage.
* {term}`Logic Errors` - these are errors where everything works right, but right does not mean it works correctly. For example, someone enters 2022 for current year and 2023 for birth year,  -1 is not a valid age. However, the program worked rightly, just not correctly. These are on the programmer to catch with validation and more importantly, your own validation of the results. 

Computers are very powerful, but they are also very stupid. They do exactly what you tell them to do, without variation. This means most errors, whether we like it or not, are often our fault. That means we have to continually look at our code and validate what we are doing **as we are doing it**. Some guiding principles are:

1. **Write Incrementally** - Write only a few lines at a time, and test. Your tests don't have to be logically valid, they are there so you as the programmer knows that it compiles and that you understand what is going on. Adding print randomly throughout your code will help!

2. **Validate Incrementally** - Test your code at every function. Don't wait until you have written everything to test. 

3. **Check your assumptions** - You should constantly look at what you assume is going on, and find out what is really going on. Often assumption from client specifications get us in trouble, so any time you have a question, there is usually a person in the process to ask! Specifications are rarely that clear, which is why some people dedicate their careers to working with clients on gathering specifications. 

4. **Collaborate** - The idea of a programmer working alone in a basement, ever talking to others is completely false. Programming is a social activity in which we often have to work together to solve problems. While sharing code is rarely beneficial (and plagiarism), talking with others about concepts, ideas, and going over problems is essential to success. 
   
5. **Art and Logic** - There is important logic and structure to programmer, but there is also art to programming. The art is creatively coming up with ideas. That means a programmer is constantly switching from different sides of their brain as they look at problems. Embrace the art and the logic both!


Above all.... *practice, practice, practice*. You are learning an instrument, and the only way to get better at it is practicing. 

## Reflection

Take time to reflect. Reflection is one of five principles of recall, and is an *evidence based* practice on improving your understanding of material {cite:p}`roediger2012inexpensive`,{cite:p}`brown2014make`,{cite:p}`roediger2013applying`! It has been directly linked towards programming success {cite:p}`VanDeGrift2011`, {cite:p}`Stone2007`. As such, before you move onto the next chapter, we encourage you to write out in a journal/notebook/etc the following.

* What are concepts you understand the most? Can you imagine ways to use them in the future.
* What are concepts you find yourself struggling with? What are some resources that will help you understand them? See if you can come up with code examples of these concepts. 
* Reflect on the process of what you are learning, and how it applies not only to programming but problems around you on a day to day basis. 
* Reflect on items in your life that could benefit from a program to help with the task. Whether you know how to write it not, just think of solutions to things that could be improved with software.