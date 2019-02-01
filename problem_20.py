
FACT = {0: 1}

def fact(n):
    try:
        return FACT[n]
    except KeyError:
        _fact = n * fact(n-1)
        FACT[n] = _fact
        return _fact

def sum_digits(n):
    return sum([int(s) for s in str(n)])

print(sum_digits(fact(100)))
