import pickle
import itertools
import math
import time


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
            next_mult = m ** 2 + m * i
            primes[next_mult] = False
            i += 1

    return [k for k, v in primes.items() if v]


def write_primes(n):
    primes = sieve(n)
    with open('primes.txt', 'wb') as f:
        pickle.dump(primes, f)
    return None


def read_primes():
    with open('primes.txt', 'rb') as f:
        primes = pickle.load(f)
    return primes


# write_primes(int(150e9))
# print(read_primes())

def product(x):
    p = 1
    for _x in x:
        p *= _x
    return p


def combine_divisors(divisors):
    combined = []
    for i in range(len(divisors) + 1):
        for j in itertools.combinations(divisors, i):
            combined.append(product(j))
    return list(set(combined))


def prime_divisors(n, primes=None):
    if not primes:
        primes = read_primes()

    divisors = []
    curr_n = n

    set_primes = set(primes)

    if n in set_primes:
        return [n]

    for p in primes:

        while True:
            if curr_n % p == 0:
                divisors.append(p)
                curr_n /= p
            else:
                break

        if curr_n == 1:
            return divisors

    return divisors


def prime_divisors_2(n):
    primes = read_primes()
    divisors = []
    for p in primes:

        while True:
            if n % p == 0:
                divisors.append(p)
                n /= p

            else:
                break

        if n == 1:
            return divisors


def distinct_prime_divisors(n, primes=None):
    return list(set(prime_divisors(n, primes)))


def all_divisors(n):
    return proper_divisors(n) + [n]


def proper_divisors(n):
    pds = []
    for m in range(2, 1 + int(n ** 0.5)):
        if n % m == 0:
            pds.append(m)
            pds.append(int(n / m))
    return sorted([1] + list(set(pds)))


def totient(n, primes=None):
    phi = n
    for p in distinct_prime_divisors(n, primes):
        phi *= (1 - 1 / p)
    return int(phi)


def is_prime(n):
    if n == 1:
        return False

    for m in range(2, int(n ** 0.5) + 1):
        if n % m == 0:
            return False

    return True


def gcd(n, m):
    r = n % m
    while r > 0:
        n = m
        m = r
        r = n % m
    return m


class Watch(object):

    def __init__(self, msg='Time elapsed'):
        self.msg = msg

    def __enter__(self):
        self._start = time.time()

    def __exit__(self, *args, **kwargs):
        elapsed = (time.time() - self._start) * 1000
        print('%s: %s miliseconds' % (self.msg, round(elapsed, 2)))


class IntervalWatch(object):

    def __init__(self, interval=1000, msg='Time elapsed'):
        self.msg = msg
        self.interval = interval

    def __enter__(self):
        self._start = time.time()

    def __exit__(self, *args, **kwargs):
        elapsed = (time.time() - self._start) * 1000
        if elapsed > self.interval:
            print('%s: %s milliseconds' % (self.msg, elapsed))

def memoize(f, *args):
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            z = f(*args)
            cache[args] = z
            return z
    return _f


class Memoize(object):

    def __init__(self, f):
        self.f = f
        self.cache = {}
        print('Deprecated, switch to euler_tools.memoize')

    def __call__(self, *args):

        try:
            return self.cache[args]

        except KeyError:
            res = self.f(*args)
            self.cache[args] = res
            return res


# print(prime_divisors(24))
# print(all_divisors(24))
#
# for i in range(10):
#    a = prime_divisors(i)
#    b = distinct_prime_divisors(i)
#    d = all_divisors(i)
#    c = totient(i)
#    print('%s %s %s %s %s' % (i, a, b, d, c))

# N = 10000
# write_primes(N)
# with Watch('1'):
#    for i in range(1, int(N/1)):
#        pd1s = prime_divisors(i)
#
# with Watch('2'):
#    for i in range(1, int(N/1)):
#        pd2s = prime_divisors_2(i)
#
# for a, b in zip(pd1s, pd2s):
#    if a != b: print(a, b)
