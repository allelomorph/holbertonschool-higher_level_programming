#!/usr/bin/python3
"""Module built for Python 0x07 task 3. Error in project formatting scheme \
advances file numbering +1 for every task after 0.
"""


def print_square(size):
    """Function that prints a square of a given size in '#' characters:

    Args:
        size (int): length of side of square, in monospace chars

    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for row in range(size):
        for col in range(size):
            print('#', end="")
        print()
