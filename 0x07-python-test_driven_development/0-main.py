#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, -3))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
try:
    add_integer([4, 6, 7], 7)
except Exception as e:
    print(e)
try:
    add_integer(True, False)
except Exception as e:
    print(e)
try:
    add_integer("Hello", "Alx")
except Exception as e:
    print(e)
