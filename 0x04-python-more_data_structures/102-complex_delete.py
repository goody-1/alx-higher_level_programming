#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    pop_keys = []

    for k, v in a_dictionary.items():
        if v == value:
            pop_keys.append(k)

    for i in pop_keys:
        del a_dictionary[i]

    return a_dictionary
