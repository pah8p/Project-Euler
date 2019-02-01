import math
import time
import euler_tools
import pickle
import itertools

from decimal import Decimal
import decimal
import math

decimal.getcontext().prec = 250

TRIPLES = [
    [3, 4, 5],
    [5, 12, 13],
    [8, 15, 17],
    [7, 24, 25],
    [20, 21, 29],
    [12, 35, 37],
    [9, 40, 41],
    [28, 45, 53],
    [9, 12, 15],
    [64, 120, 136],
    [39350529, 68149872, 78694785],
]


#A=b*sqrt(s**2-(b/2)**2)/2
#A=b*sqrt(s**2/4-b**2/16)
#A=sqrt((b*s/2)**2-(b**4)/16)

#a**2+(b**2/4)**2=(b*s/2)**2

#(9, 12, 15):

#    12=b**2/4

#    13=(b*s/2)

##b=sqrt(4*B)
##2C=sqrt(4*B)*s
##s=2C/sqrt(4*B)
##
##B==4: 
##
##b=sqrt(4*B)
    

def area(side, base):
    try:
        #height = math.sqrt(side**2 - (base/2)**2)
        height = Decimal(side**2-(base/2)**2).sqrt()
    except ValueError:
        return 0.5
    return base*height/2

def brute_force(perim):
    s = 0
    max_x = 0
    for x in range(5, int(perim/3)):
        if x % int(1e6) == 0:
            print(x)
        for y in [-1, 1]:
            a = area(x, x+y)
            if a.is_integer():
                if 3*x+y<perim:
                    s += 3*x+y
                    print(x, x+y, a)
                    max_x = max(max_x, x)
    return s

def pythag_triples(m_max):
    triples = []
    for m in range(2, m_max):
        #if m % 100 == 0: print(m)
        for n in range(1, m):
            #with euler_tools.Watch('Coprime %s %s' % (m, n)):
            if coprime(m, n):
                if (m+n) % 2 == 1:
                    triples.append(pythag_triple(m, n))
    return triples

def pythag_triple(x, y):
    return {
        'a': x**2-y**2,
        'b': 2*x*y,
        'c': x**2+y**2,
        'm': x,
        'n': y,
    }

def check_triple(a, b, c, m, n):
    if min(a, b, c) % 2 == 1:
        k = m**2-n**2
        A = k*a
        B = k*b
    else:
        k = 2*m*n
        A = k*b
        B = k*a
    C=k*c
    base = math.sqrt(4*A)
    side = 2*C/base
    #print(A, B, C)
    #if c == 17:
        #print(a, b, c, m, n, k, A, B, C, base, side)

    if 516309057 in [a, b]:
        print(side, base, A, B, C)
    
    
    if abs(side-base)==1:
        #print(a, b, c, m, n, k, A, B, C, base, side)
        print(side, base, A, B, C)
        return base + 2*side, A, B, C
    else:
        return 0, 0, 0, 0
    
def sum_perimeters(max_perim, primitives):
    s = 0
    max_perim_hit = False
    mp = 0
    for triangle in primitives:
        check = check_triple(**triangle)
        if check[0] and check[0] < max_perim:
            s += check[0]

        mp = max(mp, check[0])

        if check[0] > max_perim:
            max_perim_hit = True

        check2 = check_triple(**{k: v/4 for k, v in triangle.items()})
        if check2[0] and check2[0] < max_perim:
            s += check2[0]

    return s, max_perim_hit, mp

def only_check_primitives(perim_max, primitives):
    s = 0
    for p in primitives:
        c = p['c']
        a = min(p['a'], p['b'])
        if 1 == abs(c - 2*a):
            perim = 2*(c+a)
            if perim < perim_max:
                s += perim
                print(p)
    return s

def check_k(perim_max, primitives):
    s = 0
    for p in primitives:
        c = p['c']
        a = min(p['a'], p['b'])
        k = abs(c-2*a)
        #print(k, c, a, p)
        if k in all_divisors(2*a) and k in all_divisors(c):
            perim = 2*(c+a)
            if perim < perim_max:
                s += perim
                print(p)
    return s

#def check_triple_2(triple):


ADS = {}

def product(x):
    p = 1
    for _x in x:
        p *= _x
    return p

def all_divisors(n):
    try:
        return ADS[n]
    except KeyError:
        divisors = prime_divisors(n)
        combined = []
        for i in range(len(divisors)+1):
            for j in itertools.combinations(divisors, i):
                combined.append(product(j))
        ads = list(set(combined))
        ADS[n] = ads
        return ads

PDS = {}

def prime_divisors(n):
    try:
        return PDS[n]
    except KeyError:
        #with euler_tools.Watch('PRIME DIVISORS %s' % n):
        pds = euler_tools.prime_divisors(n)
        PDS[n] = pds
        return pds

CP = {}

def coprime(n, m):
    try:
        return CP[(n, m)]
    except KeyError:
        n_divisors = prime_divisors(n)
        m_divisors = prime_divisors(m)
        common_divisors = list(set(n_divisors) & set(m_divisors))
        CP[(n, m)] = not common_divisors
        return not common_divisors

def write_triples(n):
    primes = pythag_triples(n)
    with open('C:/Users/Pete/AppData/Local/Programs/Python/Python36-32/Scripts/euler/pythag_triples.txt', 'wb') as f:
        pickle.dump(primes, f)
    return None

def read_triples():
    with open('C:/Users/Pete/AppData/Local/Programs/Python/Python36-32/Scripts/euler/pythag_triples.txt', 'rb') as f:
        primes = pickle.load(f)
    return primes

N = int(1e7)


#print(check_k(N, [{'a': 20, 'b': 21, 'c': 29}]))

#primitives = pythag_triples(1000)

with euler_tools.Watch():
    #print(sum_perimeters(N, primitives))
    print(brute_force(N))
    #print(only_check_primitives(N, primitives))
    #print(check_k(N, primitives))

