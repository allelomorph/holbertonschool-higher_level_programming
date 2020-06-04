#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 10. Class to JSON"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj (any): object to be serialized

    """
    return obj.__dict__
