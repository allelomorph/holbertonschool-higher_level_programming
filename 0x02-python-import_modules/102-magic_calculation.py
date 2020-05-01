#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub # 3
    if a < b:                                  # 4
        c = add(a, b)                          # 5
        for i in range(4, 6):                  # 6
            c = add(c, i)                      # 7
        return c                               # 8
    else:
        return sub(a, b)                       #10

# line 3
# consti 1 const = 0 TOS
# consti 2 const = ['add', 'sub'] TOS
# namei 0 = magic_calculation_102
#     __import__(fromlist=TOS, level=TOS1)
#     __import__(fromlist=add, sub; level=current dir)
# namei 1 = add TOS
# var_num 2 = add = TOS
#     add = magic_calculation_102.add
# namei 2 = sub TOS
# var_num 3 = sub = TOS
#     add = magic_calculation_102.sub
# remove TOS
#
# line 4
# var_num 0 = a TOS
# var_num 1 = b TOS
# dis.cmp_op: __lt__(self, value, /)
#             Return self<value.
#        TOS = TOS1 < TOS, TOS = a < b
# If (a < b) false goto BC_94, TOS popped
#
# line 5
# var_num 2 = add TOS
# var_num 0 = a TOS
# var_num 1 = b TOS
# var_num 2(var_num 0, var_num 1)
#       TOS = add(a, b)
# var_num 4 = c, c = TOS
#
# line 6
# loop to BC_90 (38??)
# namei 3 = range TOS
# consti 3 const = 4 TOS
# consti 4 const = 6 TOS
# namei3(consti 3, consti 4)
#     range(4, 6)
# iterate[4, 5]
# (BC_65) iterate until BC_89
# i stores iterations
#
# line 7
# var_num 2 = add
# var_num 4 = c
# var_num 5 = i
# var_num 2(var_num 4, var_num 5)
#     TOS = add(c, i)
# c = TOS
# jump to BC_65 (loop again)
# pop statement block
#
# line 8
# (BC_90) var_num 4 = c TOS
# return TOS
#
# line 10
# (BC_94) var_num 3 = sub TOS
# var_num 0 = a TOS
# var_num 1 = b TOS
# var_num 3(var_num 0, var_num 1)
#     TOS = sub(a, b)
# return TOS
# consti 0 = undefined TOS
# return TOS

# 3           0 LOAD_CONST               1 (0)
#             3 LOAD_CONST               2 (('add', 'sub'))
#             6 IMPORT_NAME              0 (magic_calculation_102)
#             9 IMPORT_FROM              1 (add)
#            12 STORE_FAST               2 (add)
#            15 IMPORT_FROM              2 (sub)
#            18 STORE_FAST               3 (sub)
#            21 POP_TOP
#
# 4          22 LOAD_FAST                0 (a)
#            25 LOAD_FAST                1 (b)
#            28 COMPARE_OP               0 (<)
#            31 POP_JUMP_IF_FALSE       94
#
# 5          34 LOAD_FAST                2 (add)
#            37 LOAD_FAST                0 (a)
#            40 LOAD_FAST                1 (b)
#            43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
#            46 STORE_FAST               4 (c)
#
# 6          49 SETUP_LOOP              38 (to 90)
#            52 LOAD_GLOBAL              3 (range)
#            55 LOAD_CONST               3 (4)
#            58 LOAD_CONST               4 (6)
#            61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
#            64 GET_ITER
#       >>   65 FOR_ITER                21 (to 89)
#            68 STORE_FAST               5 (i)
#
# 7          71 LOAD_FAST                2 (add)
#            74 LOAD_FAST                4 (c)
#            77 LOAD_FAST                5 (i)
#            80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
#            83 STORE_FAST               4 (c)
#            86 JUMP_ABSOLUTE           65
#       >>   89 POP_BLOCK
#
# 8     >>   90 LOAD_FAST                4 (c)
#            93 RETURN_VALUE
#
#10     >>   94 LOAD_FAST                3 (sub)
#            97 LOAD_FAST                0 (a)
#           100 LOAD_FAST                1 (b)
#           103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
#           106 RETURN_VALUE
#           107 LOAD_CONST               0 (None)
#           110 RETURN_VALUE
