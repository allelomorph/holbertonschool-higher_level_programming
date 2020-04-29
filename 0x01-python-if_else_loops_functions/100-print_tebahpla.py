#!/usr/bin/python3
for c in reversed(range(ord('a'), ord('{'))):
    if c % 2 == 1:
        c -= ord(' ')
    print("{:c}".format(c), end="")
