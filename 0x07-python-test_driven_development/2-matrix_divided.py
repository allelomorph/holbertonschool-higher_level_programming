#!/usr/bin/python3
"""Module built for Python 0x07 task 1. Error in project formatting scheme \
advances file numbering +1 for every task after 0.
"""


def matrix_divided(matrix, div):
    """Function that divides a matrix of values by a single divisor.

    Args:
        matrix (list of lists of ints or floats): 2D list to operate on
        div (int) or (float): divisor for members of matrix

    Returns: new matrix of quotients for each member of matrix divided by div

    """
    new_matrix = []

    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists)' +
                        ' of integers/floats')
    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists)' +
                            ' of integers/floats')
        if len(row) is not len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError('matrix must be a matrix (list of lists)' +
                                ' of integers/floats')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    elif div is 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        new_row = []
        for value in row:
            quot = round((value / div), 2)
            new_row.append(quot)
        new_matrix.append(new_row)
    return new_matrix
