import itertools
import euler_tools

primes = euler_tools.sieve(10**4)

IP = {}

def is_prime(n):
    try:
        return IP[n]
    except KeyError:
        ip = _is_prime(n)
        IP[n] = ip
        return ip

def _is_prime(n):
    if n == 1:
        return False

    for m in range(2, int(n**0.5)+1):
        if n % m == 0:
            return False

    return True

CIP = {}

def concat_is_prime(n, m):
    try:
        return CIP[(n, m)]
    except KeyError:
        try:
            return CIP[(m, n)]
        except KeyError:
            nm = int('%s%s' % (n, m))
            mn = int('%s%s' % (m, n))
            cip = is_prime(nm) and is_prime(mn)
            CIP[(n, m)] = cip
            CIP[(m, n)] = cip
            return cip

sets = []

for p1 in range(len(primes)):

    print(p1, len(primes))
    
    for p2 in range(p1, len(primes)):

        if concat_is_prime(primes[p1], primes[p2]):

            for p3 in range(p2, len(primes)):

                if concat_is_prime(primes[p1], primes[p3]):
                    if concat_is_prime(primes[p2], primes[p3]):

                        for p4 in range(p3, len(primes)):

                            if concat_is_prime(primes[p1], primes[p4]):
                                if concat_is_prime(primes[p2], primes[p4]):
                                    if concat_is_prime(primes[p3], primes[p4]):
                            
                                        for p5 in range(p4, len(primes)):

                                            if concat_is_prime(primes[p1], primes[p5]):
                                                if concat_is_prime(primes[p2], primes[p5]):
                                                    if concat_is_prime(primes[p3], primes[p5]):
                                                        if concat_is_prime(primes[p4], primes[p5]):
                                            

                                                            _set = [primes[p1], primes[p2], primes[p3], primes[p4], primes[p5]]
                                                            sets.append((sum(_set), _set))

print(sets)
print(min(sets, key=lambda x: x[0]))
