

F  = {1: 1}

def f(n):
    try:
        return F[n]
    except KeyError:
        _f = n * f(n-1)
        F[n] = _f
        return _f

def choose(n, r):
    return f(n)/(f(r)*f(n-r))

count = 0
for n in range(1, 101):
    for r in range(1, n):
        if choose(n, r) > 1e6:
            count += 1

print(count)
