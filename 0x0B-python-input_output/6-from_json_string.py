#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 6. From JSON string to Object  """


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_obj (any): object to be serialized

    """
    import json

    return json.loads(my_str)
