#!/usr/bin/python3
# Python classes by Lebene Gbebleou-Sleem

class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square when printed.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a new Square instance.
        size(self): Getter method for the size attribute.
        size(self, value): Setter method for the size attribute.
        position(self): Getter method for the position attribute.
        position(self, value): Setter method for the position attribute.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square with the character '#' at the given position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square when printed.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
            tuple: The position of the square when printed.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Args:
            value (tuple): The position of the square when printed.

        Raises:
            TypeError: If the value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(val, int) for val in value) or \
           any(val < 0 for val in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' at the given position.
        If the size is equal to 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
