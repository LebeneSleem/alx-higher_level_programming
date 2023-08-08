#!/usr/bin/python3
"""module for a  a locked class"""


class LockedClass:
    """
    LockedClass restricts dynamic creation of instance
    attributes, allowing only 'first_name'.
    """

    __slots__ = ['first_name']

    def __init__(self):
        """
        Initializes an instance of LockedClass.
        """
        pass
