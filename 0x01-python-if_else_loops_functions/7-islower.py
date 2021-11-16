#!/usr/bin/python3

def islower(c):
    if ord(c) < 58:
        return False
    elif c.islower():
        return True
    else:
        return False
