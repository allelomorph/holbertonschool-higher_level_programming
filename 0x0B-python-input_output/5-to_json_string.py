#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 5. To JSON string """


def to_json_string(my_obj):
    """Returns the JSON representation of an object (serialized string)

    Args:
        my_obj (any): object to be serialized

    """
    import json

    return json.dumps(my_obj)
