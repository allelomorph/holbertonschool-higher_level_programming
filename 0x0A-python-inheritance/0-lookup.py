#!/usr/bin/python3
""" 0x0A. Python - Inheritance, task 0 """


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj (any): object of any type

    Returns:
        list of available attributes and methods

    """
    return dir(obj)

# alternative that lists values for each attribute/method:
#
# from inspect import getmembers
# getmembers(obj)
#
# output equivalent to:
# [(member, eval('<obj name>' + '.' + member)) for member in dir(l)]
#
# see https://docs.python.org/3.4/library/inspect.html
