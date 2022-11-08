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
# 2.5 Repetition 

Since we can group code into blocks, like functions, and then we can conditionally code, we can look at how to cause blocks of code to repeat themselves. 


## Simple repetition

Let's say we want a menu to show until a client asks us to type 'x'. We could write such a menu as follows:

```python
def do_something(value):
    print(f"Hey, you entered: {value}" )

def menu():
    val = input("Enter a value: ")
    if val != 'x':
        do_something(val)
    else:
        print("Thank you for playing")

menu()
```
The program would run once. You can visualize the execution below assuming the input is five.
```{toggle}
<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20do_something%28value%29%3A%0A%20%20%20%20print%28f%22Hey,%20you%20entered%3A%20%7Bvalue%7D%22%20%29%0A%0Adef%20menu%28%29%3A%0A%20%20%20%20val%20%3D%20input%28%22Enter%20a%20value%3A%20%22%29%0A%20%20%20%20if%20val%20!%3D%20'x'%3A%0A%20%20%20%20%20%20%20%20do_something%28val%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22Thank%20you%20for%20playing%22%29%0A%0Amenu%28%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%225%22%5D&textReferences=false"> </iframe>
```
Or you can [run it yourself](https://pythontutor.com/render.html#code=def%20do_something%28value%29%3A%0A%20%20%20%20print%28f%22Hey,%20you%20entered%3A%20%7Bvalue%7D%22%20%29%0A%0Adef%20menu%28%29%3A%0A%20%20%20%20val%20%3D%20input%28%22Enter%20a%20value%3A%20%22%29%0A%20%20%20%20if%20val%20!%3D%20'x'%3A%0A%20%20%20%20%20%20%20%20do_something%28val%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22Thank%20you%20for%20playing%22%29%0A%0Amenu%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


The above code can be visually represented as:

```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart TD
    s([Start]) --> menu["menu()"]
    menu -->  val[/"enter a value"/]
    val -- "val" --> if{"val != 'x'"}
    if -- True --> do["do_something(val)"]
    if -- False --> p["Thank you for playing"]
    p --> e([End])
    do --> e
```

Now if we wanted to repeat, instead of ending after do something, we just go back to the menu.

```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart TD
    s([Start]) --> menu["menu()"]
    menu -->  val[/"enter a value"/]
    val -- "val" --> if{"val != 'x'"}
    if -- True --> do["do_something(val)"]
    if -- False --> p["Thank you for playing"]
    p --> e([End])
    do --> val
```

This tells us, that when it is true, we need to invoke both `do_something(val)` and then jump back to asking for input. To do this, we use a `while` loop.

```python
def do_something(value):
    print(f"Hey, you entered: {value}" )

def menu():
    val = input("Enter a value: ")
    while val != 'x':
        do_something(val)
        val = input("Enter a value: ")
    else:
        print("Thank you for playing")

menu()
```
### Visualize

This program will keep running until 'x' is entered. You can visualize the execution below assuming the input is `5`, `10`, `x`.
```{toggle}
<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20do_something%28value%29%3A%0A%20%20%20%20print%28f%22Hey,%20you%20entered%3A%20%7Bvalue%7D%22%20%29%0A%0Adef%20menu%28%29%3A%0A%20%20%20%20val%20%3D%20input%28%22Enter%20a%20value%3A%20%22%29%0A%20%20%20%20while%20val%20!%3D%20'x'%3A%0A%20%20%20%20%20%20%20%20do_something%28val%29%0A%20%20%20%20%20%20%20%20val%20%3D%20input%28%22Enter%20a%20value%3A%20%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22Thank%20you%20for%20playing%22%29%0A%0Amenu%28%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%225%22,%2210%22,%22x%22%5D&textReferences=false"> </iframe>

```

You can also [run it yourself](https://pythontutor.com/render.html#code=def%20do_something%28value%29%3A%0A%20%20%20%20print%28f%22Hey,%20you%20entered%3A%20%7Bvalue%7D%22%20%29%0A%0Adef%20menu%28%29%3A%0A%20%20%20%20val%20%3D%20input%28%22Enter%20a%20value%3A%20%22%29%0A%20%20%20%20while%20val%20!%3D%20'x'%3A%0A%20%20%20%20%20%20%20%20do_something%28val%29%0A%20%20%20%20%20%20%20%20val%20%3D%20input%28%22Enter%20a%20value%3A%20%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22Thank%20you%20for%20playing%22%29%0A%0Amenu%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)



````{Note}
In practice you, you do not need the `else` statement for most loops, as that code gets run when the loop is done. As such, the above can be rewritten as the following.

```python
def do_something(value):
    print(f"Hey, you entered: {value}" )

def menu():
    val = input("Enter a value: ")
    while val != 'x':
        do_something(val)
        val = input("Enter a value: ")
    print("Thank you for playing")

menu()
```

However, knowing you can have an else statement helps take care of some special conditions that can come up once in a while (pun intended).
````




## Looping With Functions?

Someone looking at the above flowchart could point out one could just reset the if/else line to `menu()` and it would loop! You are correct, and you can [vizualize such an execution](https://pythontutor.com/render.html#code=def%20do_something%28value%29%3A%0A%20%20%20%20print%28f%22Hey,%20you%20entered%3A%20%7Bvalue%7D%22%20%29%0A%0Adef%20menu%28%29%3A%0A%20%20%20%20val%20%3D%20input%28%22Enter%20a%20value%3A%20%22%29%0A%20%20%20%20if%20val%20!%3D%20'x'%3A%0A%20%20%20%20%20%20%20%20do_something%28val%29%0A%20%20%20%20%20%20%20%20menu%28%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22Thank%20you%20for%20playing%22%29%0A%20%20%20%20%20%20%20%20%0Amenu%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).

```{toggle}
<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20do_something%28value%29%3A%0A%20%20%20%20print%28f%22Hey,%20you%20entered%3A%20%7Bvalue%7D%22%20%29%0A%0Adef%20menu%28%29%3A%0A%20%20%20%20val%20%3D%20input%28%22Enter%20a%20value%3A%20%22%29%0A%20%20%20%20if%20val%20!%3D%20'x'%3A%0A%20%20%20%20%20%20%20%20do_something%28val%29%0A%20%20%20%20%20%20%20%20menu%28%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22Thank%20you%20for%20playing%22%29%0A%20%20%20%20%20%20%20%20%0Amenu%28%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%225%22,%22x%22%5D&textReferences=false"> </iframe>
```

This means you are thinking ahead and uncovering a concept called {term}`Recursion`, which a function is called within a function. Both loops and Recusion have their advantages. We will cover Recusion more in the future. 

## Summary
We have used if/else statements and while loops to help control the flow of our program. Let's work it all together with our overall program design in the next section. 


## Knowledge Check