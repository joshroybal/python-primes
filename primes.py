import math

# Function returns the smallest proper divisor of n.
def smallest_divisor(n):
    sd = n
    if n % 2 == 0:
        sd = 2
    elif n % 3 == 0:
        sd = 3
    i = 5
    while sd == n and i * i <= n:
        if n % i == 0:
            sd = i
        elif n % (i + 2) == 0:
            sd = i + 2
        i += 6
    return sd

# Function returns true when n is prime.
def is_prime(n):
    result = True
    if n < 2 or smallest_divisor(n) != n: result = False
    return result

# Function returns list of prime factors of n.
def factorize(n):
    factors = []
    if n > 1:
        factor = smallest_divisor(n)
        rest = n // factor
        factors.append(factor)
        while rest != 1 and not is_prime(rest):
            factor = smallest_divisor(rest)
            factors.append(factor)
            rest //= factor
        if is_prime(rest):
            factors.append(rest)
    return factors

# Eratosthenes himself skipped the even numbers!
def sieve(n):
    #t = [ i + 2 for i in range(n - 1) ]
    t = [ 2 ]
    for i in range(3, n + 1, 2):
        t.append(i)
    for i in range(2, int(math.sqrt(n)) + 1):
        for j in range(i + i, n + 1, i):
            if j in t: t.remove(j)
    return t

# Construct Sieve of Eratosthenes in discrete segments.
def segmented_sieve(n):
    m = int(math.sqrt(n))
    p = sieve(m)
    t = p.copy()
    for i in range(m + 1, n + 1, m):
        segment = list(filter(lambda z: z % 2 != 0, [j for j in range(i,min(i+m,n+1))]))
        for j in p:
            segment = list(filter(lambda z: z % j != 0, segment.copy()))
            #x = j * (i // j)
            #if x < i:
            #    x += j
            #for k in range(x, i + m, j):
            #    if k in segment:
            #        segment.remove(k)
        t.extend(segment)
    return t

# Alternative prime list construction function.
def primes(n):
    return tuple(filter(is_prime, [ i for i in range(2, n + 1) ]))

# Prime countin function.
def count_primes(n):
    p = 0
    for i in range(2, n + 1):
        if is_prime(i):
            p += 1
    return p
