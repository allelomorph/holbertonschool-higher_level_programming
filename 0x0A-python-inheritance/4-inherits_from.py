#!/usr/bin/python3
""" 0x0A. Python - Inheritance, task 4 """


def inherits_from(obj, a_class):
    """Tests if an object is an instance of a class inherited from
    the specified class, directly or indirectly.

    Args:
        obj (any): object of any type
        a_class (class): class to test against

    Returns:
        True if obj is an instance of a subclass of a_class,
            False otherwise.

    """
    if type(obj) == a_class:
        return (False)
    return (issubclass(type(obj), a_class))
