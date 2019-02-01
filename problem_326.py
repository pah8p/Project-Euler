import euler_tools
import copy
import collections

OFFSET = {
    0: (3, 6),
    1: (0, 1),
    2: (3, 3),
    3: (5, 4),
    4: (4, 3),
    5: (1, 1),
}


def a(n):
    try:
        _a = [0, 1, 1, 0]
        _n = 4
        m = 0
        while _n <= n:
            for k in range(0, 6):
                offset, factor = OFFSET[k]
                _a.append(offset + factor * m)
                _n += 1
            m += 1
        return _a
    except KeyboardInterrupt:
        print(_n, 100 * _n / n)
        raise (KeyboardInterrupt)


# def a(n):
#    if n > 3:
#        offset, factor = OFFSET[(n+2)%6]
#        return offset + factor * int((n-4)/6)
#    elif n == 3:
#        return 0
#    elif n == 2:
#        return 1
#    elif n == 1:
#        return 1

def link_f(n, m):
    _a = a(n)
    pairs = collections.defaultdict(int)
    for i in range(1, n + 1):
        j = 0
        s = 0
        while True:
            s += _a[i + j]
            if s % m == 0:
                pairs[i + j] = 1 + pairs[i - 1]
                break

            j += 1
            if i + j > n:
                break

    return pairs


def f(n, m):
    _a = a(n)
    pairs = []
    for i in range(1, n + 1):
        j = 0
        s = 0
        while True:
            s += _a[i + j]
            if s % m == 0:
                pairs.append((i, i + j))
            j += 1
            if i + j > n:
                break
    return pairs


def matrix():
    for n in range(1, 8):
        for m in range(6, 7):
            x = link_f(10 ** n, 10 ** m)
            print(n, m, sum([v for k, v in x.items()]))


N = 10 ** 3
M = 10 ** 1

# with euler_tools.Watch('a'):
#    _a = a(100)
#    print(_a)
#    for i, __a in enumerate(_a):
#        print(i, __a)

# with euler_tools.Watch('base'):
#    base = f(N, M)
#    print(len(base))

with euler_tools.Watch('link'):
    link = link_f(N, M)
    print(sum([v for k, v in link.items()]))

matrix()
