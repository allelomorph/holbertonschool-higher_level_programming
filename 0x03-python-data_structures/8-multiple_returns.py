#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        first_c = sentence[0]
    else:
        first_c = None
    return (length, first_c)

"""    retvals = [len(sentence)]
    if retvals[0] == 0:
        retvals += 
        else:
            retvals += sentence[0]
    return tuple(retvals)
  #  return retvals
"""
