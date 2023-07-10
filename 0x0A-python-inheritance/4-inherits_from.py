#!/usr/bin/python3
"""class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
        If obj is an inherited instance of a_class - return true.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
