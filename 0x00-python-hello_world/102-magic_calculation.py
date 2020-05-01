#!/usr/bin/python3
def magic_calculation(a, b):
    return 98 + (a ** b)

# 3           0 LOAD_CONST               1 (98)
#             3 LOAD_FAST                0 (a)
#             6 LOAD_FAST                1 (b)
#             9 BINARY_POWER
#            10 BINARY_ADD
#            11 RETURN_VALUE

# Code line 3:
# Const 98 on stack
# a, var_num = 0 on stack
# b, var_num = 1 on stack
# TOS = TOS1 ** TOS (remove top of stack and 2nd from top, result goes to top)
#    remove a ** remove b = result on stack
# TOS = TOS1 + TOS (remove top of stack and 2nd from top, result goes to top)
#    98 + (a ** b) = result on stack
# return top of stack
