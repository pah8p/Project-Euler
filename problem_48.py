
from problem_7 import sieve

PRIMES = sieve(1000)

def prime_factors(n):
    factors = []
    curr_n = n
    for p in PRIMES:
        if curr_n % p == 0:
            factors.append(p)

            curr_n /= p
            while True:
                if curr_n % p == 0:
                    factors.append(p)
                    curr_n /= p
                else:
                    break

    return factors

EXPONENTS = {}

def exponentiate(x, y):
    try:
        return EXPONENTS['%s**%s' % (x, y)]
    except KeyError:
        z = x**y
        EXPONENTS['%s**%s' % (x, y)] = z
        return z

def self_exponentiate(n):
    z = 1
    factors = prime_factors(n)
    for x in factors:
        zz = x
        for y in factors:
            zz = zz**y
        z *= zz
    return z
            
s = sum([self_exponentiate(i) for i in range(1, 1001)])
print(s % 10**10)
    
print(sum([i**i for i in range(1, 1001)]) % 10**10)
    
