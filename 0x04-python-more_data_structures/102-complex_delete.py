#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary)
    for k in keys:
        if a_dictionary[k] == value:
            del a_dictionary[k]

    return a_dictionary
