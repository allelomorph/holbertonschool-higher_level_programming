#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for item in sorted(a_dictionary.items()):
        print("{}: {}".format(item[0], item[1]))
