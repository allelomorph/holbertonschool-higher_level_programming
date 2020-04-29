#!/usr/bin/python3
def uppercase(str):
    for c in range(0, len(str)):
        if ord(str[c]) >= ord('a') and ord(str[c]) <= ord('z'):
            c_temp = chr(ord(str[c]) - ord(' '))
        else:
            c_temp = str[c]
        print(c_temp, end="")
    print("")
