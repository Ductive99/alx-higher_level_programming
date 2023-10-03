#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    divides a matrix by a number

    Args:
        matrix (list of lists): the matrix
        div (int OR float): the divisor

    Returns: a new matrix containing the result of the division
            rounded to 2 decimal places
    """
    typeErr1 = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(typeErr1)
    for i in range(len(matrix)):
        # checking for correct input list of lists + int or float
        if not isinstance(matrix[i], list) or not\
                all(isinstance(item, (int, float)) for item in matrix[i]):
            raise TypeError(typeErr1)
        # checking that the matrix's rows are of the same length
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    # checking if div is a number (int OR float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # we still can't divide by zero :(
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # return a new matrix
    return [[round(n / div, 2) for n in row] for row in matrix]
