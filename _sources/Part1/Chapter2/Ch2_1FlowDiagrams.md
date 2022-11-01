# 2.1 Flow Diagram

Taking a step back from the python language, let's talk about programming visually. An age old practice in programming is building a flowchart. The advantage of building a flowchart is that you can represent the algorithm/program in a way that is language independent. This flow also helps us visual paths for testing the program, and can help us understand the programming concepts themselves, as no  matter the language the concepts show up the same in the flowchart. This makes it easier to write our code, test our code, and even learn new languages. 

Let's look at the Million Dollar Sandwich example


```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart TD
    s([Start]) --> spreadB[Spread Peanut Butter]
    spreadB --> spreadJ[Spread Jam]
    spreadJ --> slice[Slice Strawberries]
    slice --> place[Place Strawberries on Jam]
    place --> join[Join pieces of bread together]
    join --> e([End])
```


You will notice that **Start** and **End** are both circles/ovals, while every *simple* step is a rectangle. However, what if we wanted to represent input/output? Let's look at our activity from {doc}`../Chapter1/Ch1_6DesignPrograms`, and redefine that as a flowchart. In order to do that, we will have to add a Rhombus slanting right to define input/output interaction. 

```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart TD
  S([Start]) --> gname[/Get Name/]
  gname --> gCyear[/Get Current Year/]
  gCyear --> gByear[/Get Birth Year/]
  gByear --> calc[Calc Age]
  calc --> p[/Print name is age./]
  p --> E([End])
```
```{important}
There are many standardized symbols used for flowcharts, often coming from the engineering schools of thought. For our use, we will use four common symbols.
* Circle/Oval - start, end, method call, return statement
* Rectangle - A simple action
* Rhombus - Input/Output/Data
* Diamond - Choices (talked about in {doc}`Ch2_2FlowBranching`)
```

Right away, we can follow the flowchart, and get an idea of each of our steps in our code. For the most part, each individual action is an item, and as you define functions, you create additional flow charts. You can even link to the additional flow charts, as follows.

```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart TD
    subgraph getYear[Get Year]
        S2([Start])
        S2 --> prompt[/Print Prompt/]
        prompt -- value --> int[Convert value to int]
        int --> E2([return int])
    end
   
    subgraph main
        S([Start]) --> gname[/Get Name/]
        gname --> gCyear[/Get Current Year/]
        gCyear --> gByear[/Get Birth Year/]
        gByear --> calc[Calc Age]
        calc --> p[/Print name is age./]
        p --> E([End])
    end
   
    gCyear --> S2
    gByear --> S2
    E2 --> gCyear
    E2 --> gByear
```

But then that gets complicated. It is more common to just give IDs to charts, and list them separately. What if we wanted to add the ability to make choices and repeat actions?