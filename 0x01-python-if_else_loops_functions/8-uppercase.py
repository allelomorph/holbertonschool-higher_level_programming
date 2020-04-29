#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            c = chr(ord(c) - ord(' '))

        print("{}".format(c), end="")
    print("")
