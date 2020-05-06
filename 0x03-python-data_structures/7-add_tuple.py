#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a):
        a_1 = tuple_a[0]
    else:
        a_1 = 0

    if len(tuple_b):
        b_1 = tuple_b[0]
    else:
        b_1 = 0

    if len(tuple_a) > 1:
        a_2 = tuple_a[1]
    else:
        a_2 = 0

    if len(tuple_b) > 1:
        b_2 = tuple_b[1]
    else:
        b_2 = 0

    return (a_1 + b_1, a_2 + b_2)
