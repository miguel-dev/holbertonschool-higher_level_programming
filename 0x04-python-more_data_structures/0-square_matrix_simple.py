#!/usr/bin/python3


def square(x):
    return x**2


def square_matrix_simple(matrix=[]):
    rows = len(matrix)

    return list(list(map(square, matrix[i])) for i in range(rows))
