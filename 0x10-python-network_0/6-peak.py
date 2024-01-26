#!usr/bin/python3
"""Module for finding a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None
    before_element = list_of_integers[0]
    for i in range(len(list_of_integers)):
        if list_of_integers[i] >= before_element:
            if (i == len(list_of_integers) - 1 or
                    list_of_integers[i] >= list_of_integers[i + 1]):
                return list_of_integers[i]
        before_element = list_of_integers[i]
