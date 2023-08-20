#!/usr/bin/env python3

def print_fibonacci(length):
    fibb_list = []
    r, a = 0, 1
    for o in range(length):
        fibb_list.append(r)
        r, a=a, r+a
    print(fibb_list)
    pass