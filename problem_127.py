
import collections
import euler_tools
import fractions
import itertools
import problem_124

def product(iterable):
    p = 1
    for i in iterable:
        p *= i
    return p

def prime_factors(n):
    primes = euler_tools.sieve(n)
    factors = collections.defaultdict(list)
    for p in primes:
        j = 1
        while True:
            factors[p*j].append(p)
            j += 1
            if p*j > n:
                break

    return factors

def radicals(n):
    factors = prime_factors(n)

    _rads = {}
    for k, v in factors.items():
        _rads[k] = product(set(v))

    _rads[1] = 1

    return _rads

GCD = {}

GCD_MISS = []
GCD_HIT = []

def gcd(n, m):
    n, m = max(n, m), min(n, m)
    try:
        m = GCD[(n, m)]
        GCD_HIT.append(1)
        return m
    except KeyError:
        GCD_MISS.append(1)
        _n = n
        _m = m
        r = n % m
        while r > 0:
            n = m
            m = r
            r = n % m
        #GCD[(_n, _m)] = m
        return m


def abc_hit(a, b, c, rads):
    
    if a < b:

        #with euler_tools.Watch('gcd %s %s' % (a, b)):
        #    gcd_ab = gcd(a, b)
        
        #if gcd(a, b) == 1:

        if rads[a]*rads[b] == rads[rads[a]*rads[b]]:
                
            rad = rads[a]*rads[b]*rads[c]

            if rad < c:
                #print(a, b, c)
                return True

    return False

def farey_sequence(n):
    pairs = []
    a, b, c, d = 0, 1, 1, n

    #pairs.append((a, b))

    while c <= n:
        k = int((n+b)/d)
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        if a != 0 and b != 0 and a != b:
            pairs.append((a, b))

    return pairs

##def _coprime_pairs(seeds, c_max):
##    all_kids = []
##    for seed in seeds:
##        kids = coprime_kids(*seed, c_max)
##        for kid in kids:
##            all_kids.append(kid)
##    return all_kids

##def coprime_pairs(c_max):
##    seeds = [(2, 1), (3, 1)]
##    pairs = []
##    while True:
##        if seeds:
##        
##            ps = _coprime_pairs(seeds, c_max)
##            for p in ps:
##                pairs.append(p)
##            seeds = ps
##
##        else:
##            break
##
##    return list(set(pairs))
##        
##        
##def coprime_kids(m, n, c_max):
##    a = [
##        (2*m-n, m),
##        (2*m+n, m),
##        (m+2*n, n),
##    ]
##    __a = []
##    for _a in a:
##        if _a[0] < c_max:
##            __a.append(_a)
##    return __a

##def abc_tuple(c, b, rads, c_max):
##    if c > c_max:
##        print('c hit %s' % c)
##        return 0
##    a = c-b
##    rad = rads[a]*rads[b]*rads[c]
##    if rad < c:
##        print(a, b, c, rad)
##        return c
##    else:
##        return 0
##
##def abc_tuples(c_max, seeds, rads):
##    if seeds == []:
##        return 0, []
##    kids = []
##    sum_c = 0
##    for seed in seeds:
##        #if seed[0] > c_max:
##            #print(len(coprime_kids(*seed, c_max)))
##        sum_c += abc_tuple(*seed, rads, c_max)        
##        for child in coprime_kids(*seed, c_max):
##            kids.append(child)
##    return sum_c, kids
##        
##def abc_hits_2(c_max):
##    try:
##        count = 0
##        sum_c = 0
##       rads = radicals(c_max)
##        seeds = [(2, 1), (3, 1)]
##        while True:
##            _sum_c, seeds = abc_tuples(c_max, seeds, rads)
##            sum_c += _sum_c
##            if seeds == []:
##                break
##        return int(sum_c/2)
##    except KeyboardInterrupt:
##        print(sum_c)

def abc_hits_3(c_max):
    count = 0
    sum_c = 0
    rads = radicals(c_max)

    a, b, c, d = 0, 1, 1, c_max

    #pairs.append((a, b))

    while c <= c_max:
        k = int((c_max+b)/d)
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        if a != 0 and b != 0 and a != b:
            #pairs.append((a, b))
            #print(a, b)

            _c = b
            _b = a

            _a=_c-_b

            rad = rads[_a]*rads[_b]*rads[_c]

            if rad < _c and _a < _b < _c:
                #print(_a, _b, _c)
                sum_c += _c
                count += 1

    return count, sum_c

def abc_hits(c_max):
    count = 0
    sum_c = 0
    with euler_tools.Watch('rads'):
        rads = radicals(c_max)
        
    for c in range(3, c_max):
        if c % 2500 == 0: print(c)

        for b in range(1, c):

            a=c-b

            #with euler_tools.Watch((a, b, c)):
            hit = abc_hit(a, b, c, rads)
                
            if hit:
                count += 1
                sum_c += c

    return count, sum_c


def abc_hits_4(n):
    sum_c = 0
    rads = radicals(n) #problem_124.rads(n)
    
    for b in range(1, n):
        for c in range(b+1, n):

            a = c-b

            rad_a = rads[a]
            rad_b = rads[b]
            rad_c = rads[c]
            
            if rad_a < (b/rad_b):
                    if rad_a*rad_b*rad_c < c:
                        if a < b < c:
                            if gcd(a, b)==1:
                                sum_c += c
                        #print(a, b, c)
    return sum_c
                    
            
#cp = coprime(10)

#print(
#    cp[9][2], cp[9][7]
#)

#with euler_tools.Watch():
    #print(farey_sequence(1000))
    #print(coprime_pairs(10))
    #print(abc_hits_3(5000))

with euler_tools.Watch():
    print(abc_hits_4(10000))
    #for k, v in GCD.items():
    #    if v != 1: print(k)
    #print(len(GCD_MISS))
    #print(len(GCD_HIT))
