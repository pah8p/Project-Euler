
p = []

for e in range(1, 100):
    for c in range(e+1, 100):
        for a in range(c+1, 100):
            b = (c**2-e**2)**0.5
            d = (a**2-e**2)**0.5
            f = (a**2-c**2)**0.5

            x = (a**2+b**2)/2
            y = (e**2+f**2)/2
            z = (c**2+d**2)/2

            #if z < y < x:
            if x.is_integer():
                if y.is_integer():
                    if z.is_integer():
                        p.append((x+y+z, x, y, z, a, b, c, d, e, f))

for pp in p: print(pp)
print(min(p, key=lambda x: x[0]))
