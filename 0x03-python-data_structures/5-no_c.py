#!/usr/bin/python3

def no_c(my_string):
    str_list = list(my_string)

    new_str = ""

    for character in str_list:
        if character not in ['c', 'C']:
            new_str = new_str + character

    return new_str
