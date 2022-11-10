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
    >>> get_positive_int("Enter the max number in your range: ") # doctest: +NORMALIZE_WHITESPACE
    Enter the max number in your range: 
    10

    Assume client enters x
    >>> get_positive_int("Enter a guess: ") # doctest: +NORMALIZE_WHITESPACE
    Enter a guess: 
    -1

    Assume client enters 0 followed by 2
    >>> get_positive_int("Enter a guess: ") # doctest: +NORMALIZE_WHITESPACE
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
    """Runs a guessing game in which the client guesses numbers greater than 0 until they guess the number. 
       They will be given feedback based on high, low, or correct using `check(guess, correct)`. They 
       can end the game early at any point returning False. 

    Sample of game play. Assume the client enters 20, 5, 9, 10
    >>> play_game(10)  # doctest: +NORMALIZE_WHITESPACE
    Guess a number: 
    You guessed 20, that is High.
    Guess a number:
    You guessed 5, that is Low.
    Guess a number:
    You guessed 9, that is Low.
    Guess a number:
    You guessed 10, that is Correct.
    True

    Sample of game play. Assume the client enters 20, x
    >>> play_game(10)  # doctest: +NORMALIZE_WHITESPACE
    Guess a number:
    You guessed 20, that is High.
    Guess a number: 
    False

    :param correct: the correct value
    :type correct: int
    :return: True if they found the value, False if they failed to find it.
    :rtype: bool
    """
    result = None
    while result != 'Correct':
        guess = get_positive_int("Guess a number: ")
        if guess == -1:
            return False  ## early exit
        result = check(guess, correct)
        print(f"You guessed {guess}, that is {result}.")
    return True

def splash():
    """Prints a how to play dialog and welcome screen"""
    print("Welcome to the guessing game.")
    print("=============================")
    print("You will set the max value, and a random number will be selected.")
    print("You can then guess numbers. At any point, type x to end the game early.")
    print("=============================")

def main():
    """Main driver of the program
    """
    splash()
    mx = get_positive_int("Enter the max for the range: ")
    if mx < 1:
        print("Invalid max, thank you for not playing.")
    else:
        correct = randint(1, mx)
        print("Random is set, good luck!")
        result = play_game(correct)
        if result:
            print("Congratulations! You won!")
        else:
            print(f"Sorry you didn't find the number, it was {correct}.")
        



if __name__ == "__main__":
    main()

### to run tests from the command line
# cat ch2_6_test_input.txt | python -m doctest -v ch2_6GuessingGameSolution.py
# it should generate the following:
# PS D: \lionelle\dev\books\computational-thinking-in-python\computational-thinking-with-python\Chapter2 > cat ch2_6_test_input.txt | python - m doctest - v ch2_6GuessingGameSolution.py
# Trying:
#     check(10, 10)
# Expecting:
#     'Correct'
# ok
# Trying:
#     check(3, 5)
# Expecting:
#     'Low'
# ok
# Trying:
#     check(5, 3)
# Expecting:
#     'High'
# ok
# Trying:
#     # doctest: +NORMALIZE_WHITESPACE
#     get_positive_int("Enter the max number in your range: ")
# Expecting:
#     Enter the max number in your range:
#     10
# ok
# Trying:
#     get_positive_int("Enter a guess: ")  # doctest: +NORMALIZE_WHITESPACE
# Expecting:
#     Enter a guess:
#     -1
# ok
# Trying:
#     get_positive_int("Enter a guess: ")  # doctest: +NORMALIZE_WHITESPACE
# Expecting:
#     Enter a guess:
#     Invalid Number, try again(must be greater than 0):
#     2
# ok
# Trying:
#     play_game(10)  # doctest: +NORMALIZE_WHITESPACE
# Expecting:
#     Guess a number:
#     You guessed 20, that is High.
#     Guess a number:
#     You guessed 5, that is Low.
#     Guess a number:
#     You guessed 9, that is Low.
#     Guess a number:
#     You guessed 10, that is Correct.
#     True
# ok
# Trying:
#     play_game(10)  # doctest: +NORMALIZE_WHITESPACE
# Expecting:
#     Guess a number:
#     You guessed 20, that is High.
#     Guess a number:
#     False
# ok
# 3 items had no tests:
#     ch2_6GuessingGameSolution
#     ch2_6GuessingGameSolution.main
#     ch2_6GuessingGameSolution.splash
# 3 items passed all tests:
#    3 tests in ch2_6GuessingGameSolution.check
#    3 tests in ch2_6GuessingGameSolution.get_positive_int
#    2 tests in ch2_6GuessingGameSolution.play_game
# 8 tests in 6 items.
# 8 passed and 0 failed.
# Test passed.
