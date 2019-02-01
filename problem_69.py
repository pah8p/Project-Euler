import itertools
import math
from problem_7 import sieve
import time

N = int(1e6)
PRIMES = sieve(N)
print('Generated Primes')
DIVISORS = {}

def product(x):
    p = 1
    for _x in x:
        p *= _x
    return p

def get_prime_divisors(n):

    try:
        return DIVISORS[n]
        
    except KeyError:
        s = time.time()
        divisors = []
        curr_n = n
        #print(time.time()-s)
        #for p in PRIMES:
        i = 0
        p = PRIMES[i]
        while p <= math.sqrt(n):    
            #if p >= math.sqrt(n):
            #    break

            if curr_n % p == 0:
                divisors.append(p)

                curr_n /= p
                while True:
                    if curr_n % p == 0:
                        divisors.append(p)
                        curr_n /= p
                    else:
                        break

            i += 1
            p = PRIMES[i]

        divisors = list(set(divisors))                
        DIVISORS[n] = divisors
        #print(time.time()-s)
        return divisors
    
def get_phi(n):
    _phi = n
    prime_divisors = get_prime_divisors(n)
    for p in prime_divisors:
        _phi *= (1 - 1/p)
    #print('%s --- %s --- %s' % (n, _phi, prime_divisors))
    return _phi

_max = 0
_max_n = 0
for n in range(2, N):

    if n % 1000 == 0:
        print(n)

    phi = get_phi(n)
    
##    phi = 1
##    if n not in PRIMES:
##        
##        n_divisors = get_divisors(n)
##        for m in range(2, n):
##            m_divisors = get_divisors(m)
##
##            if list(set(n_divisors) & set(m_divisors)) == [1]:
##                phi += 1

    if n/phi > _max:
        _max = n/phi
        _max_n = n

print(_max_n)










        

