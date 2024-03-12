#!/usr/bin/python3
def uppercase(str):
    end = ""
    length = 1

    for i in str:
        if length == len(str):
            end = "\n"
        if ord(i) in range(97, 123):
            print("{}".format(chr(ord(i) - 32)), end=end)
        else:
            print("{}".format(i), end=end)
        length = length + 1
