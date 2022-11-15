"""
    Sample from Chapter 1.6 in Computational Thinking with Python.    
    (C) Albert Lionelle

    Pair with ch1_6test_input.txt. Run command

    > cat ch1_6test_input.txt | python chapter1_6.py
"""
__author__ = "Albert Lionelle"
__version__ = 1.0


def get_name() -> str:
   """Prompts the client to enter name of the individual.
   
   Examples:
      Client enters Ada Lovelace
      >>> get_name()   # doctest: +NORMALIZE_WHITESPACE
      Enter a name:
      'Ada Lovelace'

      Client enters Trillian Astra
      >>> get_name()   # doctest: +NORMALIZE_WHITESPACE
      Enter a name:
      'Trillian Astra'

   Returns:
       str: The value returned by the input
   """
   return input("Enter a name: ")


def get_year(prompt : str) -> int:
   """Prompts the user with `prompt` requesting a year. For example:
       `get_year("What is the current year? ")` would print to the screen
       "What is the current year? " and wait for the client to enter
       a whole number. The whole number is converted to an int. For example,
   
   Examples:
      Client enter 2022
      >>> get_year("Current Year ")  # doctest: +NORMALIZE_WHITESPACE  
      Current Year 
      2022

      Client enters 2525
      >>> get_year("Current Year ")  # doctest: +NORMALIZE_WHITESPACE 
      Current Year 
      2525

      Client enters 1979
      >>> get_year("Other Message ")  # doctest: +NORMALIZE_WHITESPACE
      Other Message 
      1979

      client enters 1224
      >>> get_year("Birth Year ")  # doctest: +NORMALIZE_WHITESPACE
      Birth Year 
      1224 
       
   Args:
       prompt (str): Message to show to the user, make sure to include space at the end

   Returns:
       int: The whole number of the value entered
   """
   return int(input(prompt)) 


def get_age(current_year : int, birth_year : int) -> int:
   """Takes the current year minus the birth year, and returns the result.
       There is no error checking, it will return the value of whatever
       numbers are provided.
   
   Examples:
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

   Args:
       current_year (int): the current year as a whole number
       birth_year (int): the birth year as a whole number

   Returns:
       int: the current_year - birth_year
   """
   return current_year - birth_year

def print_results(name : str, age : int) -> None:
   """Prints to the screen {name} is {age} based on parameters.

   Examples:
      >>> print_results('Ada Lovelace', 22)
      Ada Lovelace is 22.
      >>> print_results('Trillian Astra', 42)
      Trillian Astra is 42.

   Args:
       name (str): the name of the person
       age (int): the age of the person
   """
   print(f"{name} is {age}.")

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



### These commands are not currently explored by Chapter 1.6. We will come
### back to them later!
if __name__ == "__main__":
    main()  # run the program!

## to run the program type in the command line (>)

# > python chapter1_6.py

## To test the program, you can use doctest. Here is an example of tests running

# > cat ch1_6test_input.txt | python - m doctest -v chapter1_6.py
# Trying:
#     get_age(2022, 1980)
# Expecting:
#     42
# ok
# Trying:
#     get_age(2525, 1979)
# Expecting:
#     546
# ok
# Trying:
#     get_age(2022, 2022)
# Expecting:
#     0
# ok
# Trying:
#     get_age(2022, 2023)
# Expecting:
#     -1
# ok
# Trying:
#     get_name()   # doctest: +NORMALIZE_WHITESPACE
# Expecting:
#     Enter a name:
#     'Ada Lovelace'
# ok
# Trying:
#     get_name()   # doctest: +NORMALIZE_WHITESPACE
# Expecting:
#     Enter a name:
#     'Trillian Astra'
# ok
# Trying:
#     get_year("Current Year ")  # doctest: +NORMALIZE_WHITESPACE
# Expecting:
#     Current Year
#     2022
# ok
# Trying:
#     get_year("Current Year ")  # doctest: +NORMALIZE_WHITESPACE
# Expecting:
#     Current Year
#     2525
# ok
# Trying:
#     get_year("Other Message ")  # doctest: +NORMALIZE_WHITESPACE
# Expecting:
#     Other Message
#     1979
# ok
# Trying:
#     get_year("Birth Year ")  # doctest: +NORMALIZE_WHITESPACE
# Expecting:
#     Birth Year
#     1224
# ok
# Trying:
#     print_results('Ada Lovelace', 22)
# Expecting:
#     Ada Lovelace is 22.
# ok
# Trying:
#     print_results('Trillian Astra', 42)
# Expecting:
#     Trillian Astra is 42.
# ok
# 2 items had no tests:
#     chapter1_6
#     chapter1_6.main
# 4 items passed all tests:
#    4 tests in chapter1_6.get_age
#    2 tests in chapter1_6.get_name
#    4 tests in chapter1_6.get_year
#    2 tests in chapter1_6.print_results
# 12 tests in 6 items.
# 12 passed and 0 failed.
# Test passed.
