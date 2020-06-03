#!/usr/bin/python3
""" 0x0A. Python - Inheritance, task 3 """


def is_kind_of_class(obj, a_class):
    """Tests if an object is an instance of the specified class,
    or any class inherited from it.

    Args:
        obj (any): object of any type
        a_class (class): class to test against

    Returns:
        True if obj is instance of a_class or a subclass of a_class,
            False otherwise.

    """
    return (isinstance(obj, a_class))
