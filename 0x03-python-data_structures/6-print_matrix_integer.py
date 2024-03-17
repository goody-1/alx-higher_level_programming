#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print()
        i = 0
        for item in row:
            i += 1
            if i != len(row):
                print("{}".format(item), end=" ")
            else:
                print("{}".format(item))
