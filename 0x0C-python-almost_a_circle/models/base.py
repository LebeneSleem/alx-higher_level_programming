#!/usr/bin/python3
"""This model is for a first class Base"""


class Base:
    """This is the base model of
    all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new base"""
        if id is not None:
            id = self.id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
