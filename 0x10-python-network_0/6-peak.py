#!/usr/bin/python3
"""  function that finds a peak in a list of unsorted integers """



def find_peak(list_of_integers):
    """finds peak in list of unsorted integers"""
    ls = list_of_integers
    l = len(ls)
    if l == 0:
        return
    m = l // 2
    if (m == l - 1 or ls[m] >= ls[m + 1]) and (m == 0 or ls[m] >= ls[m - 1]):
        return ls[m]
    if m != l - 1 and ls[m + 1] > ls[m]:
        return find_peak(ls[m + 1:])
    return find_peak(ls[:m])
