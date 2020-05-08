#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for item in a_dictionary.items():
        if item[1] == value:
            del a_dictionary[item[0]]
            break
    return a_dictionary
