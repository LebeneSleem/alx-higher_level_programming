#!/usr/bin/python3
"""writing a Magic Class"""
import math


class MagicClass:
    """Defines a magic class with similar behavior to the given bytecode."""

    def __init__(self, radius=0):
        """Initialize the MagicClass instance.

        Args:
            radius (int or float): The radius of the circle. Default is 0.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius
