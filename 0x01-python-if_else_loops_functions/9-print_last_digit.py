#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:  # Python returns different modulo than C for negative ints
        abs = number * -1
        digit = (abs % 10)
    else:
        digit = number % 10

    print("{:d}".format(digit), end="")
    return digit
