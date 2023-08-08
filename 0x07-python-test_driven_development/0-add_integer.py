#!/usr/bin/python3
"""A module that has a function that adds two integers"""


def add_integer(a, b=98):
    """
    Function that adds two integers.

    Args:
        a (int/float): The first number.
        b (int/float): The second number (default is 98).

    Returns:
        int: The sum of a and b, casted to an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
