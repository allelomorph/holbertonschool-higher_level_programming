#!/usr/bin/python3
"""Module built for Python 0x07 task 4. Error in project formatting scheme \
advances file numbering +1 for every task after 0.
"""


def text_indentation(text):
    """Function that prints text with 2 new lines after each of the \
characters '.',',', and '?' :

    Args:
        text (str): text to be edited

    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    j = 0
    delims = '.?:'

    for i, char in enumerate(text):
        for delim in delims:
            if char is delim:
                j += 1
                text = text[:i + j] + ' ' + text[i + j:]

    list = text.split()

    for word in list:
        if word[-1:] is "." or word[-1:] is "?" or word[-1:] is ":":
            print(word, end="\n\n")
        elif word is list[len(list) - 1]:
            print(word, end="")
        else:
            print(word, end=" ")
