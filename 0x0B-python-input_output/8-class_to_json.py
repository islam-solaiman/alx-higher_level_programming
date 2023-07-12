#!/usr/bin/python3
"""DefinesPython class-to-JSON function."""


def class_to_json(obj):
    """Return dictionary represntation of a imple data structure."""
    return obj.__dict__
