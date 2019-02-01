import copy

TEST = [
    [15],
    [-14, -7],
    [20, -13, -5],
    [-3, 8, 23, -26],
    [1, -4, -5, -18, 5],
    [-16, 31, 2, 9, 28, 3],
]

def build():
    randoms = []
    t = 0
    for k in range(1, 500501):
        t = (615949*t + 797807) % 2**20
        s = t-2**19
        randoms.append(s) 

##    print(randoms[-1], len(randoms), randoms[9])

    randoms = randoms[::-1]

    tri = []
    n = 1
    while True:
        _tri = []
        for m in range(n):
            _tri.append(randoms.pop())
        tri.append(_tri)

        if randoms:
            n += 1
        else:
            break

##    print(len(tri), len(tri[-1]), tri[-1][-1], tri[3][3])

    return tri

def rotate(t):
    r = []

    n = 1
    while True:
        _r = []
        up = range(1, n+1)
        dn = up[::-1]
        for u, d in zip(up, dn):
            _r.append(t[-d][-u])
        r.append(_r)
            
        if n == len(t):
            break
        else:
            n += 1

    return r

def sum_triangle(t):
    return sum(sum(_t) for _t in t)

def min_triangle(t):

    if not t:
        return 0

    s = sum_triangle(t)
    
    bot = sum(t[-1])
    
    r_t = rotate(t)
    r_bot = sum(r_t[-1])

    rr_t = rotate(r_t)
    rr_bot = sum(rr_t[-1])

    max_row = max(bot, r_bot, rr_bot)

    if bot == max_row:
        sub_s = min_triangle(t[:-1])
    elif r_bot == max_row:
        sub_s = min_triangle(r_t[:-1])
    elif rr_bot == max_row:
        sub_s = min_triangle(rr_t[:-1])

    return min(s, sub_s)
    

    

##    if bot < 0 and r_bot < 0 and rr_bot < 0:
##
##        s = sum_triangle(t)
##
##        _t = t[:-1]
##        min_t = min_triangle(_t)
##        _r_t = rotate(_t)[:-1]
##        _rr_t = rotate(_r_t)[:-1]
##
##        if len(_rr_t) > 1:
##            mini_s = min_triangle(_rr_t)
##            return min(s, mini_s)
##        else:
##            return s
##        
##        return s
##    
##    elif bot > r_bot and bot > rr_bot:
##        return min_triangle(t[:-1])
##
##    elif r_bot > bot and r_bot > rr_bot:
##        return min_triangle(r_t[:-1])
##
##    elif rr_bot > bot and rr_bot > r_bot:
##        return min_triangle(rr_t[:-1])

import sys
#sys.setrecursionlimit(1010)
print(sys.getrecursionlimit())


#print(min_triangle(TEST))

t = build()
#print(t)
#print(rotate(t))
#print(len(t))
#print(min_triangle(t))
