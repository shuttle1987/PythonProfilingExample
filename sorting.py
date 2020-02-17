"""Some example sorting algorithms"""

import random


def all_in_order(x):
    """Test that all items of x are in order"""
    i = 0
    j = len(x)
    while i + 1 < j:
        if x[i] > x[i + 1]:
            return False
        i += 1
    return True

def bogo(x):
    """The horribly inefficient bogosort"""
    while not all_in_order(x):
        random.shuffle(x)
    return x


def default_sort(x):
    return sorted(x)
