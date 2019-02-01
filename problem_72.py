import euler_tools
import time

def prime_divisor(i, primes):
    s = time.time()
    pds = euler_tools.prime_divisors(i, primes)
    e = time.time() - s
    return pds, e


def tester(n):

    def _key(z):
        return z[1][1] #len(z[1])   
    euler_tools.write_primes(int(n))
    primes = euler_tools.read_primes()
    with euler_tools.Watch():
        print(prime_divisor(9917, primes))
        #x = [(i, prime_divisor(i, primes)) for i in range(411, 412)]
        #print(max(x, key = _key))

#tester(1e4)
#tester(1e6)




#euler_tools.write_primes(D)

#with euler_tools.Watch():
    #print(euler_tools.prime_divisors(12345678))

#euler_tools.write_primes(int(1e6))

#with euler_tools.Watch():
#    print(euler_tools.prime_divisors(12345678))


D = int(1e6)+1

euler_tools.write_primes(int(1e6))
primes = euler_tools.read_primes()

#with euler_tools.Watch():
#    x = [euler_tools.totient(i, primes) for i in range(2, D)]

#print(x)
#print(sum(x))

lst = list(range(D))
for p in primes:
    r = p - 1
    lst[p] = r
    lst[p+p::p] = [i / p * (p-1) for i in lst[p+p::p]]

print(sum(lst[2:]))
