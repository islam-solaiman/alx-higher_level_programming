#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    temp = {}
    for i in a_dictionary:
        new = (a_dictionary.get(i)) * 2
        temp.update({i: new})
    return (temp)
