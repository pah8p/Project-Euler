from decimal import Decimal

N = 1001

##def continued_fraction(n):
##    i = 0
##    a = []
##    while i < N:
##        a.append(math.floor(Decimal(n)))
##        diff = Decimal(n) - math.floor(Decimal(n))
##        if diff == 0:
##            break
##        n = Decimal(1.0)/Decimal(diff)
##        i += 1
##    return a

def a(n):
    if n == 0:
        return 1
    else:
        return 2

H = {}

def h(n):
    try:
        return H[n]
    except KeyError:
        if n == 0:
            _h = a(0)
        elif n == 1:
            _h = a(1)*a(0) + 1
        else:
            _h = a(n)*h(n-1) + h(n-2)

        H[n] = _h
        return _h

K = {}

def k(n):
    try:
        return K[n]
    except KeyError:
        if n == 0:
            _k = 1
        elif n == 1:
            _k = a(1)
        else:
            _k = a(n)*k(n-1) + k(n-2)

        K[n] = _k
        return _k

import math

#a = continued_fraction(math.sqrt(2))
print(len([n for n in range(1, N) if len(str(h(n))) > len(str(k(n)))]))

#for n in range(1, N):
#    print((h(n), k(n)))

print(a)
