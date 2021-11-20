#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    position = 1
    for row in matrix:
        for item in row:
            if position == len(row):
                end = ""
            else:
                end = " "
            print("{:d}".format(item), end=end)
            position += 1
        print()
        position = 1
