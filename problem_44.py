import math

def pentagon(n):
    return n*(3*n-1)/2

def is_pentagon(n):
    m = (1+math.sqrt(1+24*n))/6
    return m == int(m)

MAX = 10000

diffs = []
for n in range(1, MAX):
    for m in range(n, MAX):

        pn = pentagon(n)
        pm = pentagon(m)

        if is_pentagon(pn+pm) and is_pentagon(pm-pn):
            diffs.append(pm-pn)

print(min(diffs))
