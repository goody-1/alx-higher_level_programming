#!/usr/bin/python3

"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix (list): list of lists of integers or floats
        div (int, float): number to divide by

    Returns:
        list: list of lists of integers or floats

    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if matrix contains rows of different sizes
        TypeError: if div is not an int or a float
        ZeroDivisionError: if div is 0
    """
    # Check if matrix is a list of lists of integers or floats
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    # Check if all elements are lists
    if not all(type(row) is list and len(row) != 0 for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    # Check if all elements are integers or floats
    if not all(all(type(i) is int or type(i) is float for i in row)
               for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    # Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is int or float
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    try:
        return [[round(i / div, 2) for i in row] for row in matrix]
    except Exception as e:
        raise e
