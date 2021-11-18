#!/usr/bin/python3
import hidden_4

items = dir(hidden_4)

if __name__ == "__main__":
    for item in items:
        if item[0:2] != "__":
            print(item)
