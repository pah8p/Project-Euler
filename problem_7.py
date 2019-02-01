
def sieve(n):

    primes = {}
    for n in range(2, n):
        primes[n] = True
    
    for m in range(2, n):

        if not primes[m]:
            pass

        i = 0
        next_mult = 0
        while next_mult <= n:
            next_mult = m**2 + m*i
            primes[next_mult] = False
            i += 1

    return [k for k, v in primes.items() if v]

##x = sieve(1000000)
##
##print(x)
##
## 
##print(len(x))
##
##print(x[10000])
