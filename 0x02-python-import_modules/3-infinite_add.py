#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv) - 1

#    print(ac, end=" ")
#    if ac == 1:
#        print("argument", end="")
#    else:
#        print("arguments", end="")

#    if ac == 0:
#        print(".")
#    else:
#        print(":")

#    for i in range(1, ac + 1):
#        print("{:d}: {:d}".format(i, int(argv[i])))

    sum = 0
    for i in range(1, ac + 1):
        sum += int(argv[i])

    print("{:d}".format(sum))
