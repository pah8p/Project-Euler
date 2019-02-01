
from problem_7 import sieve
import itertools

PRIMES = sieve(int(1e7))[::-1]

def is_pandigital(n):
    digits = [str(m) for m in range(1,1+len(str(n)))]
    return list(sorted(set(str(n))))==digits

print(is_pandigital(125354))

for prime in PRIMES:
    if is_pandigital(prime):
        print(prime)
        break

