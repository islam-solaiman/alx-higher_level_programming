#!/usr/bin/python3
"""
module contains function is_same_class
"""


def is_same_class(obj, a_class):
    """
    returns true if the obj is the exact class a_class
    otherwise returns false
    """
    return (type(obj) == a_class)
