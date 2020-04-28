#!/usr/bin/python3
for c in range(ord('a'), ord('{')):
    if c != ord('e'):
        if c != ord('q'):
            print("{:c}".format(c), end="")
