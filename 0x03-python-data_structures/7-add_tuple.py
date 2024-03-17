#!/usr/bin/python3

def add_tuple(a=(), b=()):
    a = list(a)
    b = list(b)

    if (len(a) == 1):
        a.append(0)
    elif (len(a) == 0):
        a.extend([0, 0])
    if (len(b) == 1):
        b.append(0)
    elif (len(b) == 0):
        b.extend([0, 0])

    return (a[0] + b[0], a[1] + b[1])
