#!/usr/bin/python3
"""writes a string to a text file. """


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
        filename (str): The name of  file to write.
        text (str): text to write to  file.
    Returns:
        number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
