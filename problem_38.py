

def pandigital(n):
    return [1, 2, 3, 4, 5, 6, 7, 8, 9] == sorted([int(m) for m in str(n)])

concat = lambda n: '%s%s' % (n, 2*n)

pandigitals = [concat(n) for n in range(9000, 10000) if pandigital(concat(n))]

print(pandigitals)
print(max(pandigitals))
