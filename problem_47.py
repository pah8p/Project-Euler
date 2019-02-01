from math import sqrt
from problem_7 import sieve
import itertools

PRIMES = sieve(1000)

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
                
    return len(set(divisors))

def check_divisors_2(n, goal):
    for i in range(goal):
        if num_divisors(n+i) == goal:
            pass
        else:
            return False, n+i+1
    return True, n

GOAL = 4
i = 1
while True:

    success, result = check_divisors_2(i, GOAL)

    if success:
        print(result)
        break
    else:
        i = result

    if i % 1000 == 0:
        print('%s----' % (i))
