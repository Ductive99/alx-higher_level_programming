#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight = 0
    total = 0
    for i in range(len(my_list)):
        total += my_list[i][0] * my_list[i][1]
        weight += my_list[i][1]
    return total / weight
