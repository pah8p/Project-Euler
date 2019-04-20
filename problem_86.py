
import euler_tools
import math
from fractions import Fraction

def x_min(a, b, c):
    return (a*b*c-a**2*c)/(b**2-a**2)

def distance(a, b, c):
    x = x_min(a, b, c)
    return (a**2+x**2)**0.5 + ((c-x)**2+b**2)**0.5

def theta(a, b, c):
    x = x_min(a, b, c)
    return math.atan(x/a) + math.atan((c-x)/b)

def is_int(x):
    if x.is_integer():
        return True

    if x-int(x) > 0.9999:
        return True

    if x-int(x) < 0.0001:
        return True

    return False

def min_distance(a, b, c):

    def d(a, b, c):
        try:
            return [distance(a, b, c), a, b, c, x_min(a, b, c), theta(a, b, c)]
        except ZeroDivisionError:
            return [1e6 + 0.1, None, None, None, None, None]

    ds = [
        d(a, b, c),
        d(c, b, a),
        d(c, a, b),
    ]

    return min(ds, key=lambda x: x[0])

def count(m):
    ts = {}
    n = []
    for c in range(1, m+1):
        for b in range(1, c+1):
            for a in range(1, b+1):

                d = min_distance(a, b, c)
                if is_int(d[0]):
                    n.append((a, b, c))
                    

                    frac = Fraction(d[-1]/math.pi).limit_denominator()

                    k = (math.sin(d[-1]), frac)

                    

                    try:
                        ts[k] += 1
                    except KeyError:
                        ts[k] = 1

    for k, v in sorted(ts.items(), key=lambda x: x[1]):
        print(k, v)

    return len(n)

with euler_tools.Watch():
    print(count(100))


#print(distance(2, 49, 68))

a = 100
b = 95
c = 10

'''
print(distance(a, b, c))
print(distance(c, b, a))
print(distance(b, a, c))
print(distance(c, a, b))
print(distance(a, c, b))
print(distance(b, c, a))
'''










