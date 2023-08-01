#!/usr/bin/python3
"""writing a docu string"""


class Square:
    """Defines a square.

    Attributes:
        size (int or float): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance.
        area(self): Calculates and returns the area of the square.
        __eq__(self, other): Equality comparison for the square area.
        __ne__(self, other): Inequality comparison for the square area.
        __gt__(self, other): Greater than comparison for the square area.
        __ge__(self, other): Greater than or equal comparison
        __lt__(self, other): Less than comparison for the square area.
        __le__(self, other): Less than or equal comparison for the square area.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int or float): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.

        Raises:
            TypeError: If the value is not a number (int or float).
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError('size must be a number (float or integer)')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison for the square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison for the square area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison for the square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison for the square area."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparison for the square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison for the square area."""
        return self.area() <= other.area()
