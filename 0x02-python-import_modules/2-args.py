#!/usr/bin/python3

from sys import argv

argv_len = len(argv)
if __name__ == "__main__":
    if argv_len - 1 == 0:
        print("{:d} arguments.".format(argv_len - 1))
    elif argv_len - 1 == 1:
        print("{:d} argument:".format(argv_len - 1))
        print("{:d}: {}".format(argv_len - 1, argv[argv_len - 1]))
    elif argv_len - 1 > 1:
        print("{:d} arguments:".format(argv_len - 1))
        for i in range(1, argv_len):
            print("{:d}: {}".format(i, argv[i]))
