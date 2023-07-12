#!/usr/bin/python3
""" Module executes function that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """ Function appends a new line when string is found
    Args:
        file-name: filename
        search_string: string to search
        new_string: string to append
    """

    res_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            res_line += [line]
            if line.find(search_string) != -1:
                res_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(res_line))
