
import euler_tools

N = int(1e5)

primes = euler_tools.sieve(N)


def rads(n):

    _rads = [1] * n

    for p in primes:
        
        k = 1
        while True:
            
            if p*k <= n:
                _rads[p*k-1] *= p
                k += 1
                
            else:
                break

#    print(max(_rads))

    _rads = [(n+1, rad) for n, rad in enumerate(_rads)]

    #print(_rads)
    return sorted(_rads, key=lambda x: x[1])

#x = rads(N)
#print(x)
#print(x[9999])
#for xx in x[:10]: print(x)
