
import euler_tools

N = int(1e7)

#euler_tools.write_primes(N)
PRIMES = euler_tools.read_primes()

print(len(PRIMES))

def totients(n):
    t = list(range(1, n+1))
    for p in PRIMES:

        m = 1
        while m*p <= n:
            t[m*p-1] *= (1-1/p)
            m += 1

    return [int(_t) for _t in t]

#phis = totients(N)

#print(max(phis))

#for n, phi in enumerate(phis):
#    if phi == 7830456:
#        print(n, phi)

print(euler_tools.totient(7830456))
print(euler_tools.totient(9151638))
