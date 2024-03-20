#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    # res = []
    # res.append(list(map(lambda x: x ** 2, matrix[i])))

    return [[i ** 2 for i in row] for row in matrix]
