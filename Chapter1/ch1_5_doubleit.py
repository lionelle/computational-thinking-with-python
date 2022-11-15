def double_it(value: str) -> str:
    """Doubles a string value

    Args:
        value (str): The string to be doubled with \\n between the string

    Returns:
        str: value twice with a new line between
    """
    return f"{value}\n{value}"

def dsays(animal : str, sound : str) -> str:
    """Takes and animal and sound, and returns a doubled version of the animal says.

    Args:
        animal (str): the animal
        sound (str): the sound they make

    Returns:
        str: A doubled version of the saying "The {animal} says {sound}."
    """
    double = double_it(f"The {animal} says {sound}.")
    return double

cat_says = dsays("cat", "meow")
dog_says = dsays("dog", "woof")
print(cat_says)
print(dog_says)
