"""
    Sample from Chapter 1.6 in Computational Thinking with Python.    
    (C) Albert Lionelle

    Pair with ch2_4_guessing_game_test_input.txt. Run command

    > cat ch2_4_guessing_game_test_input.txt | python chapter1_6.py
"""
__author__ = "Albert Lionelle"
__version__ = 1.0

def check_guess(value):
    """
        Informs the client if their value is greater than, less than, or
        equal to 3. Returns the string value based on Correct, Low, or High
        
        >>> check_guess(3)
        'Correct'
        >>> check_guess(2)
        'Low'
        >>> check_guess(4)
        'High'

        :param value: The value to be guessed, already assumed to be an int
        :param type: int
    """
    response = ""
    if value == 3:
        response = "Correct"
    if value > 3:
        response = "High"
    if value < 3:
        response = "Low"
    return response

def get_guess():
    """Gets a number from the client. Does not currently handle error checking.

    >>> get_guess()  # client enters 2
    Guess a whole number:
    2
    >>> get_guess()  # client enters 3
    Guess a whole number:
    3

    :return: a whole number value for their guess
    :rtype: int
    """
    guess_str = input("Guess a whole number: ")
    return int(guess_str)

def main():
    """ Main driver of the program. Simply asks the client to guess a number,
    and says if it is higher or lower than 3."""
    guess = get_guess()
    answer = check_guess(guess)
    print(answer)


### These commands are not currently explored by Chapter 2.4. We will come
### back to them later!
if __name__ == "__main__":
    ## these are automated ways to run the tests
    import doctest
    flags = doctest.NORMALIZE_WHITESPACE
    fail, total = doctest.testmod(optionflags=flags)
    print("{} failures out of {} tests".format(fail, total))
    ##

    main()  # run the program!
