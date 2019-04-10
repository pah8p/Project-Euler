
def cubic(n):
    return n**3

def f(n):
    return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10

def deriv(seq):
    if len(seq) == 1:
        return [0]
    return [seq[n]-seq[n-1] for n in range(1, len(seq))]

def fit(n, F):
    seq = [F(_n) for _n in range(1, n+1)]
    diffs = [seq]
    d = diffs
    while d != [0]:
        d = deriv(diffs[-1])
        diffs.append(d)
    print(diffs)
    return sum([diff[-1] for diff in diffs])

def sum_bops(n, f):
    return sum([fit(m, f) for m in range(1, n)])

print(fit(1, cubic))
print(fit(2, cubic))
print(fit(3, cubic))
print(fit(4, cubic))

print(sum_bops(4, cubic))
    
print(sum_bops(11, f))
