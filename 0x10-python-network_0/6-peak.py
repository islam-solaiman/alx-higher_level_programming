#!/usr/bin/python3
""" find_peak finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """finds peak in list of unsorted integers"""
    ls = list_of_integers
    lns = len(ls)
    if lns == 0:
        return
    m = lns // 2
    if (m == lns - 1 or ls[m] >= ls[m + 1]) and (m == 0 or ls[m] >= ls[m - 1]):
        return ls[m]
    if m != lns - 1 and ls[m + 1] > ls[m]:
        return find_peak(ls[m + 1:])
    return find_peak(ls[:m])
