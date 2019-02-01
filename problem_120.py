



def r_max(a):
    r = [2]
    n = 1
    a2 = a**2
    while True:
        _r = 2*a*n % a2
        if _r in r:
            break
        else:
            r.append(_r)
            n += 2
    return max(r)

print(sum([r_max(a) for a in range(3, 1001)]))
