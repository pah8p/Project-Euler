
N = 10

def a(n):
    if n == 0:
        return 2
    elif (n+1) % 3 == 0:
        return int((n + 1)*2 / 3)
    else:
        return 1

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


#print(len([n for n in range(1, N) if len(str(h(n))) > len(str(k(n)))]))

print(sum([int(m) for m in str(h(99))]))




