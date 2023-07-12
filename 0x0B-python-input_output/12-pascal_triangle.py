#!/usr/bin/python3
''' pascal module '''


def pascal_triangle(n):
    ''' pascal representation '''
    nw = []
    res = []
    while (n):
        old = nw[:]
        for i in range(1, len(old)):
            nw[i] = old[i] + old[i - 1]
        nw.append(1)
        res.append(nw[:])
        n -= 1
    return res
