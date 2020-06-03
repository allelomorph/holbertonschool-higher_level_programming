#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 0. Read file """


def read_file(filename=""):
    """Reads contents of a text file and print to stdout.

    Args:
        filename (str): name of file to be opened

    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
