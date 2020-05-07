#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp = my_list[:]
    sum = 0
    for x in temp:
        if temp.count(x) > 1:
            temp.remove(x)
    for x in temp:
        sum += x
    return sum
