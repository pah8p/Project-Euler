import euler_tools

##print(euler_tools.prime_divisors(1e9))
##print(euler_tools.prime_divisors(428571428570))

##for i in range(1, 20):
##    d = 10**i
##    n = int(3/7*d)
##
##    d_factors = euler_tools.prime_divisors(d)
##    n_factors = euler_tools.prime_divisors(n)
##    common = list(set(d_factors) & set(n_factors))
##    for factor in common:
##        d /= factor
##        n /= factor
##
##    if d <= 1e6:
##
##        print('%s -- %s -- %s' % (i, n, d))


CP = {}

PRIMES = euler_tools.read_primes()

def coprime(n, m):
    try:
        return CP[(n, m)]
    except KeyError:
        _coprime = True
        for p in PRIMES:

            if p > min(n, m):
                break
            
            if n % p == 0 and m % p == 0:
                _coprime = False
                break
    
        CP[(n, m)] = _coprime
        return _coprime
    
N = int(1e6)

def search():
    guesses = []
    for n in range(N, 7, -1):
        if n % 10000 == 0: print(n)
        for m in range(int(n*2999999/7000000), int(n*3/7)):
            #print(n, m)
            if coprime(n, m):
                guesses.append((n, m, m/n, 3/7-m/n))
    return guesses

x = search()

print(min(x, key = lambda x: x[3]))

    
