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

# 1.3 Let's Program!

You have already programmed on the last page, when you modified the code provided, and then clicked run. Behind the scenes, the browser takes the text file, sends it to the Python {term}`Interrupter`, and then collects the results to display in your browser. You program is always interacting with provided components from the computer. While this wasn't always the case, and many programmers such as Alan Turing and Jean Valentine of the Bombe Machine had to write the program directly in the computer, the modern world of programming is much simpler. Through there work, and the work of countless others, you can focus on the problem, write your code in very specific version english, and then your computer will run it!

## 1.3.1 Programs are in english!
People talk about programming as learning a new language, and while there is some truth, the fact is you are actually learning a very specific way to format english. This format allows another program (the Interrupter) to convert it to instructions for the computer to handle.  The difficulty then comes in two parts

* The formatting has to be **exact**. This can be frustrating, and every programmer has wanted to toss their computer out the window. Why? Because it can be something so small like missing a space, but it can be difficult to see the error! 
  * How do you handle that? Take a breath, walk away, and come back. Often the solution presents itself. 
* The logic behind building the problem, or more importantly, developing a different way at looking at the world and problems. 
  * A new way of thinking can be difficult, and this focuses more on the this problem. The most important thing will be taking everything in *small* steps. _Never_ write all your code at once. Instead, write a few lines, test, a few lines and test! We will continue to come back to this. 

```{epigraph}
Never write all your code at once. Instead, write a few lines, test make sure it works, then write a few more, and repeat. 
```

## 1.3.2 Python 
In this book, you will be using Python to help you learn computer science concepts, including how to design programs. This is intentionally stated, as this book is not focused on learning python. Instead, it is focused on key concepts and ideas that are needed to help you become a better programmer. Python was first designed by [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) in the late 1980's. It has a large volunteer community base that prides itself on diversity of contributors. It is popular in many fields including computer science, data science, general sciences, english and liberal arts, and more partially because of the large library base and simplicity in reading the code. However, it is also a very rich language with features you won't begin to touch in this book, and that is alright! Often with computer science we learn the foundation, and then as we explore new concepts, we find the tools that we need. In the end, Python is a language, and a {term}`Programming Language` is a tool in which we learn to play the computer. You often pick which tool is best given the problem and domain. 

Programming is made up of simple instructions the computer follows. Given the following instruction, the result is below it.

```{code-cell}
2 + 2  
```

We have `2 + 2`, and what the computer sees is that we want to add two numbers together. It calculates the result, and the number that gets put there is `4`. However, what happens if to that four? Can we reuse it? Have we assigned a way to find it again? This brings us to an important part of programming. A {term}`Variable` is a way we can name a value to use it again later. 



```{code-cell}
meaning = 40 + 2
name = "Ada Lovelace" # notice the quotes
```

```{margin} A Comment?
In python, when you place a pound (`#`) sign, anything after it on the line is a comment. A comment gets ignored by the interrupter, and you should use them a lot talking about the code. 
```

We now have stored the value 42 into a variable called `meaning`. We have also stored a string called "Ada" inside the variable `name`. For reference, a just like a word, but it can include any and all characters such as spaces. Storing these values into variables, allows us to do other things with the value.

```{code-cell}
print(meaning)
print("The answer to life, the universe, and everything is", meaning)
# below prints who the first programmer was
print("The first programmer was", name)
```

In the above example, we print 42 and then we print a nearly complete sentence. Two major questions come to mind, 

1. Is there a better way to write the print?
2. What is this `print` statement?

For the first question, we wanted to share it as we will commonly use "f" strings throughout this book. An f-string is a format string that includes formatting information inside the string.  As such, a more common way to write the above statement is:

```{code-cell}
 # notice the f before the quote
print(f"The answer to life, the universe, and everything is {meaning}.")
```

The f-string takes any variables and will insert it. We will explore some of the formatting features more in the future. 

## 1.3.3 print()?

Print takes the values you put into it and prints them to the screen. Going more in depth, `print()` is a {term}`Function` or a way that a reusable block of code is defined. In this case, someone else has written the code that interacts with the computer to print to the screen. You don't have to write the code that interacts with the OS and hardware, and that is great! It is also critical to start early with functions, as programmers who break their code up into smaller reusable chunks are successful programmers.


## 1.3.4 Visualizing Your Code

The best way to visual code is to draw it out. Throughout this book we will give techniques on drawing it, and you will also see us embed a tool that handles python visualizations through the book. 

Let's try visualizing code similar to above.
<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=meaning%20%3D%2040%20%2B%202%0Aname%20%3D%20%22Ada%20Lovelace%22%0Aprint%28f%22The%20answer%20to%20life,%20the%20universe,%20and%20everything%20is%20%7Bmeaning%7D.%22%29%0Aprint%28f%22The%20first%20programmer%20was%20%7Bname%7D.%22%29%0A%0A%23%20end%20program,%20it%20will%20ignore%20this%20line&codeDivHeight=400&codeDivWidth=350&cumulative=true&curInstr=0&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D"> </iframe>

Hitting next, you will see two columns generated **frames** and **objects**. Let's focus on frames. The Global Frame is the a place in which variables are stored in memory. You have the variable meaning pointing towards the value 42. 


## Knowledge Checks 

TO ADD