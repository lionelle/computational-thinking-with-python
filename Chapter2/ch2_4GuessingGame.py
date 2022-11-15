"""
    Sample from Chapter 1.6 in Computational Thinking with Python.    
    (C) Albert Lionelle

    Pair with ch2_4_guessing_game_test_input.txt. Run command

    > cat ch2_4_guessing_game_test_input.txt | python chapter1_6.py
"""
__author__ = "Albert Lionelle"
__version__ = 1.0

def check_guess(value : int) -> str:
    """Informs the client if their value is greater than, less than, or
        equal to 3. Returns the string value based on Correct, Low, or High
    
    Examples:
        >>> check_guess(3)
        'Correct'
        >>> check_guess(2)
        'Low'
        >>> check_guess(4)
        'High'

    Args:
        value (int): The value to be guessed, already assumed to be an int

    Returns:
        str: The values Correct, High or Low 
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
    
    Examples:
        Client enters 2
        >>> get_guess()  # doctest: +NORMALIZE_WHITESPACE
        Guess a whole number:
        2
        
        Client enters 3
        >>> get_guess()  # doctest: +NORMALIZE_WHITESPACE
        Guess a whole number:
        3

    Returns:
        int: a whole number value for their guess
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
    main()  # run the program!

## to run the program > python ch2_4GuessingGame.py


### Example output from testing the program

# > cat ch2_4_guessing_game_test_input.txt | python -m doctest -v ch2_4GuessingGame.py
# Trying:
#     check_guess(3)
# Expecting:
#     'Correct'
# ok
# Trying:
#     check_guess(2)
# Expecting:
#     'Low'
# ok
# Trying:
#     check_guess(4)
# Expecting:
#     'High'
# ok
# Trying:
#     get_guess()  # doctest: +NORMALIZE_WHITESPACE
# Expecting:
#     Guess a whole number:
#     2
# ok
# Trying:
#     get_guess()  # doctest: +NORMALIZE_WHITESPACE
# Expecting:
#     Guess a whole number:
#     3
# ok
# 2 items had no tests:
#     ch2_4GuessingGame
#     ch2_4GuessingGame.main
# 2 items passed all tests:
#    3 tests in ch2_4GuessingGame.check_guess
#    2 tests in ch2_4GuessingGame.get_guess
# 5 tests in 4 items.
# 5 passed and 0 failed.
# Test passed.