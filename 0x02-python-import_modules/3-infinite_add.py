#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv) - 1

    sum = 0
    for i in range(1, ac + 1):
        sum += int(argv[i])

    print("{:d}".format(sum))
