#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    checker = []
    for number in my_list:
        if number % 2 == 0:
            checker.append(True)
        else:
            checker.append(False)
    return checker
