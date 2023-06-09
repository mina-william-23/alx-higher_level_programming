#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    li = [0, 0]
    for i in range(2):
        if i < len(tuple_a):
            li[i] += tuple_a[i]
        if i < len(tuple_b):
            li[i] += tuple_b[i]
    return tuple(li)
