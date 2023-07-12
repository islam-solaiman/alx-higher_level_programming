#!/usr/bin/python3
""" Module creates an Object from JSON file"""

import json


def load_from_json_file(filename):
    """ Function creates Object from JSON file
    Args:
        file-name: textfile name
    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
