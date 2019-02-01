


triangle = lambda n: n*(n+1)/2
square = lambda n: n**2
pentagon = lambda n: n*(3*n-1)/2
hexagon = lambda n: n*(2*n-1)
heptagon = lambda n: n*(5*n-3)/2
octagon = lambda n: n*(3*n-2)

def values(f):
    n = 1
    _values = []
    f_n = 0
    while f_n < 10000:
        f_n = int(f(n))
        if 1000 <= f_n < 10000:
            _values.append(f_n)
        n += 1
    return _values

triangles = values(triangle)
squares = values(square)
pentagons = values(pentagon)
hexagons = values(hexagon)
heptagons = values(heptagon)
octagons = values(octagon)

is_cyclic = lambda n, m: str(n)[-2:] == str(m)[:2]

def find_cyclic(a, b, c, d, e, f):
    cyclics = []
    for _a in a:
        for _b in b:
            if is_cyclic(_a, _b):
                for _c in c:
                    if is_cyclic(_b, _c):
                        for _d in d:
                            if is_cyclic(_c, _d):
                                for _e in e:
                                    if is_cyclic(_d, _e):
                                        for _f in f:
                                            if is_cyclic(_e, _f) and is_cyclic(_f, _a):
                                                cyclics.append([_a, _b, _c, _d, _e, _f])
    return cyclics
                                        
values = [triangles, squares, pentagons, hexagons, heptagons, octagons]

print(find_cyclic(*values))

import itertools

all_values = list(itertools.permutations(values))

for all_value in all_values:

    res = find_cyclic(*all_value)
    if res: print(res, sum(res[0]))
    





