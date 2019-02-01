
import euler_tools

N = 1e6

primes = euler_tools.sieve(int(N))
print(primes)
res = []

for p in range(1, int(N)+1):
    k = p+1
    #print(p, k)
    _p = k**2+k*p+p**2
    if _p in primes:
        res.append(_p)
        print(_p, p**3, k*p**2, p, k)

##    k = p-1
##    _p = k**2+k*p+p**2
##    if _p in primes:
##        res.append(_p)
##        print(_p, p**3, k*p**2, p, k)

    if _p > N:
        break

with euler_tools.Watch():
    print(len(set(res)))
