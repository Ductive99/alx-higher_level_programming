#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    copy = ""
    for char in str:
        if i != n:
            copy += char
        i += 1

    return copy
