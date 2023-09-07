#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    match argv[2]:
        case '+':
            print(f"{a} + {b} = {add(a, b)}")
        case '-':
            print(f"{a} - {b} = {sub(a, b)}")
        case '*':
            print(f"{a} * {b} = {mul(a, b)}")
        case '/':
            print(f"{a} / {b} = {div(a, b)}")
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
