#!/usr/bin/python3
"""Module that defines an inherited list class MyList."""


class MyList(list):
    """Inherits from list."""

    def print_sorted(self):
        """Print a list in sorted order."""
        print(sorted(self))
