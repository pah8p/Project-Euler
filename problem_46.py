from problem_7 import sieve
import math

N = 1000

PRIMES = sieve(10000)

n = 3
while True:

    if n in PRIMES or n % 2 == 0:
        pass

    else:

        found = False
        for p in PRIMES:

            square = (n - p)/2

            if square > 0:
                if int(math.sqrt(square)) == math.sqrt(square):
                    found = True
                    break

        if not found:
            print(n)
            break

    n += 1
