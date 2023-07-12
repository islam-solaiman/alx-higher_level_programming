#!/usr/bin/python3
"""function that returns the JSON representation of an object"""


def append_write(filename="", text=""):
    """Appends string to end of UTF8 text file.

    Args:
        file-name (str): name of the file to append to.
        text (str): string to append to the file.
    Returns:
        number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
