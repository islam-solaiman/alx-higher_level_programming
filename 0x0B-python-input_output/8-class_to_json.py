#!/usr/bin/python3
""" Module that returns dictionary description 
with a simple data structure for a JSON 
serialization of an object
"""


def class_to_json(obj):
    """ function that returns the dictionary description with simple data structure """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
