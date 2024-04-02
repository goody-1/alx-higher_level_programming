#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    int_len = x
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            int_len -= 1
            continue
    print()
    return int_len
