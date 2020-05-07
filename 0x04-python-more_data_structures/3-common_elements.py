#!/usr/bin/python3
def common_elements(set_1, set_2):
    shared = []
    for a in set_1:
        for b in set_2:
            if a == b:
                shared.append(a)
    return set(shared)
