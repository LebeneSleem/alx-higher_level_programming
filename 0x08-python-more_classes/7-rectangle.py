#!/usr/bin/python3
# More classes and objects by Lebene Gbebleou-Sleem
"""A calss that defines a rectangle"""


class Rectangle:
    """Rectangle Class with property and setter"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Private optional instance attributte"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """ returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = str(self.print_symbol) * self.__width
        return ("\n".join(rectangle_str for _ in range(self.__height)))

    def __repr__(self):
        """Representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor that prints a message when the instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
