#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = [0, 0]

    for i in range(len(tuple_a)):
        if i > 1:
            break
        if tuple_a[i] is not None:
            sum[i] += tuple_a[i]

    for i in range(len(tuple_b)):
        if i > 1:
            break
        if tuple_b[i] is not None:
            sum[i] += tuple_b[i]

    return (sum[0], sum[1])
