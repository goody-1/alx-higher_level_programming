#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = str(number)
last = string[-1]

if int(last) < 6 and string[-1] != 0:
    print("Last digit of {:d} is {:d} and is less "
          "than 6 and not 0".format(number, int(last)))
elif int(last) == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, int(last)))
elif int(last) > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(
        number, int(last)))
