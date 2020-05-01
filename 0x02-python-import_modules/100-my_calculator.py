#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    ac = len(argv) - 1

    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] == '+':
        sum = add(int(argv[1]), int(argv[3]))
        print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3], sum))
    elif argv[2] == '-':
        difr = sub(int(argv[1]), int(argv[3]))
        print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3], difr))
    elif argv[2] == '*':
        prod = mul(int(argv[1]), int(argv[3]))
        print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3], prod))
    elif argv[2] == '/':
        quot = div(int(argv[1]), int(argv[3]))
        print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3], quot))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
