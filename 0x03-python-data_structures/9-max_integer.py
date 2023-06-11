#!/usr/bin/python3

def max_integer(my_list=[]):
    x = None
    for i in my_list:
        if x is None or x < i:
            x = i
    return x
