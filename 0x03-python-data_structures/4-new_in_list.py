#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = list(my_list)
    if idx < 0:
        return copy
    elif idx > len(copy) - 1:
        return copy
    else:
        copy[idx] = element
        return copy
