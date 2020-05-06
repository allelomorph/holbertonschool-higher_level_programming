#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for i, elem in enumerate(row):
                print("{:d}".format(row[i]), end="")
                if i != len(row) - 1:
                    print(" ", end="")
                else:
                    print()
    else:
        return None

""" end="")
                if num < (len(matrix[]) - 1):
                      print(" ")
                else:
                      print()
"""
"""
end=" " if num != (len(elem) - 1)
            for j in range(0, len(matrix[i])):
                if j < len(matrix[i] - 1):
                    print("{:d}".format(matrix[i][j], end=" "))
                else:
                    print("{:d}".format(matrix[i][j]))
"""
