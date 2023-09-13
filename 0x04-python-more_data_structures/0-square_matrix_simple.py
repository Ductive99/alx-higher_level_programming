#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []

    for row in matrix:
        result.append([n ** 2 for n in row])

    return result
