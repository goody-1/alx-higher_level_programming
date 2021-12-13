#!/usr/bin/python3
"""
The "matrix_divided" Module.
This module divides all elements of a matrix by a certain real number "div"
via the function, matrix_divided(matrix, div).
For example,

>>> matrix_divided([
    [1, 2, 3],
    [4, 5, 6]
], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix of each numbers divided by 'div' (rounded to 2 dp)

    Args:
        matrix - list of lists of integers / floats
        div - an integer of float
    All matrix rows must have same size, div must not be zero
    """

    # validate the matrix
    if matrix and isinstance(matrix, list) is True:	    # matrix must be a list
        for first_nest in matrix:
            # elements of matrix must be a list too
            if first_nest and isinstance(first_nest, list) is True:
                for assumed_number in first_nest:
                    # elements of first_nest must be real numbers only
                    if type(assumed_number) is not float and \
                            type(assumed_number) is not int:
                        # Raise TypeError if other types
                        raise TypeError("matrix must be a matrix "
                                        "(list of lists) of integers/floats")
            else:
                # list of lists only not list of other types
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    else:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Checking the size of the matrix rows - all should be same size
    size = []        # initialize size list

    for inner_list in matrix:
        size.append(len(inner_list))

    if max(size) != min(size):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate the div parameter
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div is float('NaN'):
        raise ValueError("cannot convert float NaN to integer")

    # Checking div for ZeroDivisionError
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # dividing the elements by div and returning the new matrix

    new_matrix = []
    counter = 0

    for inner_list in matrix:
        new_matrix.append([])
        for number in inner_list:
            new_matrix[counter].append(round(number / div, 2))
        counter += 1

    return new_matrix
