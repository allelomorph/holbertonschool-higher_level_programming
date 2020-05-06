#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    truth_list = my_list[:]
    for i, num in enumerate(my_list):
        if num % 2 == 0:
            truth_list[i] = True
        else:
            truth_list[i] = False
    return truth_list
