#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
    except IndexError:
        i -= 1
        pass
    print()

    return i + 1
