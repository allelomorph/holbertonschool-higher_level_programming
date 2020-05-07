#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_item = {key: value}
    a_dictionary.update(new_item)
    return a_dictionary
