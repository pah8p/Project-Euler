
import euler_tools

N = int(1e7)

#euler_tools.write_primes(N)
PRIMES = euler_tools.read_primes()

def totients(n):
    t = list(range(1, n+1))
    for p in PRIMES:

        m = 1
        while m*p <= n:
            t[m*p-1] *= (1-1/p)
            m += 1

    return [int(_t) for _t in t]

def permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


with euler_tools.Watch():
    phis = totients(N)
    permutations = []
    for n, phi in enumerate(phis):
        #print(n, phi)
        if permutation(n+1, phi) and n != 0: #and n != phi:
            permutations.append((n+1, phi, (n+1)/phi))

    print(min(permutations, key = lambda x: x[2]))

    print([p for p in permutations if p[0] == 87109])
