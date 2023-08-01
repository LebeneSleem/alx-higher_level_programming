#!/usr/bin/python3
# Python classes by Lebene Gbebleou-Sleem

"""creating a class to defines a Square by 0-squre.py"""


class Square:
    """Private instance attribute: size
    size must be an integer,: TypeError
    if size is less than 0,: ValueError"""

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    """retrieves the sizeof a square"""
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """ returns the current square area"""
    def area(self):
        return (self.__size ** 2)

    """prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
