#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += ((a ** b) / i)
        except Exception as e:
            result = b + a
        pass
    return result
