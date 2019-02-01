from decimal import Decimal
import decimal
import math

decimal.getcontext().prec = 250

def find_mn(A, B, C):
    err = []
    _m = Decimal(C).sqrt() + 1
    for m in range(1, int(_m)):
        n = Decimal(C-m**2).sqrt()
        m = Decimal(m)
        _a = m**2-n**2
        _b = 2*m*n
        a, b = min(_a, _b), max(_a, _b)
        c = m**2+n**2

        ss = (A-a)**2 + (B-b)**2 + (C-c)**2
        err.append((ss, m, n))

        if c == C:
            #print(m, n)
            if b == B:
                if a == A:
                    return m, n

    return min(err, key = lambda x: x[0])

def coprime_triple(m, n):
    triples = [
        (2*m-n, m),
        (2*m+n, m),
        (m+2*n, n),
    ]
    odd = lambda m, n: (m+n)%2==1
    return [t for t in triples if odd(*t)]

def pythagorean_triple(m, n):
    _a = m**2-n**2
    _b = 2*m*n
    a, b = min(_a, _b), max(_a, _b)
    c = m**2+n**2
    k = abs(c-2*a)
    x = c/k
    y = 2*a/k
    p = 2*x+y
    area = a*b/(k**2)
    return a, b, c, x, y, p, area

def check_triple(a, b, c, x, y, p, area, p_max):
    if p > p_max:
        print('p hit %s' % p)
    if x.is_integer() and y.is_integer() and p < p_max:
        print(a, b, c, x, y, p, area)
        return p
    else:
        return 0

def check_tuple(m, n, p_max):
    return check_triple(*pythagorean_triple(m, n), p_max)

def get_sum(seeds, p_max):
    s = 0
    children = []
    for seed in seeds:
        s += check_tuple(*seed, p_max)
        for t in coprime_triple(*seed):
            children.append(t)
    return s, children

def find_sum(p_max):
    s = 0
    seeds = [(2, 1), (3, 1)]
    while True:
        sum_seeds, seeds = get_sum(seeds, p_max)
        s += sum_seeds
        print('Curr sum = %s, Curr tuple = %s' % (s, len(seeds)))
    return s

print(find_sum(1e9))

#print(find_mn(516309057, 894260792, 1032607092))
#print(find_mn(63250208, 109552575, 126500417))
#print(find_sum(1e9))

#print(find_mn(6, 8, 10))
