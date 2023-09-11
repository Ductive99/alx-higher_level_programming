#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if my_list is None or len(my_list) == 0:
        return None
    for int in my_list:
        if int > max:
            max = int
    return max
