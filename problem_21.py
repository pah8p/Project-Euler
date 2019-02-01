

AMICABLES = []

DIVS = {}

def div(n):
    try:
        return DIVS[n]
    except KeyError:
        d = [m for m in range(1, 1+int((n+1)/2)) if n % m == 0]
        DIVS[n] = d
        return d

#div = lambda n: [m for m in range(1, int(n/2)) if n % m == 0]

d = lambda n: sum(div(n))

def is_amicable(a):
    b = d(a)
    if b != a:
        return a == d(b)
    else:
        return False

amicables = [n for n in range(1, 10001) if is_amicable(n)]

print(amicables)
print(sum(amicables))
    
print(div(8128))
print(sum(div(8128)))
