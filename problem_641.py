
import euler_tools

'''for n < N, n = PROD(p**np) pick n such that PROD(np+1) == 1 MOD 6'''

primes = euler_tools.sieve(int(1e6))

def sieve(n):
    a = [1]*n

    for m in range(2, n+1):
        if m % 1e6 == 0:
            print(m)
        k = 1
        while True:
            if m*k <= len(a):
                if a[m*k-1] == 6:
                    a[m*k-1] = 1
                else:
                    a[m*k-1] += 1
                k += 1
            else:
                break

    return a

def pairs():
    i = 1
    while True:
        if 2**i > 1e36:
            break
        for j in range(1, i+1):
            if (i+1)*(j+1) % 6 == 1:
                print(i, j)
        i += 1
    

def ones(n):
    dice = sieve(n)
    #print(dice)
    #print(len(dice))
    return sum([d for d in dice if d == 1])

def keys(n):
    dice = sieve(n)
    p = 1
    for m in range(1, n+1):
        o = sum([d for d in dice[:m] if d == 1])
        if p+1 == o:
            print(m, o, euler_tools.prime_divisors(m))
            p = o
    return None

with euler_tools.Watch():
    keys(100)

print(10**8)
print(1e8)
pairs()
