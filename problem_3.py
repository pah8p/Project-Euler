

def sieve(n):

    primes = list(range(2, n))

    for m in range(2, n):

        if m not in primes:
            pass

        i = int(n / m)

        for j in range(2, i):
            try:
                primes.remove(j * m)
            except ValueError:
                pass
    
    return primes

def prime_factors(n):
    factors = []
    for m in sieve(10000):
        if n % m == 0:
            factors.append(m)
    return factors

##def largest_prime_factor(n):
##    m = n
##    lpf = 2
##    while lpf < m:
##
##        if n % lpf == 0:
##
##            print(lpf)
##
##            while m % lpf
##
##            
##            print(m)
##
##        lpf += 1
##
##    return lpf



'''print(prime_factors(600851475143))'''

