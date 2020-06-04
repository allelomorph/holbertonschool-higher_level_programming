#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 8. Create object from a JSON file  """


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): file containing serialized object string

    """
    import json

    with open(filename, encoding='utf-8') as file:
        return json.load(file)
