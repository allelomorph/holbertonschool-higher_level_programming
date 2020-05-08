#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        temp = a_dictionary.items()
        sort = (sorted(temp, key=lambda item: item[1], reverse=True))
        return sort[0][0]
