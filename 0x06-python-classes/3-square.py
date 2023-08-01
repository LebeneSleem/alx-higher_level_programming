#!/usr/bin/python3
# 1-square.py by Lebene Gbebleou-Sleem

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

    """ returns the current square area"""
    def area(self):
        return (self.__size ** 2)
