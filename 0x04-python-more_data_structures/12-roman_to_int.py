#!/usr/bin/python3
def roman_to_int(roman_string):
    from functools import reduce

    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_to_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev_value = 0

    for numeral in reversed(roman_string):
        value = roman_to_decimal.get(numeral, 0)

        if value >= prev_value:
            num += value
        else:
            num -= value

        prev_value = value

    return num
