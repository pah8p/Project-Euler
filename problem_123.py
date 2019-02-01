
import euler_tools

PRIMES = euler_tools.sieve(int(3e5))
print(PRIMES[2])
def n_min(r_max):
    
    for n, p in enumerate(PRIMES):

        r = 2*p*(1+n)

        print(r, p, n+1, r<p**2)

        if r >= r_max:

            return n+1, p, r, n, PRIMES[n-1], 2*PRIMES[n-1]*n

    return None
        
print(n_min(1e10))
