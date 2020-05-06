#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            if not len(row):
                print()
            for i, elem in enumerate(row):
                print("{:d}".format(row[i]), end="")
                if i is not len(row) - 1:
                    print(" ", end="")
                else:
                    print()
