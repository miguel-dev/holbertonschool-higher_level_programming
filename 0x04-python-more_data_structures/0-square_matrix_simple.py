#!/usr/bin/python3


def square(x):
    return x**2


def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    new_matrix = []

    for r in range(rows):
        new_matrix.append(list(map(square, matrix[r])))
    return new_matrix
