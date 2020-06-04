#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 15. Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a specific
    string.

    Args:
        filename (str): file to search
        search_string (str): search term
        new_string (str): line to insert into file after line containing match

    """
    with open(filename, 'r+', encoding='utf-8') as curr_file:
        lines = curr_file.readlines()
        curr_file.seek(0)
        for i, line in enumerate(lines):
            #            print("read:   {}".format(line), end='')
            if search_string in line:
                lines[i] = line + new_string
                #                print("modded: {}".format(line), end='')
#        for line in lines:
#            print(line, end="")
        curr_file.writelines(lines)
