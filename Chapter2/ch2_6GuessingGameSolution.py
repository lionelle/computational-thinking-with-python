from random import randint # https://docs.python.org/3/library/random.html#random.randint

""" 
Guessing game. The game starts with a randomly generated number between a set range. The client guesses the number until 
they are either able to guess the number or they type x.
"""
__author__ = "Albert Lionelle"
__version__ = 1.0

def check(guess : int, correct : int) -> str:
    """Checks to see if guess is equal to, higher or lower than correct. Returns
    'Correct', 'High', 'Low' respectively. For example:

    >>> check(10, 10)
    'Correct'
    >>> check(3, 5)
    'Low'
    >>> check(5, 3)
    'High'

    :param guess: the value they are guessing
    :type guess: int
    :param correct: a value that is to be tested against
    :type correct: int
    :return: 'Correct', 'High', 'Low'
    :rtype: str
    """
    response = ''
    if guess == correct:
        response = 'Correct'
    else:
        if guess < correct:
            response = 'Low'
        else:
            response = 'High'
    return response


def get_positive_int(prompt : str) -> int:
    """Asks the user based on the prompt to enter a number. The
    number has to be either a number greater than 0 or an 'x'.
    If 'x' is entered, -1 is returned. Will continue to prompt if 0 or lower
    numbers are entered. :Does not do any error checking if non-digits are entered.:
    Example execution:

    Assume client enters 10
    >>> get_positive_int("Enter the max number in your range: ")
    Enter the max number in your range: 
    10

    Assume client enters x
    >>> get_positive_int("Enter a guess: ")
    Enter a guess: 
    -1

    Assume client enters 0 followed by 2
    >>> get_positive_int("Enter a guess: ")
    Enter a guess: 
    Invalid Number, try again (must be greater than 0): 
    2

    :param prompt: A string to prompt the client
    :type prompt: str
    :return: either a number > 0, or -1 if client enters x
    :rtype: int
    """
    val = input(prompt)
    if val == 'x':
        return -1
    num = int(val)
    while num < 1:
        val = input("Invalid Number, try again (must be greater than 0): ")
        if val == 'x':
            return -1
        num = int(val)
    return num



def play_game(correct : int) -> bool:
    """_summary_

    :param correct: _description_
    :type correct: int
    :return: _description_
    :rtype: bool
    """

def main():
    """_summary_
    """


if __name__ == "__main__":
    ## these are automated ways to run the tests
    import doctest
    flags = doctest.NORMALIZE_WHITESPACE
    fail, total = doctest.testmod(optionflags=flags)
    print("{} failures out of {} tests".format(fail, total))

    main()