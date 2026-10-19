#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Return a peak of the list, or None if the list is empty.

    A peak is a value that is not smaller than its neighbours. The
    list is halved at each step, so only a few values are inspected.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while True:
        middle = low + (high - low + 1) // 2
        if middle > low and list_of_integers[middle - 1] >= \
                list_of_integers[middle]:
            high = middle - 1
        elif middle < high and list_of_integers[middle + 1] >= \
                list_of_integers[middle]:
            low = middle + 1
        else:
            return list_of_integers[middle]
