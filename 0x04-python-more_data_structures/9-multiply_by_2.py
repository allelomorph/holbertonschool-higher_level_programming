#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key in new_dict.keys():
        new_dict[key] = a_dictionary[key] * 2
    return new_dict
