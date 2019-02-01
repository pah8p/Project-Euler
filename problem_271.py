
import euler_tools

def check_x(x, nds):
    xds = euler_tools.prime_divisors(x**3-1)
    for nd in nds:
        if nd not in xds:
            return False
    return True

def check_n(n):
    nds = euler_tools.prime_divisors_2(n)
    return [x for x in range(2, n) if check_x(x, nds)]


def check(n):
    for x in check_n(n):
        print(x, euler_tools.prime_divisors_2(n), euler_tools.prime_divisors(x**3-1))
    
##check(2)
##print('---')
##check(3)
##print('---')
##check(5)
##print('---')
##check(7)
##print('---')
##check(210)

def product(ps):
    _p = 1
    for p in ps:
        _p *= p
    return _p

def sieve(primes):

    prod = product(primes)
    _sieve = [1]*(1+prod)

    for p in primes:
        k = 1
        while True:

            x1 = k*p+1
            try:
                _sieve[x1] *= p
            except IndexError:
                pass

            x2 = ((4*k*p-3)**0.5-1)/2
            if x2.is_integer():
                _sieve[int(x2)] *= p
                
            k += 1
            if k*p > prod**2+prod+1:
                break
            
    return _sieve

primes = [2, 3, 5, 7, 13]
sn = 0

with euler_tools.Watch():
    for n, s in enumerate(sieve(primes)):
        if s >= product(primes):
            print(n, s)
            sn += n

print(sn)
        



