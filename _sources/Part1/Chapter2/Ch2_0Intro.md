# 2 Algorithmic Thinking

When we first took algebra, math teachers said we were solving algorithms which of course causes to associate the term with algebra. The same is true with formulas. We were often given something like the following:

$ f(x) = 2x + 3$

And we were told, if $f(x)$ is 9, solve for $x$. What we weren't told was the *why*. We were essentially a computer solving someone elses algorithm. Instead with programming we flip that. We notice that 

$ f(x)  = 2x + 3$

is a *function*. $x$ is the parameter, and we have been given a repeatable formula to solve. We could rewrite it in python even. 

```python
def slope(x):
    return 2 * x + 3
```

For any value of $x$ we can repeat that function. For longer problems, we were often given multiple lines. These are all algorithms in the fact they are set actions to follow and repeat. 

Looking at  another domain, we can also consider recipes. A recipe has two parts to it. One part is the ingredients. The other part is the instructions we use to assemble the recipe. 

````{margin} 
  ```{admonition} PB&J Game  
    There is a game programming instructors will play. They ask students to explain how to make a PB&J sandwich to them, adn they take everything they say *literally*. Get some peanut butter (from where?) take out some and spread it (they use their hands), etc. Context matters!
  ```
````


```{card} Million Dollar Sandwich

**Ingredients**  
  * Two slices of sandwich bread
  * 2 tablespoons of peanut butter
  * 2 tablespoons of strawberry jam
  * 2 large strawberries

**Steps**  
  1. Spread peanut butter onto one side of one slice of bread
  2. Spread jam onto one side of one slice of bread
  3. Slice strawberries and place onto jam side of bread
  4. Place peanut butter slice on top of jam slice
  5. Serve
```
The ingredients are variables, and the steps are operations. By following th operations in order, you are essentially following an algorithm. That means *cooking/baking* is algorithmic thinking! If you are a writer who follows set pattern when writing, such as the five paragraph essay or the heroes journey, you are following algorithmic thinking. 

With computer science, we learn to how to document and define these steps for a computer to follow. The problem is that both examples have **context**. When we say spread the peanut butter, we know that they mean with a knife. When we say, place the slices together, we know the peanut butter and jam should be facing each other! A computer doesn't know this, as it doesn't have learned context to adjust. 

```{epigraph}
You have to be exact with computers, because they can't make up the missing steps!
```

In programming, we always have to set our variables, define our steps carefully, and document what we do. However, the languages we use may vary based on the problem. Furthermore, how we do it may vary, which is why  programming can be difficult - there is rarely a single answer to the problem, if the problem is sufficiently large enough. However, there are more correct answers than others in how we do things, and thinking via Divide-Conquer-Glue will get you closer to seeing the differences. 

In this chapter, we explore more tools to help us in our algorithmic thinking. Most notably, we will learn how to program without writing code, but in a repeatable manner anyone can reproduce and follow. We will also be given the ability to add options and choices in our code, so our algorithms can further break the mode of a single action but allow multiple actions based on the information at hand. Let's get cooking! 
