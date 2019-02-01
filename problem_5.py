from problem_3 import sieve
from collections import defaultdict

N = 20
factors = []
for prime in sieve(N):
    m = 1
    while prime**m < N:
        m += 1

    if prime**(m-1) not in factors:
        factors.append(prime**(m-1))

print(factors)

p = 1
for v in factors:
    p *= v
    print(p)

print(p)



