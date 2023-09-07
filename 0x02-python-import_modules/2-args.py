#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    count = 1
    print("{:d} argument".format(length), end="")
    if length == 1:
        print(":")
    elif length == 0:
        print("s.")
    else:
        print("s:")
    for count, argument in enumerate(argv[1:], 1):
        print("{:d}: {}".format(count, argument))
