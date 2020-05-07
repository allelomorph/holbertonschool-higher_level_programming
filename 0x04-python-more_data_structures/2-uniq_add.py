#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp = set(my_list)
    sum = 0
    for x in temp:
        sum += x
    return sum
