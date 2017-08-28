# -*- coding: utf-8 -*-
def fib(n):
    vals = [0,1]
    if n < 2:
        return vals[n]
    for x in range(2,n+1):
        vals.append(vals[x-1] + vals[x-2])
    return vals[n]

print(fib(10000))

def lis(arr):
    n = len(arr)

    lis = [1]*n

    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1

    maximum = 0

    for i in range(n):
        maximum = max(maximum , lis[i])
    return maximum

print(lis([10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]))