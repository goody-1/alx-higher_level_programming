#!/usr/bin/python3
"""This module contains a function that multiplies 2 matrices."""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.

    Args:
        m_a (list): The first matrix represented as a list of lists.
        m_b (list): The second matrix represented as a list of lists.

    Returns:
        list: The resulting matrix after multiplication.

    Raises:
        ValueError: If the matrices cannot be multiplied.

    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not all(type(row) is list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) is list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    if not all(type(num) in [int, float] for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(type(num) in [int, float] for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    product = []

    row_size = len(m_a)
    col_size = len(m_b[0])

    for i in range(row_size):
        row = []
        for j in range(col_size):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            row.append(sum)

        product.append(row)

    return product
