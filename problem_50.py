
from problem_7 import sieve

N = 1000000

PRIMES = sieve(N)

def find_length(n, ceiling):

    for i in range(N-n):
        s = sum(PRIMES[i:i+n])
        if s >= ceiling:
            break

        if s in PRIMES:
            return (n, s)

    return None

def find_max_length(celing):
    for n in range(200, 1000):
        length = find_length(n, N)
        if length:
            print(length)








print(find_max_length(N))
