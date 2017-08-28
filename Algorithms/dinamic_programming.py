# -*- coding: utf-8 -*-
def fib(n):
    vals = [0,1]
    if n < 2:
        return vals[n]
    for x in range(2,n+1):
        vals.append(vals[x-1] + vals[x-2])
    return vals[n]

print(fib(4))