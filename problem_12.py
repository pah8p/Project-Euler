from math import sqrt
from problem_7 import sieve
import itertools

PRIMES = sieve(100000)

def triangle_number(n):
    return sum(range(1, n+1))

def product(x):
    p = 1
    for _x in x:
        p *= _x
    return p

def combine_divisors(divisors):
    combined = []
    for i in range(len(divisors)+1):
        for j in itertools.combinations(divisors, i):
            combined.append(product(j))
    return list(set(combined))

def num_divisors(n):
    divisors = []
    curr_n = n
    for p in PRIMES:
        if curr_n % p == 0:
            divisors.append(p)

            curr_n /= p
            while True:
                if curr_n % p == 0:
                    divisors.append(p)
                    curr_n /= p
                else:
                    break

    return len(combine_divisors(divisors))

i = 1
while True:

    triangle = triangle_number(i)
    x = num_divisors(triangle)

    if x > 500:
        print(triangle)
        break
    
    i += 1

    if i % 100 == 0:
        print('%s----%s' % (i, x))
