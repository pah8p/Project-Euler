from problem_7 import sieve

primes = sieve(int(1e6))

def trunc_right(n):
    truncs = [n]
    for m in range(len(str(n))-1):
        if n > 10:
            n = int(str(n)[:-1])
            truncs.append(n)
    return truncs

def trunc_left(n):
    truncs = [n]
    for m in range(len(str(n))-1):
        if n > 10:
            n = int(str(n)[1:])
            truncs.append(n)
    return truncs

def trunc(n):
    try:
        return list(set(trunc_left(n) + trunc_right(n)))
    except ValueError:
        print(n)
        raise

def truncatable(p):

    if p < 10:
        return False

    for m in [2, 4, 6, 8]:
        if m in [int(n) for n in str(p)]:
            return False

    _truncatable = True
    for t in trunc(p):
        if t not in primes:
            _truncatable = False

    return _truncatable

truncatable = [23] + [p for p in primes if truncatable(p)]

for t in truncatable: print(t)

print(len(truncatable))

