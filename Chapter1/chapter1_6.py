"""
    Sample from Chapter 1.6 in Computational Thinking with Python.    
    (C) Albert Lionelle

    Pair with ch1_6test_input.txt. Run command

    > cat ch1_6test_input.txt | python chapter1_6.py
"""
__author__ = "Albert Lionelle"
__version__ = 1.0


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
    return input("Enter a name: ")


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
   return int(input(prompt)) 


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


def print_results(name, age):
   """ Prints to the screen {name} is {age} based on parameters. For example:
      
      >>> print_results('Ada Lovelace', 22) 
      Ada Lovelace is 22.   
      >>> print_results('Trillian Astra', 42) 
      Trillian Astra is 42.
      
      :param name: the name of the person
      :type name: str
      :param age: the age of the person
      :type age: int
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
    ## these are automated ways to run the tests
    import doctest
    flags = doctest.NORMALIZE_WHITESPACE
    fail, total = doctest.testmod(optionflags=flags)
    print("{} failures out of {} tests".format(fail, total))
    ##

    main()  # run the program!