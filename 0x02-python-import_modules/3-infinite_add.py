#!/usr/bin/python3

from sys import argv

argv_len = len(argv)
sum = 0

if __name__ == "__main__":
    if argv_len != 1:
        for i in range(1, argv_len):
            sum += int(argv[i])
        print("{:d}".format(sum))
    else:
        print("{:d}".format(0))
