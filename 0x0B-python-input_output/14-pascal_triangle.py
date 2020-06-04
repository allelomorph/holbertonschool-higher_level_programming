#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 14. Pascal's Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's triangle of
    `n`.

    Args:
        n (int): base number for calculating triangle

    """
    triangle = []
    if n <= 0:
        return triangle
    for row in range(n):
        new_row = []
        triangle.append(new_row)
        new_row.append(1)
        for col in range(1, row):
            new_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
        if row > 0:
            new_row.append(1)
    return triangle
