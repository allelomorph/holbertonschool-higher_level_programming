#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 1. Number of lines """


def number_of_lines(filename=""):
    """Returns the number of lines in a text file.

    Args:
        filename (str): name of file to be opened

    """
    line_count = 0
    with open(filename, encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line_count += 1
    return line_count
