#!/usr/bin/python3
"""  function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """finds peak in list of unsorted integers"""
    ls = list_of_integers
    le = len(ls)
    if le == 0:
        return
    m = le // 2
    if (m == le - 1 or ls[m] >= ls[m + 1]) and (m == 0 or ls[m] >= ls[m - 1]):
        return ls[m]
    if m != le - 1 and ls[m + 1] > ls[m]:
        return find_peak(ls[m + 1:])
    return find_peak(ls[:m])
