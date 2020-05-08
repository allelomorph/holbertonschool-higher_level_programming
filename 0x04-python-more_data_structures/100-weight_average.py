#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    sum1 = 0
    sum2 = 0
    for elem in my_list:
        sum1 += (elem[0] * elem[1])
        sum2 += elem[1]
    return sum1 / sum2
