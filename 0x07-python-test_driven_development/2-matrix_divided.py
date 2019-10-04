#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not matrix:
        return matrix
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    new_row = []
    rows = len(matrix)
    columns = len(matrix[0])

    for r in range(rows):
        if not len(matrix[r]) == columns:
            raise TypeError("Each row of the matrix must have the same size")
        for c in range(columns):
            if not isinstance(matrix[r][c], (int, float)):
                raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")

    new_matrix = [[round(element/div, 2) for element in row] for row in matrix]
    return new_matrix
