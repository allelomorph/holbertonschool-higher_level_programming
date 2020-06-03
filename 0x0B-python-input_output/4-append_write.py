#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 4. Append to a file """


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns the
number of characters added.

    Args:
        filename (str): name of file to be opened
        text (str): chars to be written

    """
    with open(filename, 'a', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
