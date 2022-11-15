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

# 2.4 Conditional Operations

In this section we will expand the number of our operations. In the past, we talked about typical math operations of `+`, `-`, `*`, `/` and `=` . Now we will look at expanding those options to include conditional statements. These statements generate True or False for the answer, also known as boolean values.

## Conditions

Python programmers can use the mathematical conditional operators directly in code. These conditions are requirements of making choices and branches in code, which makes them fundamental operations. The example operations with code are as follows.

| Condition | Prose | Example | print(answer) |
| -- | :-- | --: | :--: |
| $a >  b$| is $a$ *greater than* $b$ | answer = 10 > 5 | True |
| $a < b$ | is $a$ *less than* $b$ | age = 50 <br> answer = age < 100 | True|
| $a >= b$  | is $a$ *greater than or equal to* $b$ | age = 42<br>meaning = 42<br> answer = age >= meaning| True |
| $a <= b$  | is $a$ *less than or equal to* $b$ | answer = 5 <= 5| True |
| $a == b$  | is $a$ *equal to* $b$ | meaning = 42<br>answer = meaning == 42| True |
| $a$  $!=$  $b$  | is $a$ *not equal to* $b$ | meaning = 22<br>answer = meaning != 42| True |

It is important to remember that conditional operators evaluate both sides of the statement based on the operator / operation type, and then a Boolean value is returned. You need to make sure the types are the same, or it can be a bit funny how it works. For example, if we are taking input in from a client, we need to convert that to a number before we run our comparison. 

```{code-block}
val = input("How many puppies would you like to pet? ") ## assume the client enters 102
```
```{code-cell}
:tags: [remove-cell]
val = 102
```

```{code-cell} 
how_many_puppies = int(val)
crazy_puppies = how_many_puppies >= 100
print(f"Are you completely crazy wanting more than 100 puppies? {crazy_puppies}, I want {how_many_puppies} puppies.")
```

### Practice
Your turn, let's practice writing a simple application. You can use the build in window below, or your own IDE to practice. 

```{admonition} Tasks
:class: tip
You are going to build application to see if the client knows  the answer to the ultimate question of life, the universe, and everything. If they type in 42 it informs them that it is True, if they type in anything else, it informs them their answer is False. 

- [ ] Request input from the client, asking them what is the "answer to the ultimate question of life, the universe, and everything?"
- [ ] Convert that input to an int value
- [ ] Compare that input to 42, only True if they entered 42, false if anything else
- [ ] Print out "Your answer is {answer}, and it is {checked}." assuming answer is the variable you stored their answer in, and checked is the outcome of the condition statement.

If you get stuck, you should also click on the Solution Flowchart below. It may be able to help!
```

```{toggle}
Don't forget to put a number into the stdin section, before hitting run!
{{empty_code_window}}
```

#### Solution


````{toggle}
```python
answer_str = input("What is the answer to the ultimate question of life, the universe, and everything? ")
answer = int(answer_str)
checked = answer == 42
print(f"Your answer is {answer}, and it is {checked}.")
```
````
##### Code Trace Solution
```{toggle} 
Trace solution, assuming the client entered 22.
<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=answer_str%20%3D%20input%28%22What%20is%20the%20answer%20to%20the%20ultimate%20question%20of%20life,%20the%20universe,%20and%20everything%3F%20%22%29%0Aanswer%20%3D%20int%28answer_str%29%0Achecked%20%3D%20answer%20%3D%3D%2042%0Aprint%28f%22Your%20answer%20is%20%7Banswer%7D,%20and%20it%20is%20%7Bchecked%7D.%22%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%2222%22%5D&textReferences=false"> </iframe>
```

##### Solution Flowchart
````{toggle}
```{mermaid}
%%{init: {'securityLevel': 'loose', 'theme':'forest'}}%%
flowchart TD
   s([Start]) --> i[/What is.../]
   i -- answer_str --> c[Convert to int]
   c -- answer --> b[answer == 42]
   b -- answer, checked --> o[/"Your answer is {answer}, and it is {checked}."/]
   o --> e([End]) 
```
> Thinking Deeper:  
> Why does this not use a diamond?  The reason is that while it calculates a condition, it doesn't actually branch into code options. 
> Spoiler, we will cover that in the next section!

```{important}
We added our variables or parameters to each step! This makes it even easier to go from a flowchart to code and back!
```
````

## Conditions with Strings

You can also use the conditional operators with strings. The problem is how would one compare strings? Using the Alphabet in order!  We also assume capitals before lowercase in our comparison. So `'a'` is less than `'b'`, but `'A'` is less than `'a'`.

```{code-cell}
one = "Aa" == "Aa"
two = "AB" == "AC"
three = "Aa" > "Ab"
four = 'A'< 'a'

print(f'Is "Aa" == "Aa"? {one}')
print(f'Is "Aa" == "AC"? {two}')
print(f'Is "Aa" > "Ab"? {three}')
print(f"Is 'A' < 'a'? {four}")
```

For the most part, we use `==` and `!=` when comparing strings. 

```{margin} Casefold?
You will find .lower() is very common. That is not the most modern way of doing it, as .lower() can't take into account non-alphanumeric alphabets (greek cyrillic for example). Casefold takes that into account when setting up the characters for comparison. 
```

````{admonition} Case Sensitive 
:class: note

Most languages are case sensitive, meaning lowercase and uppercase are treated as different characters. Which they are, so that does make sense. However, sometimes we don't care about the case. Maybe we just want someone to type `"END"` or `"end"` or some combination. In this situation, we have to force the same case using `.casefold()` if we are using python 3.3 or later, or `.lower()` for older versions. 


````


```{code-cell}
one = "Ada"
two = "ada"

print(one == two)
print(one.casefold() == two.casefold())
```

## Order of Operations

We just added more operators, does that mean our order of operations changes from  PEMDAS? The answer is not really. PEDMAS still happens first, but then the *conditional* operators happen before the assignment operators! 

When in doubt, use parentheses. The following code is the same, but the second is  much more clear to read!

```{code-cell}
val =  10 / 2.5 + 3 > 20 + 2 * 0.6
print(val)
```

```{code-cell}
val =  ((10 / 2.5) + 3) > (20 + (2 * 0.6))
print(val)
```

## Branching?

So far we have just introduced new operators that return `True` or `False` based on the condition. They can compare numbers and strings, but our goal was also to allow our code to execute conditionally - meaning, based on the condition, only certain lines are executed. We will explore that next. 


## Knowledge Check
