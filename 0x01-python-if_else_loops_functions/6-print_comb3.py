#!/usr/bin/python3
for tens in range(0, 10):
    for ones in range(0, 10):
        if ones > tens and (ones + tens) < 17:
            print("{:d}{:d}".format(tens, ones), end=", ")
print("89")
