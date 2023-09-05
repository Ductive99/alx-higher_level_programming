#!/usr/bin/python3
def uppercase(str):
    fix = ""
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - (ord('a') - ord('A')))
        fix += char
    print("{}".format(fix), end="")
    print("")
