#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    columns = len(matrix[0])
    if not matrix:
        return None

    for r in range(rows):
        for c in range(columns):
            if c != columns - 1:
                print("{:d} ".format(matrix[r][c]), end="")
            else:
                print("{:d}".format(matrix[r][c]), end="")
        print()
