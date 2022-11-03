# 2.2 Allowing Choices in Flowcharts

Life is made up of choices. Do you cross the street here, or take a left? Do you continue chopping carrots or stop? Most of these choices can be boiled down to a series of Yes and No questions, or more formally thought about as True or False. It is also called a binary (two options) situation often represented as 1 is True and 0 is False. 

With flowcharts we represent a choice with a diamond.

```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
    flowchart TD
        id{Use Strawberry Slices<br> with PB&J}
        id --True--> place[Place Slice on Bread]
        id -- False --> join
        place --> join[Join pieces of bread together]
```

## Conditions
Life also has conditions, and we were taught some ways to represent these conditions in high school algebra. 

| Condition | Prose |
| -- | -- |
| $a >  b$| is $a$ *greater than* $b$ |
| $a < b$ | is $a$ *less than* $b$ |
| $a >= b$  | is $a$ *greater than or equal to* $b$ |
| $a <= b$  | is $a$ *less than or equal to* $b$ |

Combining the two ideas, let's look back at our program from {doc}`../Chapter1/Ch1_6DesignPrograms`.

## Branching With Flowcharts

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

Now, lets say before we calculate age, we want to check to make sure the current year is higher than the birth year. We could modify our flow diagram to include that choice.

```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart TD
  S([Start]) --> gname[/Get Name/]
  gname --> gCyear[/Get Current Year/]
  gCyear --> gByear[/Get Birth Year/]
  gByear --> cond{birth year < current year}
  cond -- True --> calc[Calc Age]
  cond -- False --> notP[/Print not possible!/]
  calc --> p[/Print name is age./]
  p --> E([End])
  notP --> E
```

Adding conditions greatly increases the types of actions we can do, and improves our algorithms.  However, in the example above, if `birth year` equals `current year`, it follows the `False` pathway in the flowchart. This is because it isn't strictly True with the less than condition. That may be intentional, or maybe, I want to do something special if they are a new born!


```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart TD
  S([Start]) --> gname[/Get Name/]
  gname --> gCyear[/Get Current Year/]
  gCyear --> gByear[/Get Birth Year/]
  gByear --> cond{birth year < current year}
  cond -- True --> calc[Calc Age]
  cond -- False --> isNewBorn{birth year <br> equals <br> current year}
  isNewBorn -- True --> yayP[/Print welcome newborn!/]
  isNewBorn -- False --> notP[/Print not possible./]
  calc --> p[/Print name is age./]
  p --> E([End])
  notP --> E
  yayP --> E
```

We just added another condition (choice!) in our flowchart, and we ended up with three possible outcomes to our program. We can see the checks happen in order, and we can see the results of each condition. We now have a very visual representation of our code. 

## Repeating Actions

Let's say we have three strawberries we want to slice for our Million Dollar Sandwich. This is the same action for every strawberry, just repeated three times, or stated another way, repeated until done. After each slice, we mentally ask ourselves is it done, and if not, we keep going. Essentially, a True/False condition on to repeat or be done. 

With a flowchart, that is still represented as a Diamond, as you look at the condition, and based on the condition you mark the step you want to repeat. Going back to our Age example, what if we wanted the client to continue to enter years until the years they enter are valid? We can modify the flowchart simply by changing where our line goes!

```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart TD
  S([Start]) --> gname[/Get Name/]
  gname --> gCyear[/Get Current Year/]
  gCyear --> gByear[/Get Birth Year/]
  gByear --> cond{birth year < current year}
  cond -- True --> calc[Calc Age]
  cond -- False --> isNewBorn{birth year <br> equals <br> current year}
  isNewBorn -- True --> yayP[/Print welcome newborn!/]
  isNewBorn -- False --> gCyear
  calc --> p[/Print name is age./]
  p --> E([End])
  yayP --> E
```

This tells us that we have a loop in my code that requires the client to enter valid values for Current Year and Birth Year. In practice, it may make sense to set it up other ways, but this gives an idea of what is going on. Since each of these actions was a function call, I also can start thinking about how this would convert to code by just calling the `getYear()` function again. 

```{margin} Software Testing
Within software testing, flow diagrams for code are so common, there is actually software that will read your code and generate a modified flow diagram. This diagram can then be compared with your tests to make sure you test every pathway on the diagram (formally called a graph)! 
```

```{important}
You now have two visual tools for code, one is using cards for Divide-Conquer-Glue, while the other is this flowchart. The question is when to use which tool.  In practice, the initial high level breakdown comes from Divide-Conquer-Glue. Flowcharts are often good tools when looking at individual functions - both for design **and** debugging. The strength with debugging shows up formally in software testing, as it is often easy to see pathways or conditions missed. 

From a learning languages standpoint, we will use flowcharts when representing new concepts, so you have a visual pathway to look at on how the code is represented! We will also encourage you to convert from flowchart to code to flowchart, so you can have a better understanding of the actions taken and in what order. 

```


We will continue to explore how this looks in code, but for a flowchart it is as simple as thinking out your `True` and `False` pathways. 



## Knowledge Check

TODO