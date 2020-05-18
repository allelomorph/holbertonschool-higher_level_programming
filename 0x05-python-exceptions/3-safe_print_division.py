#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quot = a / b
    except (ZeroDivisionError):
        quot = None
    finally:
        print("Inside result: {}".format(quot))
        if quot is not None:
            quot = int(quot)
        return quot
