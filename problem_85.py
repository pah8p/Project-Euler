
TRIANGLE = {}

def triangle(n):
    try:
        return TRIANGLE[n]
    except KeyError:
        t = int(n*(n+1)/2)
        TRIANGLE[n] = t
        return t

def num_rectangles(w, h):
    return triangle(w) * triangle(h)

##    rectangles = []
##    for _w in range(1, w+1):
##
##        n_w = w + 1 - _w
##
##        for _h in range(1, h+1):
##
##            n_h = h + 1 - _h
##
##            rectangles.append((_w, _h, n_w*n_h))
##
##    return rectangles, sum([r[2] for r in rectangles])

for w in range(1, 100):
    if w % 1000 == 0: print(w)
    for h in range(1, w):
        recs = num_rectangles(w, h)
        #print(w, h, recs)
        if recs > 1999997 and recs < 2000003:
            print(recs, w, h)
