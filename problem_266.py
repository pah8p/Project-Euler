import euler_tools

PRIMES = euler_tools.sieve(190)

FACT = {}

def fact(n):
    try:
        return FACT[n]
    except KeyError:
        if n == 0 or n == 1:
            f = 1
        else:
            f = n*fact(n-1)
        FACT[n] = f
        return f

def combin(n, k):
    return int(fact(n)/(fact(k)*fact(n-k)))

def product(x):
    p = 1
    for _x in x:
        p *= _x
    return p

def num_divisors(num_primes):
    return 1 + sum([combin(num_primes, n) for n in range(1, num_primes+1)])

# def pseudo_sqrt(n):
# index = len(all_divisors(n))/2-1

print(euler_tools.prime_divisors(3102), 3102**0.5)

print(PRIMES, product(PRIMES), product(PRIMES) ** 0.5)

#p = product(PRIMES)

#d = euler_tools.all_divisors(p)

#print(d, len(d), d.index(42))

print(num_divisors(len(PRIMES))/2-1)