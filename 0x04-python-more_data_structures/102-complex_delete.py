#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for item in a_dictionary.keys():
        if item == value:
            del a_dictionary[item]
    return a_dictionary
