"""
The 'partial' function creates a new function with some arguments pre-filled.
This example demonstrates creating greet_someone function with either the greeting word or the name pre-filled.
"""

from functools import partial


def greet_someone(greeting_word, name):
    """
    Greets someone with a given greeting word and their name.

    Args:
        greeting_word (str): The greeting word to use.
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message combining the greeting word and the name.
    """
    return f"{greeting_word}, {name}!"


heya = partial(greet_someone, "Heya")

print(heya("Mor"))  # Output: Heya, Mor!

mor = partial(greet_someone, name="Mor")

print(mor("Hello"))  # Output: Hello, Mor!
