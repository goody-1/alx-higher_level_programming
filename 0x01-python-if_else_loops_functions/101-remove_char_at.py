#!/usr/bin/python3
def remove_char_at(str, n):
    """This is a function to remove a character from string
    and printing the copy like the "C array index"
    """
    copy = ""

    if n > -1 and n <= len(str) - 1:
        for i in range(len(str)):
            if i != n:
                copy = copy + str[i]
        return copy
    else:
        return str
