#!/usr/bin/python3
def magic_calculation(a, b, c):
    if (a < b):         # 3
        return c        # 4
    if (c > b):         # 5
        return a + b    # 6
    return (a * b) - c  # 7

# line 3
# var a, var_num 0 TOS
# var b, var_num 1 TOS
# TOS = TOS < TOS1??? TOS = b < a
# If (b < a) false goto BC_16, TOS popped
#
# line 4
# var c, var_num 2 TOS
# return TOS
#
# line 5
# (BC_16) var c, var_num 2 TOS
# var b, var_num 1 TOS
# TOS = TOS > TOS1??? TOS = b > c
# If (b > c) false goto BC_36, TOS popped
#
# line 6
# var a, var_num 0 TOS
# var b, var_num 1 TOS
# TOS = TOS1 + TOS, a + b on TOS
# return TOS
#
# line 7
# (BC_36) var a, var_num 0 TOS
# var b, var_num 1 TOS
# TOS = TOS1 * TOS, a * b on TOS
# var c, var_num 2 TOS
# TOS = TOS1 - TOS, (a * b) - c on TOS
# return TOS

# 3           0 LOAD_FAST                0 (a)
#             3 LOAD_FAST                1 (b)
#             6 COMPARE_OP               0 (<)
#             9 POP_JUMP_IF_FALSE       16
#
# 4          12 LOAD_FAST                2 (c)
#            15 RETURN_VALUE
#
# 5     >>   16 LOAD_FAST                2 (c)
#            19 LOAD_FAST                1 (b)
#            22 COMPARE_OP               4 (>)
#            25 POP_JUMP_IF_FALSE       36
#
# 6          28 LOAD_FAST                0 (a)
#            31 LOAD_FAST                1 (b)
#            34 BINARY_ADD
#            35 RETURN_VALUE
#
# 7     >>   36 LOAD_FAST                0 (a)
#            39 LOAD_FAST                1 (b)
#            42 BINARY_MULTIPLY
#            43 LOAD_FAST                2 (c)
#            46 BINARY_SUBTRACT
#            47 RETURN_VALUE
