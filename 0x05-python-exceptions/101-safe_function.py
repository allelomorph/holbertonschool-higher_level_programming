#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        retval = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
    else:
        return retval
