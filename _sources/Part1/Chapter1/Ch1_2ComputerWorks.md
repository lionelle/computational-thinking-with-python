# 1.2 How does it all work? 

We will slowly dive into the multiple components and how it works together throughout the book, but for now, the important part to understand is that a computer processes {term}`Files`. Everything we work with is a file, a stored *state* of information, that is processed by the computer, including programs! 

A written program is a {term}`Text File` that contains the recipe for the machine to follow, after it is first passed through a phase that converts the Text File to machine readable code. In Pythons case, that is called an {term}`Interrupter`. Or another way to word it, you write in english a recipe to follow and that is the song you are creating for the machine to play! That is it. Really! 


A computer is made up of multiple major grouping of parts all called {term}`Hardware`. You have the devices that do the work and store the information, that is often the part people call computer. You have {term}`Input Devices` that takes information from the {term}`Client`, you probably know these devices such as keyboard and input. However, your program doesn't have to handle it directly! Instead, the {term}`Operating System` handles that input, and sends it to your program! Your program then tells the operating system it want's to share information with the client, this is done through {term}`Output Devices`. 

```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart LR
    Hardware-->OS["Operating System"]
    OS-->Interrupter
    Interrupter[Interrupter]-->Code[Your Program]
    Code-->Interrupter
    Interrupter-->OS
    OS-->Hardware
    Hardware-->Client
    Client-->Hardware
```

Looking at the diagram above, you will notice that every part talks with the next stage, and everything is modularized. Your program doesn't have to talk to the hardware directly, but it can assume by passing the information through the Interrupter to Operating System, that the OS will then print to the screen, display an image, or collect information from the client such as keyboard input, and then it goes along the chain to your program.  Since these are links in a chain, one can change out a link, and the later links still work.

Better yet, lets look at some actual python code

## Hello, World!
A class program is simply printing `Hello, World!` to the screen. Using the interactive programming window below, click the **run** button.  If the `Output:` statement is not next to the highlighted code, you  may need to increase the width on your screen. 

<iframe
 frameBorder="0"
 height="450px"  
 src="https://onecompiler.com/embed/python/Python%20Hello%20World?hideLanguageSelection=true&hideNewFileOption=true&hideTitle=true&hideNew=true&hideStdin=true" 
 width="100%"
 ></iframe>

```{admonition} TASK: Give it a try!
:class: tip
Whenever you see code, you should play with it! You will also see tasks like the following, try to do them for better understanding.

☑ Change "Hello, World!" to be your name, so for example, "Hello, Ada!" and click run again. Be careful about the quotes!
```

## main.py??
You will notice there is a tab that says main.py. That is actually the File Name of your code file. When you program, you will need to save your code into a file before you run it! The file is a {term}`Text File` with the {term}`File Extension` of {term}`.py` for python file. However, it is still a text file, just one that has specific syntax related to programming. 

### Text Files to Computer Code
```{sidebar} Shout out! Grace Murray Hopper 
Grace Murray Hopper created one of the first compilers for a language she created called COBOL. She started working with cryptography in the Navy after World War II and eventually became an admiral in the 80s. Her work was essential to modern computer science. [Learn more about Grace Murray Hopper](https://president.yale.edu/biography-grace-murray-hopper).
```

You will find many files you deal with daily are text files with various "markup" or specific formatting to them. HTML (Hypter Text Markup Language) is the primary final extension for website files. CSV is a comma separated value file used for cell based data like you see in excel. And most programming files are simply text files with a very specific syntax you follow. A program such as an interpreter or compiler will then read your text file, and convert it into something your computer can process.


Now that we have some of the basics, let's start programming!

