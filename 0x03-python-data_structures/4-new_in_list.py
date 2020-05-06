#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
