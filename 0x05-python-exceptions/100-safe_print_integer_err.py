#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys

    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        return True

# 'except Exception as err:' for all exceptions
