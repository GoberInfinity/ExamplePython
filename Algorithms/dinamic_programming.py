def fib(n):
    """
    :type n: int
    :rtype: int
    """
    vals = [0, 1]
    if n < 2:
        return vals[n]
    for x in range(2, n + 1):
        vals.append(vals[x - 1] + vals[x - 2])
    return vals[n]


print(fib(10000))
