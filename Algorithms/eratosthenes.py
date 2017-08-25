import math

def get_primes(n):
    m = n+1
    numbers = [True for i in range(m)]
    #You only need to start crossing out multiples at p2, because any smaller multiple
    # of p has a prime divisor less than p and has already been crossed out as a multiple
    # of that. This is also the reason why we can stop after we’ve reached sqrt(n)
.
    for i in range(2, int(math.sqrt(n))):   
        if numbers[i]:
            for j in range(i*i, m, i):
                numbers[j] = False
        primes = []
    for i in range(2, m):
        if numbers[i]:
            primes.append(i)
    return primes

print(get_primes(10))