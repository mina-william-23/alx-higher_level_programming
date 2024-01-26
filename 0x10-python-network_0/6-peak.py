#!/usr/bin/python3
"""Module for finding a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None
    lt = list_of_integers
    before_element = lt[0]
    for i in range(len(lt)):
        if lt[i] >= before_element:
            if (i == len(lt) - 1 or lt[i] >= lt[i + 1]):
                return lt[i]
        before_element = lt[i]
