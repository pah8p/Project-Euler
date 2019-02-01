import euler_tools
import copy

primes = euler_tools.sieve(100)

def n(factorization):
    _n = 1
    for k, v in factorization.items():
        _n *= (k**v)
    return _n

def d(factorization):
    _d = 1
    for k, v in factorization.items():
        _d *= (2*v+1)
    return _d

def replace(factorization, factor, limit):
    _factorization = copy.deepcopy(factorization)
    for i in range(2, factor):
        factorization[factor] = 0

        pds = euler_tools.prime_divisors(i)
        for pd in pds:
            factorization[pd] += 1

        print(factor, i, pds, factorization, d(factorization), d(_factorization))

        if 2*limit < d(factorization) :
            return factorization, True
        else:
            factorization = copy.deepcopy(_factorization)
            
    return _factorization, False
        

def min_d(primes, limit):

    i = 1
    while True:
        j = 3**i
        if j > limit:
            break
        i += 1

    primes = sorted(primes[:i], reverse = True)

    factorization = {}
    for p in primes:
        factorization[p] = 1

    for p in primes:
        factorization, updated = replace(factorization, p, limit)
        if not updated:
            return factorization, d(factorization), n(factorization)

    return primes
    

    

print(min_d(primes, 4000000))



