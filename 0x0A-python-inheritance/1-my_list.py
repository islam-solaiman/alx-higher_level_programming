#!/usr/bin/python3
"""class inherits from list Public instance method"""

class MyList(list):
    """print_sorted - prints the list in ascending order"""
    def print_sorted(self):
        """prints a list in ascending order."""
        print(sorted(self))
