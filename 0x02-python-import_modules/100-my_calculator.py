#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator == "+":
        print("{:d} {} {} = {:d}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, div(a, b)))
