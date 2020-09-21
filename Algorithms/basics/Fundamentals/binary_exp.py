def binary_exponentiation(a, n):
    result = 1
    while n:
        if n & 1:
            result = result * a
        a = a * a
        n = n >> 1
    return result


for n in range(0, 50):
    print(f"2^{n} ={binary_exponentiation(2,n)}")
